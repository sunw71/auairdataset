import json
import time
from os import listdir
from os.path import isfile, join, splitext
import cv2

from auairtools.utils import TimeStamp

class AUAIR(object):

    def __init__(self, annotation_file, data_folder):
        """Default constracture for AUAIR Dataset objects.
        Must be initiated with the annotation file and the data (image) folder.

        Args:
            annotation_file ([type]): [description]
            data_folder ([type]): [description]
        """
        print('Loading annotations into memory...')
        tic = time.time()
        dataset = json.load(open(annotation_file, 'r'))
        assert type(dataset)==dict, 'annotation file format {} not supported'.format(type(dataset))
        print('Done (t={:0.2f}s)'.format(time.time()- tic))
        print('%d annotated frames are found.' % len(dataset['annotations']))

        print('Checking images...')
        self._valid_img_ext = ['.jpg', '.jpeg', '.png']
        onlyimgs = [f for f in listdir(data_folder) if isfile(join(data_folder, f)) and splitext(f)[1] in self._valid_img_ext]
        print('%d image files found.' % len(onlyimgs))

        self.annotations = dataset['annotations']
        self.image_names = onlyimgs
        self.data_folder = data_folder
        self.categories  = dataset['categories']
        self.num_samples = len(self.annotations)
        self.sorted_annotations = None
        '''
        print('Sanity check...')
        tic = time.time()
        diff = list(set([annot['image_name'] for annot in dataset['annotations']]) - set(onlyimgs))
        if(len(diff)==0):
            print('Done (t={:0.2f}s)'.format(time.time()- tic))
        else:
            raise RuntimeError('Image names in the annotation file and data folder does not match.')
        '''

    def get_data_by_index(self, index, ret_img=True, ret_ann=True):
        """Get image/annotation data according to index in the annotation file. Index range -> [0, num_samples]
        
        Args:
            index (int): Index of data.
            ret_img (bool, optional): Return image data. Defaults to True.
            ret_ann (bool, optional): Return annotation. Defaults to True.
        
        Returns:
            np.array, dict: image and annotation
        """

        ann=self.annotations[index] 
        img=None

        if ret_img:
            img_path = join(self.data_folder, self.annotations[index]['image_name'])
            img = cv2.imread(img_path)
  
        if ret_img == True and ret_ann == True:
            return img, ann
        elif ret_img == True and ret_ann == False:
            return img 
        elif ret_img == False and ret_ann == True:
            return ann
        else:
            raise TypeError("ret_img and ret_ann cannot be both False. At least one of them must be True.")    
                

    def get_data_by_name(self, img_name, ret_img=True, ret_ann=True):
        """Get image/annotation data according to image name.
        
        Args:
            img_name (str): image name
            ret_img (bool, optional): Return image data. Defaults to True.
            ret_ann (bool, optional): Return annotation. Defaults to True.
        
        Returns:
            np.array, dict: image and annotation
        """

        img_names = [f['image_name'] for f in self.annotations]
        index = img_names.index(img_name)

        return self.get_data_by_index(index, ret_img, ret_ann) 
   

    def get_index_by_catId(self, catId):
        """Get index of images/annotations including an object belonging to catId category.
        
        Args:
            catId (int): Id of the category.
        
        Returns:
            List of int: List of image/annotation indices.
        """
        indices = []
        for i in range(len(self.image_names)):
            ann = self.get_data_by_index(i, ret_img = False)
            cat_ids = [c['class'] for c in ann['bbox']]
            if catId in cat_ids:
                indices.append(i)
        return indices        


    def get_index_by_alt(self, alt, offset=100):
        """Get index of images/annotations captured at certain altitude.
        
        Args:
            alt (float): The fligh altitude. In millimeter.
            offset (int, optional): To create a range for target altitude. Defaults to 100.
        
        Returns:
            List of int: List of image/annotation indices.
        """
        indices = []
        for i in range(len(self.image_names)):
            ann = self.get_data_by_index(i, ret_img = False)
            altitude = ann['altitude']
            if altitude-offset<alt and altitude+offset>alt:
                indices.append(i)
        return indices   


    def display_image(self, id_or_name):
        """Display image which has given name or id.
        
        Args:
            id_or_name (int or name): Id (index) or name of the image.
        """

        if type(id_or_name)==int:
            img, ann =  self.get_data_by_index(id_or_name)
            cv2.imshow("Name: "+ann['image_name']+', Altitude: '+str(ann['altitude']), img)
        else:
            img, ann =  self.get_data_by_name(id_or_name)
            cv2.imshow("Name: "+ann['image_name']+', Altitude: '+str(ann['altitude']), img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()       


    def display_bboxes(self, id_or_name):
        """Display image with object bounding boxes which has given name or id.
        
        Args:
            id_or_name (int or name): Id (index) or name of the image.
        """

        if type(id_or_name)==int:
            img, ann =  self.get_data_by_index(id_or_name)
        else:
            img, ann =  self.get_data_by_name(id_or_name)

        for bbox in ann['bbox']:
            x = bbox['left']
            y = bbox['top']
            w = bbox['width']
            h = bbox['height']
            label = self.categories[bbox['class']]
            cv2.putText(img, label, (x, y+25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), thickness = 2, lineType=cv2.LINE_AA) 
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        
        cv2.imshow("Name: "+ann['image_name']+', Altitude: '+str(ann['altitude']), img)
        cv2.waitKey() 
        cv2.destroyAllWindows()      
    

    def _sort_by_time(self, annotations):
        newlist = sorted(annotations, key=lambda k: TimeStamp(k['time'])) 
        return newlist

    def get_frame_seqeunces(self, seq_len=5, window_gap=200, overlap=4):

        self.sorted_annotations = self._sort_by_time(self.annotations)


        samples = []
        
        i = 0

        # Create TimeStamp for given window gap.
        window_t = TimeStamp({'year': 0,
            'month': 0,
            'day': 0,
            'hour': 0,
            'min': 0,
            'sec': 0,
            'ms': window_gap})

        # Iterate over sorted annotations (sorted by time).
        while i<self.num_samples:
            sample = []
            
            # Current length of sample seq.
            curr_length = 0

            # First frame of the sample seq.
            first_frame = self.sorted_annotations[i]
            sample.append(first_frame)
            curr_t = TimeStamp(first_frame['time'])

            if i+seq_len>=self.num_samples:
                break

            skip_flag = False
            for j in range(1, seq_len):
                next_frame = self.sorted_annotations[i+j]
                next_t  = TimeStamp(next_frame['time'])
                diff_t = next_t-curr_t

                if diff_t <= window_t:
                    sample.append(next_frame)
                    curr_t = next_t

                else:
                    skip_flag = True
                    #print("[INFO] Frames skipped due to large time difference:") 
                    #for s in sample:
                    #    print(s)
                    #print("Too far:", next_frame)    
                    #print() 
                    break 

            if(len(sample)!=seq_len):
                assert RuntimeError("Sample length (%d) does not equal to seq_len (%d)" % (len(sample), seq_len))           

            else:
                #print() 
                #for s in sample:
                #    print(s)
                #print()                 
                samples.append(sample)

            if skip_flag==False:
                i += seq_len - overlap
            elif skip_flag==True:
                i += j    

        return samples

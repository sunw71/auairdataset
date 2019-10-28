from auairtools.auair import AUAIR

# Paths to annotation file and source data.
annotFile = '/home/ilker/Desktop/baum/workspace/DATASET/annotations.json'
dataDir = '/home/ilker/Desktop/baum/workspace/DATASET/images'

# Create a AUAIR object.
auairdataset = AUAIR(annotation_file=annotFile, data_folder = dataDir)

##############################################################
########## Get image and annotation for given index ##########
##############################################################
ret_index = 0
print("Get image and annotation with index %d" %ret_index)
img, ann = auairdataset.get_data_by_index(ret_index)
print('Image shape: ', img.shape)
print('Annotation: ', ann)
print("Done")
##############################################################


##############################################################
########## Get image and annotation for given name ###########
##############################################################
ret_name = "frame_20190905112522_x_0004462.jpg"
print("Get image and annotation with name %s" %ret_name)
img, ann = auairdataset.get_data_by_name(ret_name)
print('Image shape: ', img.shape)
print('Annotation: ', ann)
print("Done")
##############################################################


##############################################################
### Get index of images including certain object categories ##
##############################################################
ret_cat = 5
print("Get index by category ids %s" %ret_cat)
indices = auairdataset.get_index_by_catId(ret_cat)
print('Indices (first 3 samples for sake of space): ', indices[:3])
for i in indices[:3]:
    ann = auairdataset.get_data_by_index(i, ret_img=False) 
    print('Image name: ', ann['image_name'])
    print('Annotation: ', ann)
print("Done")
##############################################################


##############################################################
###### Get index of images captured in certain altitudes #####
##############################################################
ret_alt = 5000
print("Get index by altitude (mm) %s:" %ret_alt)
indices = auairdataset.get_index_by_alt(ret_alt)
print('Indices: ', indices[:3])
for i in indices[:3]:
    ann = auairdataset.get_data_by_index(i, ret_img=False) 
    print('Image name: ', ann['image_name'])
    print('Annotation: ', ann)
print("Done")
##############################################################


##############################################################
######### Display images for given key index or name #########
##############################################################
ret_index = 7
print("Display image which has index %d:" %ret_index)
auairdataset.display_image(ret_index)

ret_name = "frame_20190905112522_x_0004462.jpg"
print("Display image which has name %s:" %ret_name)
auairdataset.display_image(ret_name)

print("Done")
##############################################################


##############################################################
######## Display images with object bounding boxes  ##########
##############################################################
ret_index = 7
print("Display image which has index %d:" %ret_index)
auairdataset.display_bboxes(ret_index)

ret_name = "frame_20190905112522_x_0004462.jpg"
print("Display image which has name %s:" %ret_name)
auairdataset.display_bboxes(ret_name)

print("Done")
##############################################################
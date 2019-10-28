from auairtools.auair import AUAIR

annotFile = '/home/ilker/Desktop/baum/workspace/DATASET/annotations.json'
dataDir = '/home/ilker/Desktop/baum/workspace/DATASET/images'


auairdataset = AUAIR(annotation_file=annotFile, data_folder = dataDir)

##############################################################
########## Get image and annotation for given index ##########
##############################################################
ret_index = 0
print("Get image and annotation with index %d" %ret_index)
img, ann = auairdataset.get_data_by_index(ret_index)
print('Image shape: ', img.shape)
print(ann)
print("Done")
##############################################################


##############################################################
########## Get image and annotation for given name ###########
##############################################################
ret_name = "frame_20190905112522_x_0004462.jpg"
print("Get image and annotation with name %s" %ret_name)
img, ann = auairdataset.get_data_by_name(ret_name)
print('Image shape: ', img.shape)
print(ann)
print("Done")
##############################################################


##############################################################
### Get index of images including certain object categories ##
##############################################################
ret_cat = 5
print("Get index by category ids %s" %ret_cat)
indices = auairdataset.get_index_by_catId(ret_cat)
print('Indices: ', indices[:3])
for i in indices[:3]:
    print(auairdataset.get_data_by_index(i, ret_img=False))
##############################################################


##############################################################
###### Get index of images captured in certain altitudes #####
##############################################################
ret_alt = 5000
print("Get index by altitude (mm) %s" %ret_alt)
indices = auairdataset.get_index_by_alt(ret_alt)
print('Indices: ', indices[:3])
for i in indices[:3]:
    print(auairdataset.get_data_by_index(i, ret_img=False))
##############################################################

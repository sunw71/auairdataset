# This script can convert your AU-AIR annotations to YOLO Format
import json
data = open(r'annotations.json') #Pass in the path for AU-AIR annotation file
ann_file = json.load(data)
ann_list = ann_file['annotations']
b = [i.get('bbox') for i in ann_list] #b is a list which contains the bbox parameters for YOLO Conversion
b = b[:10]
# print(b)

name = []
for i in ann_file['annotations']:
    name.append(i.get('image_name'))

# print(name)
YOLO_LABELS_PATH = r'yolo_annotation_folder/'  # Pass in a folder to save the YOLO Annotation Files

for a in range(0,len(b)):
    c = b[a]
    dw = 1/1920
    dh = 1/1080
    file = name[a]
    file = file.replace('jpg','txt')
    out_file = open(YOLO_LABELS_PATH + '/' + file, 'w')
    for i in range(0,len(c)):
        x = c[i]['left'] + c[i]['width']/2
        x = x*dw
        y = c[i]['top'] + c[i]['height']/2
        y = y*dh
        w = c[i]['width'] * dw
        h = c[i]['height'] * dh
        label = (round(x,6),round(y,6),round(w,6),round(h,6))
        out_file.write(str(c[i]['class']) + " " + " ".join(str(f'{x:.6f}') for x in label) + '\n')
out_file.close()
            
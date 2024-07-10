import json
import base64
import os

tsv_file = 'train_set/SAM-1.tsv'
index_file = 'train_set/SAM-1.lineidx'
f1 = open(tsv_file, 'w')
f2 = open(index_file, 'w')
"""
Example code: write a single image and its json annotation to
    tsv_file: save the image and annotation (forms one data piece)
    index_file: save the tsv index of each data piece
"""
ann_start = 0
img_dir = "JPEGImages"
json_dir = "Annotations"

img_list = os.scandir("JPEGImages")
for ins in img_list:
    name = (ins.name).replace('.jpg','')
    json_file = os.path.join(json_dir,'p_'+name+'.json')
    f3 = open(json_file,'r')
    image_file = os.path.join(img_dir,name+'.jpg')
    ann = json.load(f3)
    anno = json.dumps(ann)
    img = open(image_file, 'rb').read()
    img = base64.b64encode(img).decode('utf-8')
    lent = 0
    # save image_file name
    length = f1.write("%s\t"%image_file)
    lent += length
    # save annotation
    length = f1.write("%s\t"%anno)
    lent += length
    # save image
    length = f1.write("%s\n"%img)
    lent += length
    f2.write("%d %d\n"%(ann_start, lent))
    ann_start += lent
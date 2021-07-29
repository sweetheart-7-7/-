# 划分数据集

import os
from tqdm import tqdm
from random import shuffle

base = 'dataset/voc/'
img_base = 'VOCdevkit/VOC2012/JPEGImages/'
xml_base = 'VOCdevkit/VOC2012/Annotations/'

images_list = os.listdir(os.path.join(base, img_base))
shuffle(images_list)

split_num = int(0.9 * len(images_list))

with open(os.path.join(base, 'trainval.txt'), 'w') as f:
    for im in tqdm(images_list[:split_num]):
        img_id = im[:-4]
        line = '{}{}.jpg {}{}.xml\n'.format(img_base, img_id, xml_base, img_id)
        f.write(line)

with open(os.path.join(base, 'test.txt'), 'w') as f:
    for im in tqdm(images_list[split_num:]):
        img_id = im[:-4]
        line = '{}{}.jpg {}{}.xml\n'.format(img_base, img_id, xml_base, img_id)
        f.write(line)


labels = ['car', 'van', 'bus', 'others']

with open('dataset/voc/label_list.txt', 'w') as f:
    for lbl in labels:
        f.write(lbl+'\n')

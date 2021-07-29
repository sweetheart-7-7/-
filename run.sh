cd /home/aistudio/PaddleDetection-master/

python tools/train.py -o num_classes=4 -c configs/yolov3_darknet_coc.yml --eval --use_vdl=Ture

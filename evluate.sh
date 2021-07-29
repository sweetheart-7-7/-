# 评估模型

python -u tools/eval.py -c configs/yolov4/yolov4_cspdarknet_voc.yml -o weights=output/yolov4_cspdarknet_voc/best_model

python tools/export_model.py -c configs/yolov4/yolov4_cspdarknet_voc.yml --output_dir=./inference_model -o weights=output/yolov4_cspdarknet_voc/best_model.pdparams

from mmdeploy.apis import torch2onnx
from mmdeploy.backend.sdk.export_info import export2SDK

img = 'demo/demo.jpg'
work_dir = 'mmdeploy_models/mmdet/onnx_v8'
save_file = 'end2end.onnx'
deploy_cfg = '../mmdeploy/configs/mmdet/detection/detection_onnxruntime_static.py'
model_cfg = 'configs/rtmdet/rtmdet_tiny_smoke_azuria.py'
model_checkpoint = '/home/masrour/mmdetection/workspace/workdir/finetune_smoke/from_coco_rtmdet_tiny_syncbn_fast_2xb1-lr0.0005-10e_-smoke/best_coco_bbox_mAP_epoch_2.pth'
device = 'cpu'

# 1. convert model to onnx
torch2onnx(img, work_dir, save_file, deploy_cfg, model_cfg,
           model_checkpoint, device)

# 2. extract pipeline info for inference by MMDeploy SDK
export2SDK(deploy_cfg, model_cfg, work_dir, pth=model_checkpoint,
           device=device)
# /home/masrour/ONNXTOCaffe/onnx2caffe/_operators.py make_input
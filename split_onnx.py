import onnx 




input_path = "/home/masrour/mmdetection/mmdeploy_models/mmdet/onnx_v8/end2end.onnx"
output_path= "/home/masrour/ONNXToCaffe/onnx_split_2.onnx"
input_names = ["input"]
#output_names = ["/backbone/stage1/stage1.0/conv/Conv_output_0"]#["/bbox_head/rtm_cls.0/Conv_output_0","/bbox_head/rtm_cls.1/Conv_output_0","/bbox_head/rtm_cls.1/Conv_output_0","/bbox_head/rtm_cls.1/Conv_output_0","/bbox_head/rtm_reg.1/Conv_output_0","/bbox_head/rtm_reg.2/Conv_output_0"]#,"/bbox_head/rtm_cls.1/Conv","/bbox_head/rtm_cls.2/Conv","/bbox_head/rtm_reg.1/Conv","/bbox_head/rtm_reg.1/Conv"]
output_names = ["/bbox_head/rtm_reg.0/Conv_output_0","/bbox_head/rtm_reg.1/Conv_output_0","/bbox_head/rtm_reg.2/Conv_output_0","/bbox_head/rtm_cls.0/Conv_output_0","/bbox_head/rtm_cls.1/Conv_output_0", "/bbox_head/rtm_cls.2/Conv_output_0"]
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
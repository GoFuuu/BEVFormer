import torch 

checkpoint = torch.load('/home/gofuuu/BEVFormer/work_dirs/bevformer_tiny_1_add_relu/latest.pth')
#print(checkpoint['state_dict'].keys())
for parameter in checkpoint.parameters():
    print(parameter)
# 检查权重文件中是否存在名为 self.query_concat 的参数
if 'level_embeds' in checkpoint['state_dict'].keys():
    print("Found 'self.query_concat' parameter in the checkpoint.")
else:
    print("Could not find 'self.query_concat' parameter in the checkpoint.")
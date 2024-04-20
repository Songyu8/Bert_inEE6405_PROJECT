import torch

# # 加载 .pt 文件
# data = torch.load('../bert_data/LCSTS.train.2.bert.pt')

# # 打印文件中包含的内容
# print(data.keys())

data = torch.load('../bert_data/cnndm.train.0.bert.pt', map_location=torch.device('cpu'))

print(data)
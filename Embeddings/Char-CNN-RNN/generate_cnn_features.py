import os 
import csv
import torchvision
import torchvision.transforms as transforms
import torch
import torch.nn as nn
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import pickle
import numpy as np
data_folder = '/media/user/DATA/ArtImages'


net = torchvision.models.resnet50(pretrained=True)
net = nn.Sequential(*(list(net.children())[:-2]))     

net.eval()
net.cuda()



files = []
with open(os.path.join(data_folder, 'new_info.csv'), 'r') as file:
	reader = csv.reader(file, delimiter='|')
	header = next(reader)
	for k, row in enumerate(reader):
		files.append([k, row[0]])
len_data = len(files)
batch_size = 36

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

t = transforms.Compose([transforms.Resize(512), transforms.TenCrop(224), 
	transforms.Lambda(lambda crops: torch.stack([normalize(transforms.ToTensor()(crop)) for crop in crops]))])
out_folder = './images/'
if not os.path.exists(out_folder):
	os.makedirs(out_folder)
max_file_length = 40
manifest = open(os.path.join('./art_data', 'manifest.txt'), 'w')
for k, f in files:
	img = t(Image.open(os.path.join(data_folder, f)).convert('RGB')).cuda()
	with torch.no_grad():
		feat = net(img).mean(-1).mean(-1)
	feat = feat.permute(1,0).unsqueeze(0)
	file_name = str(k+1).zfill(5)+'.'+f.replace('/', '_')[:-4]
	out_file_name = os.path.join(out_folder, file_name[:max_file_length]+'.npy')
	np.save(out_file_name, feat.cpu().numpy())
	manifest.write(file_name[:max_file_length]+'.t7'+'\n')
	

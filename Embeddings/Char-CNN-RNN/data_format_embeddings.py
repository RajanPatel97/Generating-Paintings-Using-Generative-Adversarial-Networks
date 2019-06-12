import csv
import os
import random
import numpy as np
import torchfile
#from torch.utils.serialization import load_lua
data_folder = '/media/user/DATA/ArtImages'

out_base_f = './art_data'
if not os.path.exists(out_base_f):
	os.makedirs(out_base_f)
max_folder_length = 34
vocab = {}
alphabet = list(" abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}.")
alp_dict = {}
for k, a in enumerate(alphabet):
	alp_dict[a] = k
n_char_array = 200
with open(os.path.join(data_folder, 'new_info.csv'), 'r') as file:
	reader = csv.reader(file, delimiter='|')
	header = next(reader)
	train_ids = open(os.path.join(out_base_f, 'trainvalids.txt'), 'w')

	for k, row in enumerate(reader):
		print(row)
		#file_name = str(k+1).zfill(5)+'.'+f.replace('/', '_')[:-4]
		#out_file_name = os.path.join(out_folder, file_name[:max_file_length]+'.npy')
		new_folder = row[0].replace('/', '_')[:-4][:max_folder_length]
		out_text_folder = os.path.join(out_base_f, 'text_c10',  str(k+1).zfill(5)+'.'+new_folder)
		if not os.path.exists(out_text_folder):
			os.makedirs(out_text_folder)
		### Text
		file_name = new_folder + '.txt'
		with open(os.path.join(out_text_folder, file_name), 'w') as txt_file:
			txt_file.write(row[-1])
		npy_text_name = str(k+1).zfill(5)+'.'+new_folder + '.npy'
		char_array = np.zeros((1, n_char_array, 1))
		for n_c, c in enumerate(row[-1].lower()):
			if n_c == n_char_array:
				break
			if c not in alp_dict:
				continue
			char_array[0,n_c,0] = alp_dict[c]
		np.save(os.path.join(out_base_f, 'text_c10', npy_text_name), char_array)
		if random.random() < 0.8:
			train_ids.write(str(k+1).zfill(5)+'\n')
#torchfile.load('/media/adrian/SSD/finegrained-text-embeddings-pytorch/cvpr2016_cub/text_c10/170.Mourning_Warbler.t7')

#load_lua('/media/adrian/SSD/finegrained-text-embeddings-pytorch/cvpr2016_cub/text_c10/170.Mourning_Warbler.t7')

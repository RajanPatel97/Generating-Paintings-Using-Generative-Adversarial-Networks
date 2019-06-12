npy4th = require 'npy4th'

subfolders = {}
counter = 0

local files = paths.dir('./art_data/text_c10')
table.sort(files)

for i = 1, #files do
    counter = counter + 1
    file = files[i]
    if file ~= nil and file ~= '.' and file ~= '..' and file:match("[^.]+$") == 'npy' then
	print('./art_data/text_c10/' .. file)
	array = npy4th.loadnpy('./art_data/text_c10/' .. file)
	file = file:gsub("npy", "t7")
	print(file)
	
	torch.save('./art_data/text_c10/' .. file, array)
    end
end
-- read a .npy file into a torch tensor


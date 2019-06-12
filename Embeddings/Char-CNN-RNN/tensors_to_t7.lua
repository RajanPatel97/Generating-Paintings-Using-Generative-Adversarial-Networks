npy4th = require 'npy4th'

subfolders = {}
counter = 0

local files = paths.dir('./images')
table.sort(files)

for i = 1, #files do
    counter = counter + 1
    file = files[i]
    if file ~= nil and file ~= '.' and file ~= '..' then
	print('./images/' .. file)
	array = npy4th.loadnpy('./images/' .. file)
	file = file:gsub("npy", "t7")
	
	torch.save('./images/' .. file, array)
    end
end
-- read a .npy file into a torch tensor


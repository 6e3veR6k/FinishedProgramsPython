import os, shutil
from datetime import datetime

# list of input information
current_dir = os.getcwd()
# print current_dir
copied_dir = "C:\\Users\\bezvershuk_do\\Desktop"
# print copied_dir
file_mask = ".py"
# print file_mask


def dict_files(current_dir, copied_dir, mask=''):
	dict_files = {}
	for filename in os.listdir(current_dir):
		path = os.path.join(current_dir, filename)
		if os.path.isfile(path) and mask in filename:
			date_part_tuple = datetime.fromtimestamp(os.path.getctime(path)).utctimetuple()[:3]
			new_path = "_".join([str(date_part) for date_part in date_part_tuple])
			dict_files[filename] = (os.path.join(current_dir, filename), os.path.join(copied_dir, new_path))
	return dict_files


def make_dir(coppied_dir):
	try:
		os.makedirs(coppied_dir)
	except OSError as OSErr:
		pass






for key, value in dict_files(current_dir, copied_dir, file_mask).items():
	curr_full_path, new_path = value
	make_dir(new_path)
	shutil.copy(curr_full_path, new_path)
	print "File \n %s \n copied to dirrectory \n %s." % (curr_full_path, new_path)
	print "="*100

mask = "*.py"


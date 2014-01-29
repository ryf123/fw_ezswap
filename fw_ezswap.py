import sys,getopt
import os.path, time
import shutil
def error_handler():
	print "fw_ezswap -d destination location -s sourcefile location"
	sys.exit(2)
def file_not_exist(file_name):
	print "\nfile:"+file_name+" does not exist\n"
	sys.exit(2)
def check_time_stamp(file_name):
	print "file "+file_name +" last modeified time :"+time.ctime(os.path.getmtime(file_name))+"\n"
def remove_file(file_name):
	os.remove(file_name)
	if(not os.path.exists(file_name)):
		print "\nfile:"+file_name+" removed"
	else:
		"Unable to remove file:"+file_name+"\n"
		sys.exit(2)
def remove_dir(dir_name):
	os.removedirs(dir_name)
def copy_file(src,dst):
	shutil.copy(src, dst)
if __name__=="__main__":
	print sys.argv[1:]
	try:
		opts, args = getopt.getopt(sys.argv[1:],"d:s:")
	except:
		sys.exit(2)
	for opt, arg in opts:
		if opt=="-d":
			des_loc = arg
			if(not os.path.exists(des_loc)):
				file_not_exist(des_loc)
			des_fw_lte_lib = des_loc+"\\modem_proc\\fw_lte\\bin\\QSAFA\\fw_lte.lib"
			if(os.path.exists(des_fw_lte_lib)):
				check_time_stamp(des_fw_lte_lib)
			des_fw_common_lib = des_loc+"\\modem_proc\\fw_common\\bin\\QSAFA\\fw_common.lib"
			if(os.path.exists(des_fw_common_lib)):
				check_time_stamp(des_fw_common_lib)	
		elif opt =="-s":
			src_loc = arg
			if(not os.path.exists(src_loc)):
				file_not_exist(src_loc)
			src_fw_lte_lib = src_loc+"\\modem_proc\\fw_lte\\bin\\QSAFA\\fw_lte.lib"
			if(not os.path.exists(src_fw_lte_lib)):
				file_not_exist(src_fw_lte_lib)
			check_time_stamp(src_fw_lte_lib)
			src_fw_common_lib = src_loc+"\\modem_proc\\fw_common\\bin\\QSAFA\\fw_common.lib"
			if(not os.path.exists(src_fw_common_lib)):
				file_not_exist(src_fw_common_lib)
			check_time_stamp(src_fw_common_lib)			
		else:
			error_handler()
	if(os.path.exists(des_fw_lte_lib)):
		print "removing fw lte lib \n"
		remove_file(des_fw_lte_lib)
	if(os.path.exists(des_fw_common_lib)):
		print "removing fw common lib"
		remove_file(des_fw_common_lib)
	print "copying fw lte lib\n"
	copy_file(src_fw_lte_lib,des_fw_lte_lib)
	print "copying fw common lib\n"
	copy_file(src_fw_common_lib,des_fw_common_lib)
	des_fw_lte_api = des_loc+"\\modem_proc\\fw_lte\\api"
	src_fw_lte_api = src_loc+"\\modem_proc\\fw_lte\\api"
	des_fw_common_api = des_loc+ "\\modem_proc\\fw_common\\api"
	src_fw_common_api = src_loc+"\\modem_proc\\fw_common\\api"
	print "removing fw lte api \n"
	remove_dir(des_fw_lte_api)
	print "removing fw common lib \n"
	remove_dir(des_fw_common_api)
	if(not os.path.exists(src_fw_lte_api)):
		file_not_exist(src_fw_lte_api)
	if(not os.path.exists(src_fw_common_api)):
		file_not_exist(src_fw_common_api)
	print "copying fw lte api\n"	
	shutil.copytree(src_fw_lte_api, des_fw_lte_api, False, None)
	print "copy fw common api\n"
	shutil.copytree(src_fw_common_api, des_fw_common_api, False, None)
	
	

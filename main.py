import os
import re

def update_version():
  #build this dict, probably from user variables during deployment
  #or get from env variables
  file_replacetext_dict = {
    "SCONSTRUCT": "point=",
    "VERSION" : "ADLMSDK_VERSION_POINT= "
  }

  #loop through the dict
  for filename, replace_text in file_replacetext_dict.items():
    print(filename, replace_text)

    #get file name with path
    full_name = get_filename_with_dir(filename)

    #read contents of the file
    file_data = read_file_data(full_name)

    #search and replace file's contents with build number
    file_data = re.sub(replace_text + "[\d]+", replace_text+get_build_number(), file_data)

    #write updated data to the same file
    write_file_data(full_name, file_data)

#get build number
def get_build_number():
  return os.environ["BuildNum"]

#get source path
def get_source_path():
  return os.environ["SourcePath"]

#get full file name with directory
def get_filename_with_dir(filename):
  return get_source_path() + "/develop/global/src/" + filename

#read file data for given file
def read_file_data(filename_with_path):
  with open(filename_with_path, 'r') as file :
    filedata = file.read()
  return filedata

#write data to the given file 
def write_file_data(filename_with_path, filedata):
  with open(filename_with_path, 'w') as file :
    file.write(filedata)


update_version()
#read_file_data('https://replit.com/@solomon911/FilthyConsiderableInterface#test_files/SConstruct.txt')
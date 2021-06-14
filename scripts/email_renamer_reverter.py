from dateutil.parser import parse
import os
import extract_msg
import hashlib

"""Removes the received datetime of an .msg email file that has previously been added as a prefix to the file name by another email_renamer script

Creates log file that lists original filepath, new filename, and file fixity. (| delimited)
"""
### set this to the name of your log file.
my_log_file = "log.txt"

### set to folder to process.
folder = r"folder"

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


log_data =[]
for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
    msg_filepath = os.path.join(folder, f)
    new_filename=f.split("#",1)[1]
    new_filepath = os.path.join(folder, new_filename)
    msg_file_md5 = md5(msg_filepath)
    #If the 'cleaned' filename already exists in the folder, the filename will not be changed back
    if not os.path.exists(new_filepath):
            os.rename(msg_filepath,new_filepath)
            log_data.append(f"{msg_filepath}|{new_filename}|{msg_file_md5}")
    else:
        print("Filename exists"+"|"+msg_filepath+"|"+msg_file_md5)
    

with open(my_log_file, "w", encoding = "utf8") as data:
    data.write("\n".join(log_data))

from dateutil.parser import parse
import os
import extract_msg
import hashlib
import os

"""Removes the rvc datetime of an msg email file as a string to the .msg file name
Delimited by a #
yyyy_mm_dd-hh_mm_ss 

creates log file that lists old f_name, new f_name, and file fixity. (| delimited)
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
    my_f = os.path.join(folder, f)
    new_f_name=f.split("#")[1]
    new_f_path = os.path.join(folder, new_f_name)
    my_md5=md5(my_f)
    #If the filename already exists in the folder, the filename will not be changed back
    if not os.path.exists(new_f_path):
            os.rename(my_f, new_f_path)
            log_data.append(f"{my_f}|{new_f_name}|{my_md5}")
    else:
        print("Filename exists"+"|"+my_f+"|"+my_md5)
    

with open(my_log_file, "w", encoding = "utf8") as data:
    data.write("\n".join(log_data))
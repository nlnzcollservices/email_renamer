from dateutil.parser import parse
import os
import extract_msg
import hashlib

""" 
Prepends the rvc datetime of an msg email file as a string to the .msg file name
Delimited by a #
yyyy_mm_dd-hh_mm_ss 

creates log file that lists old f_name, new f_name, and file fixity. (| delimited)  

"""


### set this to the name of your log file.
my_log_file = "rename_log_ld_v3.txt"

### set to folder to process.
folder = r"Z:\NDHA\testing\emails\2020"

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


root = ""
log_data = []
for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
    my_f = os.path.join(folder, f)
    msg = extract_msg.Message(my_f)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_subj = msg.subject
    msg_message = msg.body
    my_date = parse(msg_date)

    my_folder = os.path.join(root, my_date.strftime('%B_%Y'))

    if not os.path.exists(os.path.join(folder, my_folder)):
        os.mkdir(os.path.join(folder, my_folder))


    my_date_string = my_date.strftime("%Y_%m_%d-%H_%M_%S")
    if "#" not in f:
        new_f_name = my_date_string+"#"+f
    else:
        new_f_name = f
    new_f_path = os.path.join(folder,my_folder, new_f_name)
    msg.close()

    my_md5 = md5(my_f)
    os.rename(my_f,new_f_path)
    log_data.append(f"{my_f}|{new_f_name}|{my_md5}")

with open(my_log_file, "w", encoding = "utf8") as data:
    data.write("\n".join(log_data))

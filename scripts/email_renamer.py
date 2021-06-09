from dateutil.parser import parse
import os
import glob
import extract_msg
import hashlib

"""Prepends the received datetime of an msg email file as a string to the .msg file name
Delimited by a #
i.e. 'yyyy_mm_dd-hh_mm_ss#[original_filename].msg'
Acts on all .msg files in a given folder
Creates log file that lists original filepath, new filename, and file fixity. (| delimited)
"""
### set this to the name of your log file.
my_log_file = "log.txt"

### set to filepath of folder containing .msg files to process.
folder = r"folder"


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


log_data = []
for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
	msg_filepath = os.path.join(folder, f)

	msg_glob = glob.glob(msg_filepath)

	for filename in msg_glob:
		msg = extract_msg.Message(filename)
		msg_sender = msg.sender
		msg_date = msg.date
		msg_subject = msg.subject
		msg_body = msg.body
		msg_datetime = parse(msg_date)
		msg_date_string = msg_datetime.strftime("%Y_%m_%d-%H_%M_%S")
		new_filename = msg_date_string+"#"+f
		new_filepath = os.path.join(folder, new_filename)
		msg.close()

	msg_file_md5 = md5(msg_file)
	os.rename(msg_filepath,new_filepath)
	log_data.append(f"{msg_filepath}|{new_filename}|{msg_file_md5}")

with open(my_log_file, "w", encoding = "utf8") as data:
	data.write("\n".join(log_data))


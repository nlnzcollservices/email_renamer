from dateutil.parser import parse
import os
import glob
import extract_msg
import hashlib

"""Prepends the rcv datetime of an msg email file as a string to the .msg file name
Delimited by a #
yyyy_mm_dd-hh_mm_ss 

creates log file that lists old f_name, new f_name, and file fixity. (| delimited)
"""
### set this to the name of your log file.
my_log_file = "log.txt"

### set to folder to process.
folder = r"folder"


def md5(fname):
	"""generates an MD5 hash of a binary object
	Expects a file like object"""
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


log_data = []

### find all files in the given folder the end with .msg as files to process
for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
	my_f = os.path.join(folder, f)

	my_glob = glob.glob(my_f)

	for filename in my_glob:
		try:
			msg = extract_msg.Message(filename)
			msg_sender = msg.sender
			msg_date = msg.date
			msg_subj = msg.subject
			msg_message = msg.body
			my_date = parse(msg_date)
			my_date_string = my_date.strftime("%Y_%m_%d-%H_%M_%S")
			new_f_name = my_date_string+"#"+f
			new_f_path = os.path.join(folder, new_f_name)
			msg.close()
		except:
			print (f"couldn't process {filename} - might be damaged or not an email file.")

	my_md5 = md5(my_f)
	os.rename(my_f,new_f_path)
	log_data.append(f"{my_f}|{new_f_name}|{my_md5}")

with open(my_log_file, "w", encoding = "utf8") as data:
	data.write("\n".join(log_data))


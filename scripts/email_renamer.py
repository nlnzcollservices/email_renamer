from dateutil.parser import parse
import os
import glob
import extract_msg
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

folder = r"Y:\pre-deposit_prod\LD_Proj\covid_collecting\COVID-19_email\new email"

log_data = []

for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
	my_f = os.path.join(folder, f)

	my_glob = glob.glob(my_f)

	for filename in my_glob:
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

	my_md5 = md5(my_f)
	os.rename(my_f,new_f_path)
	log_data.append(f"{my_f}|{new_f_name}|{my_md5}")

with open("rename_log.txt", "w", encoding = "utf8") as data:
	data.write("\n".join(log_data))


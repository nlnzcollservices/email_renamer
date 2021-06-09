from dateutil.parser import parse
import glob
import extract_msg
import hashlib
from pathlib import Path

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

msg_files = glob.glob(folder+'/*.msg')

for msg_file in msg_files:
    msg_file_md5 = md5(msg_file)

    msg = extract_msg.Message(msg_file)
    msg_sender = msg.sender
    msg_subject = msg.subject
    msg_body = msg.body
    msg_date = msg.date
    msg.close()

    msg_datetime = parse(msg_date)
    msg_date_string = msg_datetime.strftime("%Y_%m_%d-%H_%M_%S")

    msg_filepath = Path(msg_file)
    msg_filename = msg_filepath.name
    new_filename = msg_date_string+"#"+msg_filename
    new_filepath = Path(folder).joinpath(new_filename)
    msg_filepath.rename(new_filepath)

    log_data.append(f"{msg_filepath}|{new_filename}|{msg_file_md5}")

with open(my_log_file, "w", encoding = "utf8") as data:
    data.write("\n".join(log_data))


from dateutil.parser import parse
import os
import extract_msg
import hashlib
import os

folder = r"C:\Users\granthrh\Documents\NDHA\testing\May_2020"

for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
    my_f = os.path.join(folder, f)
    new_f_name=f.split("#")[1]
    new_f_path = os.path.join(folder, new_f_name)
    os.rename(my_f, new_f_path)
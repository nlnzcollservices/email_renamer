# Email Renamer
Prepends the received datetime of a msg email file as a string to the .msg file name and can move emails into month folders based on receive date. Extracts md5 hashes for file comparisons. 

This project has three scripts:

1. email_renamer.py - renames all the .msg files in a folder with the email's received date.
2. email_renamer_month_buckets.py - within the folder containing the emails, it will rename each email and move them into a folder based on the date the email was received.
3. file_name_reverter.py - reverts the file names back. It there are any duplicate file names it will print the filename "yyyy_mm_dd-hh_mm_ss#filename.msg", but not process it.

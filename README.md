# Email Renamer
Prepends the received datetime of a msg email file as a string to the .msg file name and can move emails into month folders based on receive date.

This project has three scripts:

1. email_renamer.py - it will rename all the files in a folder with the email's received date.
2. email_renamer_month_buckets - within the  folder containing the emails, it will rename each email and move them into a folder based on the date the email was received.
3. fil_name_reverter.py - this will revert the file names back. It there are any duplicate file names it will print the filename, but not process it. 

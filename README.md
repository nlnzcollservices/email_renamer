# Email Renamer
Uses [extract_msg](https://pypi.org/project/extract-msg/) to prepend the received datetime of a msg email file as a string to the .msg file name. Move emails into folders by month based on the received date. Returns file fixity to aid file analysis.

This repo has three scripts:

1. email_renamer.py - prefixes the filenames of all .msg files in a given folder with the emails' received date.
2. email_renamer_month_buckets.py - within a given folder containing .msg files, it will rename each email and move them into a subfolder based on the date the email was received.
3. file_name_reverter.py - reverts the file names back by removing the date prefix added by one of the other email_renamer scripts. If that would lead to duplicate file names in a folder, it will print the filename "yyyy_mm_dd-hh_mm_ss#filename.msg", but not process it.

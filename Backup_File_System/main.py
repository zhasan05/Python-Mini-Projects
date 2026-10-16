import os
import shutil #copy or move files 
import datetime
import schedule #cron jobs - scheduler
import time 

source = 'D:/Projects/Python_Projects/Backup_File_System/Temp1'
destination_dir = 'D:/Projects/Python_Projects/Backup_File_System/Temp2'

def copy_to_folder(src, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(src, dest_dir)
        print(f'Folder copied to: {dest_dir}')
    except FileExistsError:
        print(f'File alrady exists in {dest}!')

# lambda allows a func to be passed into another in one single line
# Create the schedule job
schedule.every().day.at("15:26").do(
    lambda: copy_to_folder(source, destination_dir)
)

while True:
    schedule.run_pending()
    time.sleep(1)
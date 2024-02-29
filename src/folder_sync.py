# Import modules
from datetime import datetime
import os
import shutil

# Read arguments
src_folder_path = "/home/ruben/Documents/repos/veeam-test-task/test_env/src"
dest_folder_path = "/home/ruben/Documents/repos/veeam-test-task/test_env/dst"
sync_interval = ""
logs_path = ""

# Run sync process
def sync_process(src_folder, dest_folder):
    # Get a list of all files in the source folder
    files = os.listdir(src_folder)

    # Iterate through each file and copy it to the destination folder
    for file_name in files:
        print(f"FILE_NAME: {file_name}")
        # Construct full paths for the source and destination files
        source_file = os.path.join(src_folder, file_name)
        destination_file = os.path.join(dest_folder, file_name)

        if os.path.isfile(source_file):
             # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"File '{file_name}' copied successfully.")
        else:
            # Copy the file
            shutil.copytree(source_file, destination_file)
            print(f"File '{file_name}' copied successfully.")

    return 0

# Get timestamp
def get_timestamp():

    current_timestamp = datetime.now().replace(microsecond = 0)

    return current_timestamp


# Build logs
def build_logs(path, timestamp):

    return 0

sync_process(src_folder_path, dest_folder_path)


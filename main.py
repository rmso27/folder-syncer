# Import modules
from src.modules.sync.sync_func import sync_process

# Read arguments
src_folder_path = "/home/ruben/Documents/repos/veeam-test-task/test_env/src"
dest_folder_path = "/home/ruben/Documents/repos/veeam-test-task/test_env/dst"
sync_interval = 10
logs_path = ""


if __name__ == '__main__':
    sync_process(src_folder_path, dest_folder_path, sync_interval)

'''
    TODO:
    - Update folder deletion to validate if content of folder is equal to source;
    - Update script to read arguments provided by the user;
    - Update comments;
    - Update README;
'''
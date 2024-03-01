# Import modules
import sys
from src.modules.sync.sync_func import sync_process

# Read arguments
src_folder_path = sys.argv[1]
dest_folder_path = sys.argv[2]
sync_interval = int(sys.argv[3])
logs_path = sys.argv[4]

# Start script
if __name__ == '__main__':
    sync_process(src_folder_path, dest_folder_path, sync_interval)

'''
    TODO:
    - Update README;
'''
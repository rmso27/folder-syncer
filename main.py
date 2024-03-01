# Import modules
import sys

# Start script
if __name__ == '__main__':
    if len(sys.argv) == 5:
        from src.modules.sync.sync_func import sync_process
        sync_process(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
        print("The script expects 4 arguments: <SOURCE_FOLDER> <DEST_FOLDER> <SYNC_INTERVAL> <LOGS_PATH>")

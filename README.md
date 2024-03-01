# Veeam's Test Task
<br />
## Objective
<br />
Please implement a program that synchronizes two folders: source and replica. The
program should maintain a full, identical copy of source folder at replica folder.
<br />
## Requirements
<br />
- Synchronization must be one-way: after the synchronization content of the
replica folder should be modified to exactly match content of the source
folder;
- Synchronization should be performed periodically.
- File creation/copying/removal operations should be logged to a file and to the
console output;
- Folder paths, synchronization interval and log file path should be provided
using the command line arguments;
- It is undesirable to use third-party libraries that implement folder
synchronization;
- It is allowed (and recommended) to use external libraries implementing other
well-known algorithms. For example, there is no point in implementing yet
another function that calculates MD5 if you need it for the task – it is
perfectly acceptable to use a third-party (or built-in) library.
<br />
## How To
<br />
In order to execute the script, just type the following command: <br />
`python main.py <SOURCE_FOLDER> <DEST_FOLDER> <SYNC_INTERVAL> <LOGS_PATH>`

'''
    DESCRIPTION:
    In this file I've set the all of the needed synced funtions.
    The "sync_process" function continuously synchronizes files and folders between a source and
    destination directory at a specified interval, handling files and folders separately with
    appropriate logging and error handling.
'''

# Import modules
import os
import shutil
from ..logs.logs import logging
import time

# Run sync process
def sync_process(src_folder, dest_folder, sync_interval):

    '''
        NOTE:
        Here I've went with an infinite loop to keep script running
        I don't like this approach to much. Idealy a scheduled job on the server would be better.
    '''

    while True:
        try:
            # Get a list of all items in the source folder
            items = os.listdir(src_folder)

            # Iterate through each item and copy it to the destination folder
            for item_name in items:
                # Construct full paths for the source and destination items
                source_item = os.path.join(src_folder, item_name)
                destination_item = os.path.join(dest_folder, item_name)

                # Validate if it's a file or a folder
                if os.path.isfile(source_item):
                    sync_file(item_name, source_item, destination_item)
                else:
                    sync_folder(item_name, source_item, destination_item)
        except Exception as ex:
            logging.error(f"Error while executing synchronization: {ex}")

        # Wait specified sync interval
        time.sleep(sync_interval)

'''
    NOTE:
    I've segregated the sync between folders / files in 2 different functions because they are handled differently.
'''

# Folder sync
def sync_folder(item_name, source_item, destination_item):

    '''
        NOTE:
        In this function, the first thing that I do is to delete the folder if it exists. I'm doing this because in the requirements
        it says that the content of the DESTINY should be the same as the SOURCE.
    '''

    # If folder already exists in destination, delete it
    if os.path.exists(destination_item):
        try:
            shutil.rmtree(destination_item)
            logging.warning(f"Folder '{item_name}' already existed and it was DELETED FROM {destination_item}.")
        except:
            logging.error(f"Folder '{item_name}' already exists and it was not possible to delete it.")
    try:
        shutil.copytree(source_item, destination_item)
        logging.info(f"Folder '{item_name}' synced successfully FROM {source_item} TO {destination_item}.")
    except:
        logging.error(f"FAILED to copy folder '{item_name}'.")

# File sync
def sync_file(item_name, source_item, destination_item):

    # If file exists in destination, delete it
    if os.path.exists(destination_item):
        try:
            os.remove(destination_item)
            logging.warning(f"File '{item_name}' already existed and it was DELETED FROM {destination_item}.")
        except:
            logging.error(f"File '{item_name}' already exists and it was not possible to delete it.")
    try:
        shutil.copy2(source_item, destination_item)
        logging.info(f"File '{item_name}' synced successfully FROM {source_item} TO {destination_item}.")
    except:
        logging.error(f"FAILED to copy file '{item_name}'.")
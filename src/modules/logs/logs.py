'''
    DESCRIPTION:
    This module is used for setting up logging 'format'.
'''

# Import modules
import time
import logging
import sys
from logging.config import fileConfig

# Setup logging
loglevel='DEBUG'
currtime = time.localtime()
timest = time.strftime('%Y-%m-%d_%H%M', currtime)
logfile = (sys.argv[4] + "folder_sync" + "_" + timest + ".log")
fileConfig('configs/logs.ini',defaults={'logfilename': logfile, 'loglevel': loglevel})
logging = logging.getLogger('root')
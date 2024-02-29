import time
import logging
from logging.config import fileConfig

# Setup logging
loglevel='DEBUG'
currtime = time.localtime()
timest = time.strftime('%Y-%m-%d_%H%M', currtime)
logfile = ("folder_sync" + "_" + timest + ".log")
fileConfig('configs/logs.ini',defaults={'logfilename': logfile, 'loglevel': loglevel})
logging = logging.getLogger('root')
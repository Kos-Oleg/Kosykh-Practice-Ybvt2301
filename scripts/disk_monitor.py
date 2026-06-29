#!/usr/bin/env python3 
import shutil 
import logging 
 
THRESHOLD = 20 
LOG_FILE = '/var/log/disk_monitor.log' 
 
def setup_logging(): 
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%%(asctime)s - %%(levelname)s - %%(message)s') 
 
def check_disk_space(): 
    total, used, free = shutil.disk_usage('/') 
    free_percent = (free / total) * 100 
        logging.warning(f"Свободное место на диске: {free_percent:.1f}%% (ниже порога {THRESHOLD}%%)") 
    else: 
        logging.info(f"Свободное место на диске: {free_percent:.1f}%%") 
    return free_percent 
 
if __name__ == '__main__': 
    setup_logging() 
    check_disk_space() 

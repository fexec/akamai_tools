#!/bin/env/python3

import requests
import os


# Environment Variables
HOSTS_FILE_PATH = os.envget['HOSTS_FILE_PATH']


# Persist session
session = requests.Session()

# Set Proxies. 
# To be used with FoxyProxy or other browser config manager

session.proxies = {
    'http' : 'http://localhost:8000',
    'https': 'http://localhost:8000'
}


# Check for custom hosts file path else use default path
def load_hosts():
    if os.environ['HOSTS_FILE_PATH']:
        HOSTS_FILE_PATH = os.environ.get['HOSTS_FILE_PATH']
    else:
        pass


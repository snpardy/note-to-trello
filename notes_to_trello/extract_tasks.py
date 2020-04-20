import json
import os
import re

import requests

from parser import Parser


def configure_api(path=None):
    ''' Reads in api_config file and checks that all the information expected by the package is present.
        Required JSON names are:
        - key: key associated with your Trello account.
        - token: auth token to access your Trello account.
        - target_list: the list ID of the list you wish cards to be added to
    '''
    
    # personal_to_do_list = '5e7d3b9bd8355164c6ff5c3e'
    try:
        if path:
            with open(path) as f:
                cred = json.load(f)
        else:
            with open('api_config.json') as f:
                cred = json.load(f)
    except:
        raise OSError("Unable to open API config JSON. Make sure the provided path is correct \
                       or that there is a file in the working directory called 'api_config.json'")

    cred['url'] = f"https://api.trello.com/1/cards"

    if 'key' not in cred:
        raise KeyError("Name 'key' is not present in api_config file.")
    if 'token' not in cred:
        raise KeyError("Name 'token' is not present in api_config file.")
    if 'target_list' not in cred:
        raise KeyError("Name 'target_list' is not present in api_config file.")

    return cred


for directory in os.walk('.'):
    for path in directory[2]:
        



query = {
    'idList': personal_to_do_list,
    "name": "Test Card",
    "key": key,
    "token": token
    }
response = requests.request("POST",url,params=query)
print(response)

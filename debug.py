from twitchAPI.twitch import Twitch
from pprint import pprint
from elasticsearch import Elasticsearch
from datetime import datetime
import sys
import requests
sys.getdefaultencoding()


twitch = Twitch('***REMOVED***', '***REMOVED***')

file1 = open('./liste_streamer.txt', 'r')
Lines = file1.readlines()
i = 0

for line in Lines:
    print(line)
    user_info = twitch.get_users(logins=[line.strip()])

    user_name = user_info['data'][0]['display_name']

    i += 1
    print(user_name, i)

    #autre test jspre ça marche wollah

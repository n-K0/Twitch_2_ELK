from twitchAPI.twitch import Twitch
from pprint import pprint
from elasticsearch import Elasticsearch
from datetime import datetime
import sys, time, requests, calendar, datetime
sys.getdefaultencoding()

twitch = Twitch('***REMOVED***', '***REMOVED***')


file1 = open('./liste_streamer.txt', 'r')
Lines = file1.readlines()
es = Elasticsearch([{'host': '***REMOVED***', 'port': 9200}])

for line in Lines:
    
    user_info = twitch.get_users(logins=[line.strip()])

    user_name = user_info['data'][0]['display_name']
    user_id = user_info['data'][0]['id']
    channel_info = twitch.get_channel_information(user_id)
    game_id = channel_info['data'][0]['game_id']
    game_name = channel_info['data'][0]['game_name']
    stream_title = channel_info['data'][0]['title']
    date_exacte = datetime.datetime.utcnow().isoformat()

    live_info = twitch.get_streams(language='fr',game_id=game_id,user_id=user_id)
    try:    
        channel_viewer = live_info['data'][0]['viewer_count']
    except  IndexError:
        continue

    body = {
    'date': date_exacte,
    'user': user_name,
    'game': game_name,
    'title': stream_title,
    'viewers': channel_viewer
    }    
    
    res = es.index(index='zevent2021', body=body)
    print(date_exacte, res)
    with open("logs/import_twitch.log", "a") as log_file:
        log_file.write(str(date_exacte) + "(UTC) - " + str(res) + str(body) + "\n")

        

import time
import requests
import json
import threading

API_URL = "https://www.clubhouseapi.com:443/api"
TOKEN   = "b78e5cc79376274ead76aac2733f5f3edd765d37"

user_id=346734170

gifId=str("a15gMwHXeOmCc2xjG1")

def getCurrentroom(userId):
    HEADERS = {
                    "CH-Languages": "en-US",
                    "CH-Locale": "en_US",
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "CH-AppBuild": "304",
                    "CH-AppVersion": "0.1.28",
                    "CH-UserID": "1387526936",
                    "User-Agent": "clubhouse/android/1447",
                    "Connection": "close",
                    "Authorization": f"Token {TOKEN}"
                }
        
    DATA={
        "user_id": userId
    }
    response 	= requests.post(f"{API_URL}/get_feed",data=DATA, headers=HEADERS)
    json_data = json.loads(response.text)
    if(json_data['items'][0]['channel']['channel']):
        channelId=json_data['items'][0]['channel']['channel']
        data={
            "channel":channelId,
            
             }
    else:
        pass   
    
    return data
channel1= ("MEKVGKN2")
def join_channel(channel1):
    HEADERS = {
                    "CH-Languages": "en-US",
                    "CH-Locale": "en_US",
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "CH-AppBuild": "304",
                    "CH-AppVersion": "0.1.28",
                    "CH-UserID": "1387526936",
                    "User-Agent": "clubhouse/android/1447",
                    "Connection": "close",
                    "Authorization": f"Token {TOKEN}"
                }
        
    DATA = {
                "channel": channel1, 
        }
    response = requests.post(f"{API_URL}/join_channel", headers=HEADERS, data=DATA)
    json_data = json.loads(response.text)
    if response.status_code==200:
        
        join_channel(channel1)
        
def active_ping(channel):
    
        HEADERS = {
                        "CH-Languages": "en-US",
                        "CH-Locale": "en_US",
                        "Accept": "application/json",
                        "Accept-Encoding": "gzip, deflate",
                        "CH-AppBuild": "304",
                        "CH-AppVersion": "0.1.28",
                        "CH-UserID": "1387526936",
                        "User-Agent": "clubhouse/android/1447",
                        "Connection": "close",
                        "Authorization": f"Token {TOKEN}"
                    }
  
        data = {
                "channel": channel,
                "chanel_id": None
            }
        try:
            response 	= requests.post(f"{API_URL}/active_ping",data=data, headers=HEADERS)
            print (channel)
            print("pinging")
        except requests.exceptions.RequestException:
            print(response.text) 
            
        time.sleep(30)
        


def updateGif(gifId,channel):
    
        HEADERS = {
                    "CH-Languages": "en-US",
                    "CH-Locale": "en_US",
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "CH-AppBuild": "304",
                    "CH-AppVersion": "0.1.28",
                    "CH-UserID": "1387526936",
                    "User-Agent": "clubhouse/android/1447",
                    "Connection": "close",
                    "Authorization": f"Token {TOKEN}"
                }
        
        DATA = {                
                    "giphy_id":gifId,
                    "channel":channel,
                    "action":"gif_reaction"
                }
        print(DATA)
        response 	= requests.post(f"{API_URL}/gif_reaction",data=DATA, headers=HEADERS)
        print(response.status_code)
        if response.status_code==400:
            join_channel(channel1)
            print("joined")    
            getCurrentroom(channel)
            
        time.sleep(28)

while True:
    
    getCurrentroom(user_id)
    channel=getCurrentroom(user_id)
    channel=channel['channel']
    act_ping_thread = threading.Thread(target=active_ping, args=(channel,))
    gif_thread = threading.Thread(target= updateGif, args=(gifId,channel,))
    act_ping_thread.start()
    gif_thread.start()
    act_ping_thread.join()
    gif_thread.join() 


from flask import requests
import json
import random
url = "https://wqwfrkh5k1.execute-api.ap-northeast-2.amazonaws.com/kakao-2020"

def start(user, problem):
    uri = url + '/start'
    return requests.post(uri,headers={'X-Auth-Token':user},json={'problem':problem}).json()
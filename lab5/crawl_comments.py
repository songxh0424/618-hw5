import urllib3
import json
from bs4 import BeautifulSoup
import codecs
import datetime

reader = codecs.getreader("utf-8")
app_id = '176975276185964'
app_secret = '39c0a736cfd732bc153e87bb0d1b92e1'

# url = 'https://graph.facebook.com/v2.10/wsj?fields=posts%%7Bcomments%%7D&access_token=%s|%s' % (app_id, app_secret)
getid_url = 'https://graph.facebook.com/v2.10/wsj?fields=id&access_token=%s|%s' % (app_id, app_secret)
req = requests.get(getid_url)
data = req.json()

url = 'https://graph.facebook.com/v2.10/%s/comments?filter=stream&access_token=%s|%s' % (data['id'], app_id, app_secret)
req = requests.get(url)
raw = req.json()

http = urllib3.PoolManager()
req = http.request('GET', url)

data = req.data
data = data.decode('utf-16')
data_js = json.loads(data)

test_url = 'https://graph.facebook.com/v2.10/wsj?fields=id,name&access_token=%s|%s' % (app_id, app_secret)

req = http.request('GET', test_url)
data = req.data
data_json = json.loads(data.decode('utf-8'))

import requests

raw = json.loads(req.text)

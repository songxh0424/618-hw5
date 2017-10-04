import requests
import json
import re

url_posts = 'https://graph.facebook.com/v2.10/nytimes/posts?since=20 september 2017&until=27 september 2017&limit=100&access_token=%s|%s' % (app_id, app_secret)

req = requests.get(url_posts)
data = req.json()

## get post ids
ids = [dic['id'] for dic in data['data']]
## get all comments under each post
comments = []
for i in ids:
    url = 'https://graph.facebook.com/v2.10/%s/comments?filter=stream&limit=3000&access_token=%s|%s' % \
        (i, app_id, app_secret)
    req = requests.get(url)
    data_com = req.json()['data']
    comments += [dic['message'] for dic in data_com]

with open('comments.txt', 'w+', encoding = 'utf-8') as f:
    for c in comments:
        f.write(c + '\n')

## ignores non-ascii characters, but also loses some spanish characters
# with open('comments-bytes.txt', 'wb+') as f:
#     for c in comments:
#         f.write((c + '\n').encode('ascii', 'ignore'))

## experimenting emoji removal
myre = re.compile(u'['
    u'\U0001F300-\U0001F64F'
    u'\U0001F680-\U0001F6FF'
    u'\U0001F910-\U0001F9EF'
    u'\U0001F1E0-\U0001F1FF'
    u'\U0000203C'
    # u'\U000000A9-\U0000269C'
    u'\U000026A0-\U0001F18E'
    # u'\U0001F190-\U0001F251'
    u'\u2600-\u26FF\u2700-\u27BF]+', 
    re.UNICODE)

with open('comments-noemo.txt', 'w+', encoding = 'utf-8') as f:
    for c in comments:
        f.write(myre.sub('', c + '\n'))

## comments without any emoji
comments_emoless = [myre.sub('', c + '\n') for c in comments]

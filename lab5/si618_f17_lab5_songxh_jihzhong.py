import requests
import json
import re
import random
import csv

url_posts = 'https://graph.facebook.com/v2.10/nytimes/posts?since=20 september 2017&until=27 september 2017&limit=100&access_token=%s|%s' % (app_id, app_secret)

req = requests.get(url_posts)
data = req.json()

## get post ids
ids = [dic['id'] for dic in data['data']]
## get all comments under each post
post_ids = []
comment_ids = []
comments = []
for i in ids:
    url = 'https://graph.facebook.com/v2.10/%s/comments?filter=stream&limit=3000&access_token=%s|%s' % \
        (i, app_id, app_secret)
    req = requests.get(url)
    data_com = req.json()['data']
    post_ids += [i for dic in data_com]
    comment_ids += [dic['id'] for dic in data_com]
    comments += [dic['message'] for dic in data_com]

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

## comments without any emoji
comments_emoless = [myre.sub('', c).replace('\n', ' ') for c in comments]
## remove empty comments
cmnt_lst = list(zip(post_ids, comment_ids, comments_emoless))
for i in range(len(cmnt_lst)-1, -1, -1):
    if cmnt_lst[i][2].strip() == '':
        cmnt_lst.pop(i)

cmnt_kept = random.sample(cmnt_lst, 100)

with open('si618_f17_lab5_random_sample_100_comments_songxh_jhzhong.csv', 'w+', encoding = 'utf-8') as f:
    w = csv.writer(f)
    w.writerow(['pagename','post_id','comment_id','comment'])
    for c in cmnt_kept:
        w.writerow(['nytimes', *c])


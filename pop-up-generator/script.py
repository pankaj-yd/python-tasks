import json
import urllib.request
import string
import random
from random import randint
import webbrowser
import os

count = 50
API_KEY = os.environ['API_KEY']
random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))
random_IDS = []

for data in results['items']:
    random_IDS.append(data['id']['videoId'])

random_URL = 'https://www.youtube.com/embed/{}'.format(random_IDS[randint(0, 49)])

webbrowser.open_new_tab(random_URL)

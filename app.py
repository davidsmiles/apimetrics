import json

from apimetrics import ApiMetrics
from config import *

api = ApiMetrics()

with open('keywords.json', 'r') as f:
    keywords = json.load(f)

for keyword in keywords[:10]:
    url = f'http://www.apimetrics.de/api/google?user={API_USERNAME}&password={API_KEY}&service=serps&' \
          f'results=500&start=0&keyword={keyword}'
    data = api.make_request(url)
    if data:
        api.send_to_db(data=data, keyword=keyword)

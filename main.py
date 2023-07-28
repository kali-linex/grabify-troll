import requests
from bs4 import BeautifulSoup
import sys

ua, link = sys.argv[1:]

s = requests.session()
s.headers['user-agent'] = ua

html = s.get(link).text
bs = BeautifulSoup(html, 'html.parser')
fields = {f['name']: f['value'] for f in bs.find_all("input", {'type': 'hidden'})}
s.post(link, data=fields)

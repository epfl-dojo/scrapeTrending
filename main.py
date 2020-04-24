#!/usr/bin/python3

import requests

from bs4 import BeautifulSoup


html_page = requests.get('https://github.com/trending')
html_txt = html_page.text
print(html_txt)

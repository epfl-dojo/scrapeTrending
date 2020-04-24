#!/usr/bin/python3

import requests

from bs4 import BeautifulSoup


html_page = requests.get('https://github.com/trending')
html_txt = html_page.text

soup = BeautifulSoup(html_txt, 'html.parser')
names = soup.findAll("div", { "class" : "Box" })

paragraphs = soup.find('article')
for paragraph in paragraphs:
    print (paragraph.text)

    # print(names)

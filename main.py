#!/usr/bin/python3

import requests

from bs4 import BeautifulSoup


html_page = requests.get('https://github.com/trending')
html_txt = html_page.text

soup = BeautifulSoup(html_txt, 'html.parser')
names = soup.findAll("div", { "class" : "Box" })

projects = soup.findAll('article', {"class" : "Box-row"})


for project in projects:
    title = project.h1.a
    print(title.text)
    # print ("title = " project.find)
    # print ("description = " project.find)
    # print ("author = " project.find)
    # print ("language = " project.find)
    # print ("stars = " project.find)
    # print ("forks = " project.find)
    # print (project.text)

    # print(names)

#!/usr/bin/python3

import requests, collections
from bs4 import BeautifulSoup

ProjectDetail = collections.namedtuple("ProjectDetail", ["author", "title", "description", "language", "stars", "forks", "url"])

html_page = requests.get('https://github.com/trending')
html_txt = html_page.text

soup = BeautifulSoup(html_txt, 'html.parser')
names = soup.findAll("div", { "class" : "Box" })

projects = soup.findAll('article')


for project in projects:

    dum, author, title = project.h1.a['href'].split("/")

    print(title)
    print(author)
    description = project.p.text.strip()
    print(description)
    # stars = project.findAll("div span")
    raw_language = project.find("span", itemprop="programmingLanguage")
    if raw_language:
        language = raw_language.text
    else
        language = "Not found"

    raw_star, raw_fork, *_ = project.findAll('a', {"class": "d-inline-block"})
    if raw_star:
        star = "".join(raw_star.text.split()).replace(",", "")
    else
        star = "not found"

    if raw_fork:
        fork = raw_fork.text.strip().replace(",", "")
    else
        fork = "not found"

    print('-'*10)

    ProjectDetail(auther=author, title=title, description=description, language=raw_language.text)

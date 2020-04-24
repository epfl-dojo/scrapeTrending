#!/usr/bin/python3

import argparse
import collections
import json
import requests 

from bs4 import BeautifulSoup

ProjectDetail = collections.namedtuple("ProjectDetail", ["author", "title", "description", "language", "star", "fork", "url"])

parser = argparse.ArgumentParser(description="Fetch github trending repos")
parser.add_argument('--since', default='today', help="set time range")

args = parser.parse_args()
print(args.since)

html_page = requests.get('https://github.com/trending')
html_txt = html_page.text

soup = BeautifulSoup(html_txt, 'html.parser')
names = soup.findAll("div", { "class" : "Box" })

projects = []
for project in soup.findAll('article'):

    dum, author, title = project.h1.a['href'].split("/")

    description = project.p.text.strip()
    # stars = project.findAll("div span")
    raw_language = project.find("span", itemprop="programmingLanguage")
    if raw_language:
        language = raw_language.text
    else:
        language = "Not found"

    raw_star, raw_fork, *_ = project.findAll('a', {"class": "d-inline-block"})
    if raw_star:
        star = "".join(raw_star.text.split()).replace(",", "")
    else:
        star = "not found"

    if raw_fork:
        fork = raw_fork.text.strip().replace(",", "")
    else:
        fork = "not found"

    projects.append(ProjectDetail(author=author, title=title, description=description, language=language, star=star, fork=fork, url=''))

print(json.dumps(projects))
	    

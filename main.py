#!/usr/bin/python3

import requests

from bs4 import BeautifulSoup

# class Project
#     def __init__(project):
#         dum,self.author,self.title = project.h1.a['href'].split("/")

#         self.description = project.p.text.strip()

#         __str__():


html_page = requests.get('https://github.com/trending')
html_txt = html_page.text

soup = BeautifulSoup(html_txt, 'html.parser')
names = soup.findAll("div", { "class" : "Box" })

projects = soup.findAll('article', {"class" : "Box-row"})


for project in projects:

    dum,author,title = project.h1.a['href'].split("/")
    description = project.p.text.strip()
    # stars = project.findAll("div span")
    infospans = project.findAll("div") #.select("span") # stars[0].findChildrens()
    print(infospans)
    # language = infospans[0].find(span).text()
    # print(language)
    # oneStar = stars.findAll('a', {"class" : " muted-link d-inline-block mr-3"})
    
    
    
    
    # stars = project.findAll(div[2]/a[1])
    # forks =
    # language =
    # print(author)
    # print(title)
    # print(description)
    # print(stars)
    # print(oneStar)

    exit()

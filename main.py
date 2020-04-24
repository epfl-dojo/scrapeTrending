#!/usr/bin/python3
import argparse
import collections
import json
import requests 
import logging

from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify, request, make_response

ProjectDetail = collections.namedtuple("ProjectDetail", ["author", "title", "description", "language", "star", "fork", "url"])

app = Flask(__name__)

@app.route("/")
def main():
    docs = []
    for route, view in app.view_functions.items():
        docs.append("{}: {}".format(route, view.__doc__))
    return "<br/>".join(docs)

@app.route("/trending")
def get_trending():
    """Return the latest trending repository of github.
    """
    logging.info(request.args)
    resp = requests.get('https://github.com/trending', params=request.args)
    if not resp.ok:
        return make_response("error from source url", resp.status_code)
    html_txt = resp.text

    soup = BeautifulSoup(html_txt, 'html.parser')
    names = soup.findAll("div", { "class" : "Box" })

    projects = []
    for project in soup.findAll('article'):

        dum, author, title = project.h1.a['href'].split("/")

        raw_description = project.p
        if raw_description:
            description = raw_description.text.strip()
        else:
            description = ''
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

    return jsonify({"projects": [project._asdict() for project in projects], "source_url": resp.url})

if __name__ == "__main__":
    #main()
    app.run(debug=True)
#    flask.F
    #args = parser.parse_args()
    #print(args.since)

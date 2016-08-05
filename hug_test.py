#!/usr/bin/env python
# encoding: utf-8

"""An example of writing an API to scrape hacker news once, and then enabling usage everywhere"""
import hug
import requests


@hug.local()
@hug.cli()
@hug.get()
def top_post(section: hug.types.one_of(('news', 'newest', 'show'))='news'):
    """Returns the top post from the provided section"""
    '''
    cli:hug -f hug_test.py  -c top_post
    http:hug -f hug_test.py
    '''
    #content = requests.get('https://news.ycombinator.com/{0}'.format(section)).content
    #text = content.decode('utf-8')
    #return text.split('<tr class=\'athing\'>')[1].split("<a href")[1].split(">")[1].split("<")[0]
    #return "hello hug"
    return section

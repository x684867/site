#!/usr/bin/env python

import Flask
import os
import sys


class RouterClass:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def show_homePage(self):
        articleFiles=os.listdir('./articles/')
        articleList=""
        for article in articleFiles:
            articleList+="<div id='articleListRow'>{}</div>".format(article)
        with open('./templates/home.html','r') as f:
            html=f.read()
            return html.replace('ARTICLE_LIST_HTML',articleList)

    def show_page(pageName):
        with open('./templates/article.html') as t:
            html=t.read()
            articleFilename='./articles/{}'.format(pageName)
            with open(articleFilename,'r') as f:
                html=html.replace('articleTitle',articleTitle)
                         .replace('articleAuthor',articleAuthor)
                         .replace('articleKeywords',articleKeywords)
                         .replace('articleDescription',articleDescription)
                         .replace('articleCopyright',articleCopyright)
                         .replace('articleFooter',articleFooter)
                         .replace('articleContent',articleContent)
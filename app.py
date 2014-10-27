# all the imports
import json
import sys
import os

from routerClass import RouterClass
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)

router=RouterClass()

@app.route('/')
def home_page():
    return router.show_homePage()

@app.route('/article/<articleName>')
    return route.show_page(articleName)

if __name__ == '__main__':
    app.run()
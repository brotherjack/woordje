'''
Created on Aug 27, 2016

@author: Thomas Adriaan Hellinger
'''
from flask import Blueprint, render_template
from flask.views import MethodView


blueprint = Blueprint("root", __name__)


class WoordjeRootView(MethodView):
    def get(self):
        return render_template('index.html')    


blueprint.add_url_rule("/", view_func=WoordjeRootView.as_view("main"))  
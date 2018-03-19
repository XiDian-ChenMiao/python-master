#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import Response

flask_app = Flask('flaskapp')

@flask_app.route('/hello')
def hello_world():
    return Response('Hello World from flask!\n', mimetype='text/plain')

app = flask_app.wsgi_app


def custom_app(environ, start_response):
    """
    A barebones WSGI application.
    This is a starting point for your own web framework.
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world from a simple WSGI application.\n']

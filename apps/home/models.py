# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 | TYLER
"""

from flask_login import UserMixin

from apps import db

class API_TOKEN(db.Model, UserMixin):

    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    app_id = db.Column(db.String(64), unique=True)
    app_secret = db.Column(db.String(64), unique=True)
    token = db.Column(db.String(300), unique=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

class URL_SETTING(db.Model, UserMixin):

    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    url_name = db.Column(db.String(64), unique=True)
    url_desc = db.Column(db.String(64), unique=True)
    url_str = db.Column(db.String(300), unique=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.url_name)
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 | TYLER
"""

from flask import render_template, request, url_for, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps import db
from apps.home import blueprint
from apps.home.models import API_TOKEN as ak

@blueprint.route('/index')
@login_required
def index():
    name = ak.query.order_by(ak.name)
    count = [i.name for i in name]
    return render_template('home/index.html', segment='home', name=name, count=count)

# Settings Page
class SettingsPage():

    @blueprint.route('/settings/api_keys', methods=['GET', 'POST'])
    @login_required
    def api_keys():
        if "submit" in request.form:
            name = request.form['name']
            token = request.form['token']

            value = ak.query.filter_by(token=token).first()
            if value:
                return render_template('home/P_settings/api_keys.html', msg="This token already exists.", success=False)

            value = ak.query.filter_by(name=name).first()
            if value:
                return render_template('home/P_settings/api_keys.html', msg="This name already exists.", success=False)

            value = ak(**request.form)
            db.session.add(value)
            db.session.commit()

            return render_template('home/P_settings/api_keys.html', msg=f"{request.form['name']}", success=True)

        return render_template('home/P_settings/api_keys.html')

    @blueprint.route('/settings/list_keys', methods=['GET', 'POST'])
    @login_required
    def list_keys():
        name = ak.query.order_by(ak.name)
        if "submit" in request.form:
            tk = request.form['post_to_delete']
            usr = ak.query.filter_by(name=tk).one()
            db.session.delete(usr)
            db.session.commit()
            return render_template('home/P_settings/list_keys.html', msg=tk, name=name)
        else:
            return render_template('home/P_settings/list_keys.html', name=name)


@blueprint.route('<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

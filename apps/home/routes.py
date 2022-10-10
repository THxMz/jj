# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 | TYLER
"""

from datetime import datetime

from flask import render_template, request, url_for, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps import db
from apps.apis.utils import get_act_id, save_act_id
from apps.apis.ty_api import get_result_from_api
from apps.home import blueprint
from apps.home.models import API_TOKEN as ak
from apps.home.models import URL_SETTING as url

@blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def index():
    name = ak.query.order_by(ak.name)
    count = [i.name for i in name]
    return render_template('home/index.html', name=name, count=count)

# Settings Page
class SettingsPage:

    @blueprint.route('/settings/api_keys', methods=['GET', 'POST'])
    @login_required
    def api_keys():
        if "submit" in request.form:
            name = request.form['name']
            appID = request.form['app_id']
            appSecret = request.form['app_secret']
            token = request.form['token']

            value = ak.query.filter_by(token=token).first()
            if value:
                return render_template('home/P_settings/api_keys.html', msg="This token already exists.", success=False)

            value = ak.query.filter_by(name=name).first()
            if value:
                return render_template('home/P_settings/api_keys.html', msg="This name already exists.", success=False)

            value = ak.query.filter_by(app_id=appID).first()
            if value:
                return render_template('home/P_settings/api_keys.html', msg="This app id already exists.", success=False)

            value = ak.query.filter_by(app_secret=appSecret).first()
            if value:
                return render_template('home/P_settings/api_keys.html', msg="This name already exists.", success=False)

            # Record to databases
            value = ak(**request.form)
            db.session.add(value)
            db.session.commit()

            # Record to Json file
            save_act_id(name)

            return render_template('home/P_settings/api_keys.html', msg=f"{request.form['name']}", success=True)

        return render_template('home/P_settings/api_keys.html')

    @blueprint.route('/settings/list_keys', methods=['GET', 'POST'])
    @login_required
    def list_keys():
        name = ak.query.order_by(ak.name)
        tk = [i.token for i in name]
        if "submit" in request.form:

            msg = request.form['delete']
            usr = ak.query.filter_by(name=msg).one()
            db.session.delete(usr)
            db.session.commit()

            save_act_id(name=msg, delete=True)

            return render_template('home/P_settings/list_keys.html', msg=msg, name=name, tk=tk)
            
        else:
            return render_template('home/P_settings/list_keys.html', name=name, tk=tk)

class DetailPage:

    @blueprint.route('/dashboard/detail/id_<n>', methods=['GET', 'POST'])
    def details(n) -> None:
        api = get_result_from_api(name=n, date='today')
        name = ak.query.order_by(ak.name)
        count = api
        status = [s['status'][0] for s in api]
        date = datetime.now().strftime("%d/%m/%y - %H:%M:%S %p")
        if 'refresh' in request.form:
            return render_template("home/detail.html", name=name, count=count, api=api, date=date)

        return render_template("home/detail.html", name=name, count=count, api=api, date=date)

class LinksPage:

    @blueprint.route('/links/link_details', methods=['GET', 'POST'])
    @login_required
    def link_details() -> None:
        if 'submit' in request.form:
            msg = request.form['delete']
            usr = url.query.filter_by(url_name=msg).one()
            db.session.delete(usr)
            db.session.commit()
        links = url.query.order_by(url.url_str)
        return render_template('home/P_links/link_details.html', links=links)

    @blueprint.route('/links/add_link', methods=['GET', 'POST'])
    @login_required
    def add_link() -> None:
        if "submit" in request.form:
            url_name = request.form['url_name']

            value = url.query.filter_by(url_name=url_name).first()
            if value:
                return render_template('home/P_links/add_link.html', msg="This url name is already exists.", success=False)

            # Record to databases
            value = url(**request.form)
            db.session.add(value)
            db.session.commit()

            return render_template('home/P_links/add_link.html', msg=f"{request.form['url_name']}", success=True)

        return render_template('home/P_links/add_link.html')
        

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

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 | TYLER
"""
import json

def get_act_id(name):
    with open(f'apps/apis/id_ads/{name}.json', 'r') as f:
        jsn = json.load(f)
        return [i for i in jsn[name]]

def save_act_id(name, delete:bool = False):
    import os
    if delete == True:
        os.remove(f'apps/apis/id_ads/{name}.json')
        return

    import requests
    try:
        access_token = [i[4] for i in get_facebook_cred()][0]
        url = f"https://graph.facebook.com/v15.0/me/adaccounts?fields=name,account_id&access_token={access_token}"
        headers = {}
        r = requests.get(url = url, headers = headers)
        fb_ads_account_data = r.json()
        fb_ads_accounts = fb_ads_account_data['data']
        jsn = {
            name : []
        }
       
        for i in fb_ads_accounts:
            jsn[name].append(
                {
                    "name" : i['name'],
                    "account_id" : i['account_id'],
                    "id" : i['id']
                }
            )
        
        with open(f"apps/apis/id_ads/{name}.json", 'w+') as f:
            json.dump(jsn, f, indent=4)

    except Exception as ex:
        print(ex)

def get_facebook_cred():
    import sqlite3
    return sqlite3.connect('apps/db.sqlite3').execute("SELECT * from token").fetchall()

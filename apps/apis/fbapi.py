#!/usr/bin/python3
import sys
import requests
import json
import sqlite3
 
def get_facebook_ads_account(access_token, api_version, name):
    try:
        url =  "https://graph.facebook.com/"+api_version+"/me/adaccounts?fields=name,account_id,currency,timezone_id&access_token="+access_token
 
        headers = {}
 
        r = requests.get(url = url, headers = headers)
        fb_ads_account_data = r.json()
        fb_ads_accounts = fb_ads_account_data['data']

        jsn = {
            name : [
                
            ]
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
            
 
        print(jsn)
    except:
        print("\nFunction (get_facebook_ads_account) Failed",sys.exc_info())
 
if __name__ == '__main__':
    try:
        print("Facebook Ads Account extraction process Started")
        #reading client_id json file

        import sqlite3
        db = sqlite3.connect('apps/db.sqlite3')
        data = db.execute("SELECT * FROM token").fetchall()
        for i in data:
            name = i[1]
            app_id = i[2]
            app_secret = i[3]
            access_token = i[4]
            api_version = "v15.0"
 
        accounts_details_df = get_facebook_ads_account(access_token, api_version, name)
 
    except:
        print("\nFacebook Ads Account extraction process Failed", sys.exc_info())
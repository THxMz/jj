# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 | TYLER
"""
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adsinsights import AdsInsights

from apps.apis.utils import get_act_id, get_facebook_cred


def get_result_from_api(name, date:str = None):
    ls = []
    for i in get_facebook_cred():
        app_id = i[2]
        app_secret = i[3]
        access_token = i[4]
    
    FacebookAdsApi.init(app_id, app_secret, access_token, api_version='v15.0')
    fields = ['name', 'status']
    params = {'date_preset': 'today'}
    for account in get_act_id(name):
        tempaccount = AdAccount(account['id'])
        # Ads Data
        ads_name = tempaccount.get_ads(fields, params)
        # Ad Sets Data
        ad_sets_name = tempaccount.get_ad_sets(fields, params)
        # Campaign Data
        campaign_name = tempaccount.get_campaigns(fields, params)

        # Loop for ads_name
        for ads_data in campaign_name:
            ls.append(
                {
                    "MainWallet" : account['name'],
                    "data" : {
                        "Campaign" : {
                            "id" : ads_data['id'],
                            "name" : ads_data['name'],
                            "status" : ads_data['status']
                        }
                    }
                }
            )
    print(ls)

    return ls

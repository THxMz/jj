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
    for account in get_act_id(name):
        print(account)
        tempaccount = AdAccount(account['id'])
        acc_name = tempaccount.get_ads(fields=['name'])
        cpg = tempaccount.get_campaigns(fields=['status', 'bid_strategy'])
        fields = [
            AdsInsights.Field.account_id,
            AdsInsights.Field.adset_name,
            'inline_post_engagement',
            'clicks',
            'spend',
            'ctr',
            'impressions',
            'reach',
            'cost_per_inline_link_click',
            'catalog_segment_value'
        ]

        if date != None:
            params = {
                "date_preset" : date
            }
            a = tempaccount.get_insights(fields=fields, params=params)
            acc_names = [k['name'] for k in acc_name]
            n = 0
            for aa in a:
                for cp in cpg:
                    if aa == []:
                        ls.append(
                            {
                                "account_id" : "-",
                                "clikcs" : "-",
                                "cost" : "-",
                                "ctr" : "-",
                                "impressions" : "-",
                                "once_click" : "-",
                                "reach" : "-",
                                "spend" : "-",
                            }
                        )
                    else:
                        ls.append(
                            {
                                "account_id" : aa['account_id'],
                                "account_name" : [g for g in acc_names][n],
                                "bid_strategy" : cp['bid_strategy'],
                                "clikcs" : aa['clicks'],
                                "cost" : "{:.2f}".format(float(aa['cost_per_inline_link_click'])),
                                "ctr" : "{:.2f}".format(float(aa['ctr'])),
                                "impressions" : aa['impressions'],
                                "once_click" : aa['inline_post_engagement'],
                                "reach" : aa['reach'],
                                "spend" : aa['spend'],
                                "status" : [
                                    {
                                        "id" : cp['id'],
                                        "status" : cp['status']
                                    }
                                ]
                            }
                        )
                        n += 1
        else:
            s = tempaccount.get_insights(fields=fields)
            for ss in s:
                for cp in cpg:
                        if ss == []:
                            ls.append(
                                {
                                    "account_id" : "-",
                                    "clikcs" : "-",
                                    "cost" : "-",
                                    "ctr" : "-",
                                    "impressions" : "-",
                                    "once_click" : "-",
                                    "reach" : "-",
                                    "spend" : "-",
                                }
                            )
                        else:
                            ls.append(
                                {
                                    "account_id" : ss['account_id'],
                                    "account_name" : [g for g in acc_names][n],
                                    "clikcs" : ss['clicks'],
                                    "cost" : "{:.2f}".format(float(ss['cost_per_inline_link_click'])),
                                    "ctr" : "{:.2f}".format(float(ss['ctr'])),
                                    "impressions" : ss['impressions'],
                                    "once_click" : ss['inline_post_engagement'],
                                    "reach" : ss['reach'],
                                    "spend" : ss['spend'],
                                    "status" : [
                                        {
                                            "id" : cp['id'],
                                            "status" : cp['status']
                                        }
                                    ]
                                }
                            )
                
    return ls

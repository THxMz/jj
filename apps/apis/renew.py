# import os
# token = "EAAQQcCRlKsUBAMfqpGkFR0BABD3d5tVdKZClgpTFo7buDGEOOS7y9prPKt8JsZBkhnHOkZCNx1XJc0IMZBKpYIyeQuyKrvIU478QZAaV4myf6QBkTCk5pu13v7ZCVcc1BrDK8BXISiNv2qTpZAWWC4w2PpKMJxNtZBYzzA45ZCWW18vZBjYAzBRqlLTvwnBoTSUWyTcOgQDc1H42CZB72vZB26AEZBf4IwbXsuXkZD"
# sql = f"""curl -i -X GET "https://graph.facebook.com/v15.0/oauth/access_token?grant_type=fb_exchange_token&client_id=1143973739834053&client_secret=5a13513785d17da1947a366284266d80&fb_exchange_token={token}" """
# os.system(sql)
import sqlite3
c= sqlite3.connect('apps/db.sqlite3')
c.execute("drop table url").fetchall()
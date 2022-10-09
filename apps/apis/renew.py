# import os
# sql = """curl -i -X GET "https://graph.facebook.com/v15.0/oauth/access_token?grant_type=fb_exchange_token&client_id=1143973739834053&client_secret=5a13513785d17da1947a366284266d80&fb_exchange_token=EAAQQcCRlKsUBAARbL9AEXNNm0kEfDBsyCvsldZAcIL7ub9ZBwgqMjy4gL0Tgu2dBGtHz1hVMi1vS8WTyjeWB0YwVk2Xh59xeR4P7C6mL0z3P7kLLYa3gf4eb00isMc16dVUR5zwfUyTzK3UZCjErR1KmWnRfrlKpNPadGSyS8tng6ggIq8BMadY2ZBcuPajat0sxByskjfnrRrp5glFI2jo4ZAdCZBPPwZD" """

# os.system(sql)
# "EAAQQcCRlKsUBAK396WvN4BmGjXas6YW04ljMf6ea1QdUqHm8wypiRPI0EhTF92cUdtcQZA58afzbLJYIusBkqrrlz1f6lRFBI0eyDsUZBMOEx7tr2um0HmqSKJD2Xw9c3Fd96TS5rRKynqsvONW7uS3jZAynH7xyUpHwWzZB8HqRWToJ6miz31Tu4HTRf3EZD"



import sqlite3
c= sqlite3.connect('../db.sqlite3')
c.execute("drop table token").fetchall()
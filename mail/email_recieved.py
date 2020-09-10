import json
with open('./secrets.json', "r") as json_file:
    secrets = json.load(json_file)

fromaddr = secrets["gmail_id"]
password = secrets["gmail_password"]
toaddr = secrets["gmail_id"]

# import imaplib
# M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
# M.login(fromaddr, password)
# print("INbox", M.list())
# M.select('INBOX')

# typ, data = M.search(None, "SUBJECT", "hello")
# typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
# print("Message is ", msg[0][1])
# M.close()
# M.logout()

import  gmail
from datetime import date
g = gmail.login(fromaddr, password)

mails = g.inbox().mail(after = date(2020, 9, 9))
mails[-1].fetch()

print(mails[-1].body())
g.logout()
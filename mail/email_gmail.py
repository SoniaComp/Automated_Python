import json
with open('./secrets.json', "r") as json_file:
    secrets = json.load(json_file)

fromaddr = secrets["gmail_id"]
password = secrets["gmail_password"]
toaddr = secrets["gmail_id"]

import sys
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587) # 지메일의 SMTP 설정을 구성하고 이메일 서버에 액세스 할 수 있다.
'''
# server.starttls()

# server.login(fromaddr, password)

# msg = "some nice msg"
# server.sendmail(fromaddr, toaddr, msg)

# server.quit()
'''

## 이메일 암호화
'''
이메일 메시지가 의도한 당사자가 아닌 다른사람이 읽지 못하도록 보호하는 것
이메일은 일반적으로 평문으로 전송되며, 서드파티에서 스니핑할 수 있다.
프로토콜 계층에서 암호화한다.
SSL/TLS 프로토콜을 사용해 포트 25에서 이메일을 전송한다.
STARTTLS 의 출현과 메시지 제출을 위한 포트 587  을 사용
start TLS 를 사용해 서버와 통신한다. 세션은 암호화된다.
server.ehlo()를 전송할 때, TLS 세션을 통해 서버를 식별할 수 있다.
스크린샷에서는 서버가 인증 확장을 구현하는 것을 제안한다.
'''
'''
# try:
#   server.set_debuglevel(True)

#   print("Sending ehlo")
#   server.ehlo()
  
#   if server.has_extn('STARTTLS'):
#     print("Starting TLS Session")
#     server.starttls()

#     print("Sending ehlo again")
#     server.ehlo()
# finally:
#   server.quit()
'''

## MIME으로 이메일 메시지 꾸미기

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils

msg = MIMEMultipart()
msg['Subject'] = "hello"
msg['To'] = email.utils.formataddr(('Recipient', toaddr))
msg['From'] = email.utils.formataddr(('Author', fromaddr))
body = 'Ok'
msgBody = MIMEText(body, 'plain')
msg.attach(msgBody)

'''
server.starttls()
server.login(fromaddr, password)

text = msg.as_string()
print("Text is ", text)
server.sendmail(fromaddr, toaddr, text)

server.quit()
'''

## 첨부파일
from email.mime.base import MIMEBase
from email import encoders

filename = 'attach.txt'
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=%s"%filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)

text= msg.as_string()
server.sendmail(fromaddr, toaddr, text)

server.quit()
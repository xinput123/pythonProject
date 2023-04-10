# 使用python推送邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = "xinput.xx@gmail.com"
password="Yuan,.?@1234"
mail_from = "xinput.xx@gmail.com"
mail_to = "1258533069@qq.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com',port=587)
connection.starttls()
connection.login(username, password)
connection.send_message(mimemsg)
connection.quit()



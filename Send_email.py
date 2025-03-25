#发邮件引用的库
import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
# 配置邮件用户名密码
mail_host = "smtp.qq.com"  # SMTP服务器
mail_user = ""  # 用户名
mail_pass = ""  # 密码(授权smtp服务的授权码)
 
sender = ''  # 发件人邮箱
receivers = [""]  # 接收人邮箱


def send_email(title,content):
    message = MIMEText(content, 'plain', 'utf-8')  
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
        smtpObj.login(mail_user, mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("email send successful!")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == "__main__":
    send_email('title','content')
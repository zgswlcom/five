# !/usr/bin/python
from django.shortcuts import render, HttpResponse
# Create your views here.
import smtplib
from email.mime.text import MIMEText

mailto_list = ["admin@ctolife.com"]
mail_host = "service.mail.qq.com"  # 设置服务器
mail_user = "621987"  # 用户名
mail_pass = "cqh888"  # 口令
mail_postfix = "qq.com"  # 发件箱的后缀


def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        # s.sendmail(to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False


def email(req):
    # if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "<a href='http://www.w3cschool.cn/'>W3Cschool</a>"):
        print("发送成功")
    else:
        print("发送失败")
    return HttpResponse('ok')
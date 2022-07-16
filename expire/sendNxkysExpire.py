import random
import smtplib
import string
import time
from email.mime.text import MIMEText


def send_email(receiver, count, password):
    # 接收方／发送方，接收方是一个list，可以接受多个数值
    sender = count
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    contant = """<div dir="ltr">
        ﻿亲，为不影响您正常使用，请登录网站购买套餐<
        <br><br>
        -----------------------------------------------
        您在本站的账户<font color="darkred">已经过期</font>!
        <br><br>
        续费请 <a href="https://nxkys.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://nxkys.com&amp;source=gmail&amp;ust=1638599219093000&amp;usg=AOvVaw1_o00JKGkAtJHfAIdy040a">登录官网</a>，点击<font color="red">'购买套餐'</font> <br> <br>
        续费后请<font color="red">稍等两分钟,</font>然后重新连接客户端 <br> <br>
        …………………………………………………………………………………………………………………………………………
        灵溪官方网址： <a href="https://nxkys.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://nxkys.com&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://nxkys.com</a><div class="yj6qo"></div><div class="adL"> <br> <br>
        请复制上面方地址，去浏览器打开访问
        <br><br>
        灵溪加速器防走失网址：<a href="https://awkys.github.io" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://awkys.github.io&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://awkys.github.io</a><div class="yj6qo"></div><div class="adL">
        <br>
        ********************
        已经解锁p站，奈飞等网站!
        ********************
        <br><br>
        如有任何疑问，请联系网站右下角在线客服 
		<br><br>
		科学上网，畅游Google, Youtube, Facebook, Twitter, Instagram, 谷歌学术等海外网站。
		<br><br>
        发送时间为：<font color="darkred">%s</font>
        <br><br>
        随机字符: %s
        """ % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),ran_str)


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "灵溪加速器@海外网络加速账户过期提醒&&&邮件编号:%s"%(random.randint(10000, 100000))
    message['From'] = sender
    message['To'] = receiver

    # 关于ssl
    server = smtplib.SMTP_SSL('smtp.zoho.com.cn', 465)
    try:
        # 登陆邮箱，发送邮件退出登陆
        server.login(count, password)
        server.sendmail(sender, [receiver], message.as_string())
        server.quit()
    except smtplib.SMTPException:
        print(receiver)

if __name__ == '__main__':
    f = open("/var/script/data/expire/0714nxUsedExpire.txt", "r")
    # f = open("../data/expire/0714nxUsedExpire.txt", "r")
    lines = f.readlines()
    for user in reversed(lines):
        send_email(user, 'nxe@nxbest.men', 'nx_Admin123')
        time.sleep(random.uniform(632, 850))




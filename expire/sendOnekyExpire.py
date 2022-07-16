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
        ﻿你好，你在本站的账户已过期！
        <br><br>
		续费请 <a href="https://www.oneky.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.oneky.xyz&amp;source=gmail&amp;ust=1638599219093000&amp;usg=AOvVaw1_o00JKGkAtJHfAIdy040a">登录官网</a>，点击<font color="red">'购买套餐'</font> <br> <br>
		续费后请<font color="red">稍等两分钟,</font>然后重新连接客户端 <br> <br>
		小火箭加速器-官方网址： <a href="https://www.oneky.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.oneky.xyz&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://www.oneky.xyz</a><div class="yj6qo"></div><div class="adL"> <br><br>
        复制上方链接去浏览器打开
        <br><br>
        <br><br>
        小火箭加速器防走失网址：<a href="https://onekyss.github.io" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://onekyss.github.io&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://onekyss.github.io</a><div class="yj6qo"></div><div class="adL">
        <br>
        小火箭套餐：美国，日本，香港，韩国，新加坡，英国，法国，印度等国家节点，支持8k视频，月付价格低至:18元
        <br><br>
        畅游海外网站：ins，推特，脸书，谷歌等
		<br><br>
		支持苹果，安卓，电脑等客户端同时使用
		<br><br>
        """

    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "小火箭加速器-最稳定的海外网络加速器!"
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
    f = open("/var/script/data/expire/0714onekyUsedExpire.txt", "r")
    # f = open("../data/unSignUser.txt", "r")
    lines = f.readlines()
    for user in reversed(lines):
        send_email(user, 'xhj@nxyyds.xyz', 'nx_Admin123')
        time.sleep(random.uniform(650, 850))





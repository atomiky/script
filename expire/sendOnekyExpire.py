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
        ﻿亲，您在小火箭账户已经过期！
        <br><br>
        如需继续使用，请登录网站续费后，重新连接即可。<<br><br>
		续费请 <a href="https://www.oneky.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.oneky.xyz&amp;source=gmail&amp;ust=1638599219093000&amp;usg=AOvVaw1_o00JKGkAtJHfAIdy040a">登录官网</a>，点击<font color="red">'购买套餐'</font> <br> <br>
		续费后请<font color="red">稍等两分钟,</font>然后重新连接客户端 <br> <br>
		小火箭加速器-官方网址： <a href="https://www.oneky.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.oneky.xyz&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://www.oneky.xyz</a><div class="yj6qo"></div><div class="adL"> <br><br>
        请复制上方链接去浏览器打开
        <br> <br>
        如有疑问，请联系网站右下角在线客服！
		<br><br>
		已经解锁p站，奈飞等海外网站!!!
		<br><br>
        随机字符: %s
		<br><br>
		支持 苹果，安卓，电脑等客户端同时使用。
		<br><br>
        邮件发送时间：<font color="darkred">%s</font>
        """%(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),ran_str)


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "小火箭账户过期,邮件编号::%s"%(random.randint(4000, 80000))
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
    f = open("/var/script/data/expire/oneky608Expire.txt", "r")
    # f = open("../data/unSignUser.txt", "r")
    lines = f.readlines()
    for user in lines:
        send_email(user, 'xhj@entkys.xyz', 'nx_Admin123')
        time.sleep(random.uniform(650, 850))
    # for i in range(0, len(lines) - 1, 5):
    #     send_email(lines[i], 'nxkys01@zoho.com.cn', 'fVz3eH6vBj3u')
    #     time.sleep(random.uniform(432, 450))
    #     #账户锁定
    #     # send_email(lines[i + 1], 'nxyyds@zoho.com.cn', 'H6EvV3hBEaVu')
    #     # time.sleep(random.uniform(420, 445))
    #     send_email(lines[i + 2], 'bestone@zoho.com.cn', 'D3PLnrLKAiss')
    #     time.sleep(random.uniform(410, 460))
    #     send_email(lines[i + 3], 'ocbest@zoho.com.cn', 'ntEpKQfZBrdL')
    #     time.sleep(random.uniform(400, 455))
    #     send_email(lines[i + 4], 'tkyyds@zoho.com.cn', 'W4pnjz1PZXRW')
    #     time.sleep(random.uniform(405, 445))





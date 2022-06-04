import random
import smtplib
import time
from email.mime.text import MIMEText


def send_email(receiver, count, password):
    # 接收方／发送方，接收方是一个list，可以接受多个数值
    sender = count

    contant = """<div dir="ltr">
            ﻿<font color="Blue" size=4>亲，灵溪加速器，专业团队海外运营，稳定运行六年!</font>
    		<br><br>
    		<font color="Purple" size=4>畅游Google, Youtube, Facebook, Twitter, Instagram, 谷歌学术等海外网站</font>
    		<br><br>
    		<font color="Blue" size=4>支持 苹果（iphone, Mac），安卓，电脑等客户端</font>
    		<br><br>
    		<font color="red" size=4>黄金套餐：</font><font color="Purple" size=3>美国，新加坡，日本节点，支持4k视频，月付价格:</font><font color="red" size=5>12元</font>
    		<br><br>
    		<font color="red" size=4>砖石套餐：</font><font color="Purple" size=3>美国，日本，香港，韩国，新加坡等众多节点，支持8k视频，月付价格:</font><font color="red"size=5>18元</font>
    		<br><br>
    		<font color="red" size=4>官方网址：</font> <a href="https://nxkys.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.nxkys.com&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://nxkys.com</a><div class="yj6qo"></div><div class="adL">
            <br><br>
            --> <a href="https://nxkys.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.nxkys.com&amp;source=gmail&amp;ust=1638599219093000&amp;usg=AOvVaw1_o00JKGkAtJHfAIdy040a">点击登录官网</a><--
            <br><br>
            有疑问，请联系网站右下角在线客服
            <br> <br>
    		邮件发送时间：<font color="darkred">%s</font>
    		<br><br>
            </div></div>
            """ % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "灵溪加速器 - 提供海外网络加速服务，畅游全世界网站，实现科学上网!邮件编号:%s"%(random.randint(10000, 100000))
    message['From'] = sender
    message['To'] = receiver

    # 关于ssl
    server = smtplib.SMTP_SSL('smtp.zoho.jp', 465)
    try:
        # 登陆邮箱，发送邮件退出登陆
        server.login(count, password)
        server.sendmail(sender, [receiver], message.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        print(e)
        print(receiver)

if __name__ == '__main__':
    f = open("/var/script/data/invite/nx4.txt", "r")
    # f = open("../data/nxUnSingIN3.txt", "r")
    lines = f.readlines()
    for i in range(0, len(lines) - 1, 3):
        send_email(lines[i], 'zasulqu@zohomail.jp', '7t5Yqhk9noqq')
        time.sleep(random.uniform(632, 850))
        send_email(lines[i + 1], 'yhgtigx@zohomail.jp', 'd2ZOZ508EINS')
        time.sleep(random.uniform(610, 760))
        send_email(lines[i + 2], 'nssghocd@zohomail.jp', 'Ku4egysHC20w')
        time.sleep(random.uniform(510, 740))





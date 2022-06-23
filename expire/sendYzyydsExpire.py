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
        ﻿亲，你在柚子加速器购买的会员已过期，请登录网站，购买套餐后继续使用。
        <br>
		续费请 <a href="https://www.yzyyds.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.yzyyds.xyz&amp;source=gmail&amp;ust=1638599219093000&amp;usg=AOvVaw1_o00JKGkAtJHfAIdy040a">登录官网</a>，点击首页<font color="red">'购买套餐'</font> 按钮<br> <br>
		续费后请<font color="red">稍等两分钟,</font>然后重新连接客户端 <br> <br>
		官方网址： <a href="https://www.yzyyds.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.yzyyds.xyz&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://www.yzyyds.xyz</a><div class="yj6qo"></div><div class="adL"> <br> <br>
        <br><br>
    	白银套餐：美国，日本，新加坡等国家节点，月付价格低至:15元
    	<br><br>
    	黄金套餐：美国，日本，香港，韩国，新加坡等国家节点，支持8k视频，月付价格低至:20元
    	<br><br>
        畅游海外网站:ins,推特,脸书,谷歌等!
		<br>
		支持苹果（iphone, Mac），安卓，电脑等客户端
		<br>
		48蚊7放假沃尔、39i4jwofuwfjowjfoiwfwfhwufwfjwo493082&*^(*#*(#*((*
        """


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "加速器过期提醒"
    message['From'] = sender
    message['To'] = receiver

    try:
        # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
        smtp = smtplib.SMTP('smtp.zoho.com.cn', 587)
        smtp.set_debuglevel(True)
        # smtp.ehlo()
        smtp.starttls()
        # smtp.ehlo()
        smtp.login(count, password)
        smtp.sendmail(sender, [receiver], message.as_string())
        smtp.close()

    except smtplib.SMTPException:
        print(receiver)

if __name__ == '__main__':
    f = open("/var/script/data/expire/yz608Expire.txt", "r")
    # f = open("../data/unSignUser.txt", "r")
    lines = f.readlines()
    for user in lines:
        send_email(user, 'iyz@yzyyds.xyz', 'nx_Admin123')
        time.sleep(random.uniform(502, 830))
    # for i in range(0, len(lines) - 1, 5):
    #     send_email(lines[i], 'tnmcer@outlook.com', 'Endc98765')
    #     time.sleep(random.uniform(432, 450))
    #     send_email(lines[i + 1], 'scmnvr@outlook.com', 'Huin123456')
    #     time.sleep(random.uniform(420, 445))
    #     send_email(lines[i + 2], 'uterncv@outlook.com', 'Tiun123456')
    #     time.sleep(random.uniform(410, 460))
    #     send_email(lines[i + 3], 'iurtdcd@outlook.com', 'Tiun123456')
    #     time.sleep(random.uniform(400, 455))
    #     send_email(lines[i + 4], 'uternbr@outlook.com', 'Tiun123456')
    #     time.sleep(random.uniform(405, 445))





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
            你好，柚子加速器，专业团队运营，稳定运行六年，真诚为您服务!
    		<br><br>
    		畅游Google, Youtube, Facebook, Twitter, Instagram, 谷歌学术等海外网站。
    		<br><br>
    		支持 苹果，安卓，电脑等客户端同时连接!
    		<br><br>
    		黄金套餐：美国，日本，新加坡等国家节点，月付价格低至:15元
    		<br><br>
    		砖石套餐：美国，日本，香港，韩国，新加坡等国家节点，支持8k视频，月付价格低至:20元
    		<br><br>
    		官方网址： <a href="https://www.yzyyds.xyz/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.nxkys.com&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://www.yzyyds.xyz/</a><div class="yj6qo"></div><div class="adL">
            <br>
            复制上面官方网址去浏览器打开
            <br><br>
            已解锁p站，奈飞等网站!!!
            <br>
            有任何疑问，请联系网站右下角在线客服!
            <br> <br>
    		邮件发送时间为：<font color="darkred">%s</font>
    		<br><br>
    		随机字符: %s
            </div></div>
            """ % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), ran_str)


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "柚子加速器 - 最稳定的海外网络加速器--邮件编号:%s"%(random.randint(10, 1000))
    message['From'] = sender
    message['To'] = receiver

    # 关于ssl
    server = smtplib.SMTP_SSL('smtp.zoho.com.cn', 465)
    try:
        # 登陆邮箱，发送邮件退出登陆
        server.login(count, password)
        server.sendmail(sender, [receiver], message.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        print(e)
        print(receiver)

if __name__ == '__main__':
    f = open("/var/script/data/expire/yz608Expire.txt", "r")
    # f = open("../data/invite/nx.txt", "r")
    lines = f.readlines()
    for user in lines:
        send_email(user, 'hiyz@rentky.shop', 'nx_Admin123')
        time.sleep(random.uniform(432, 880))





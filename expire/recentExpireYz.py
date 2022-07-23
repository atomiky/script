import random
import smtplib
import string
import time
from email.mime.text import MIMEText

import pymysql


def getExpireUser():
    # 打开数据库连接
    db = pymysql.connect(host='yzyyds.xyz',
                         user='root',
                         password='yz_mysql_Admin6688',
                         database='sspanel')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = """SELECT email
       FROM `user`
       where class_expire > DATE_SUB(NOW(),INTERVAL 1 HOUR)
			 and class_expire < NOW()"""

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

    user = []
    for i in results:
        user.append(i[0])

    return user


def send_email(receiver, count, password):
    # 接收方／发送方，接收方是一个list，可以接受多个数值
    sender = count
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    contant = """<div dir="ltr">
        ﻿亲，你在柚子加速器购买的会员已过期，请登录网站，购买套餐后继续使用。
        <br>
		官方网址： <a href="https://www.yzyyds.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.yzyyds.xyz&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://www.yzyyds.xyz</a><div class="yj6qo"></div><div class="adL"> <br> <br>
        <br><br>
        柚子加速器防走失网址：<a href="https://onekys.github.io" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://onekys.github.io&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://onekys.github.io</a><div class="yj6qo"></div><div class="adL">
        """


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "柚子账号过期"
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
    expireUser = getExpireUser()
    for user in reversed(expireUser):
        send_email(user, 'ryz@tkyer.xyz', 'nx_Admin123')
        time.sleep(random.uniform(60, 180))
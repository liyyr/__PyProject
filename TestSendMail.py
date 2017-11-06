from email.mime.text import MIMEText
msg = MIMEText('hello too, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = 'liyyr@eastfantasy.com'
password = 'justsmall4'
# 输入收件人地址:
to_addr = ['20507354@qq.com','developer@eastfantasy.com']
# 输入SMTP服务器地址:
smtp_server = 'smtp.ym.163.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
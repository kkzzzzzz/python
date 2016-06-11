__author__ = 'kevin.zhu'

#coding:utf-8
import urllib2, json,sys,smtplib
from email.mime.text import MIMEText

reload(sys)
sys.setdefaultencoding('utf-8')

mail_host="smtp.163.com"
mail_user="**"
mail_pass="**"
mailto_list=['**']

def send_mail(to_list,from_user,sub,content):
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = from_user
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(mail_user, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    appkey = "**"
    url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'
    req = urllib2.Request(url)
    req.add_header("apikey", appkey)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        json_result = json.loads(content)
        content_list = json_result['showapi_res_body']['contentlist']
        item = content_list[0]
        first_text = item['text']
        text_trim = first_text.replace("\r\n", "")
        length = len(text_trim)
        from_user = text_trim[0:10]
        sub = text_trim[10:22]
        content = text_trim[22:length]
        if send_mail(mailto_list,from_user,sub,content):
            print "send msg succeed"
        else:
            print "send msg failed"
    else:
        print "get joke error"

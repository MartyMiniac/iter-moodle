import requests
from bs4 import BeautifulSoup
import json

class app:
    
    cookies=''
    def __init__(self,username,password):
        self.m_username=username
        self.m_password=password
        self.login()

    def getsessionid(self):
        r=requests.get('http://136.233.14.6/moodle/login/index.php')
        soup=BeautifulSoup(r.text,'html.parser')
        self.cookies=r.cookies
        self.sessionid=soup.find('input',{'name':'logintoken'})['value']

    def getkeyinfo(self,txt):
        arr=txt.split('\n')
        js={}
        for s in arr:
            if 'M.cfg' in s:
                ind1=s.index('{')
                ind2=s.index('}')
                js=json.loads(s[ind1:ind2+1])
                break
        self.sesskey=js['sesskey']
        self.contextid=js['contextid']

    def getuserid(self,txt):
        soup=BeautifulSoup(txt,'html.parser')
        self.userid=soup.find('div',{'id':'nav-notification-popover-container'})['data-userid']

    def login(self):
        self.getsessionid()
        payload={
            'anchor': '',
            'logintoken': self.sessionid,
            'username': str(self.m_username),
            'password': str(self.m_password)
        }
        r=requests.post('http://136.233.14.6/moodle/login/index.php',data=payload,cookies=self.cookies)
        self.getkeyinfo(r.text)
        self.getuserid(r.text)
    
    def logout(self):
        url='http://136.233.14.6/moodle/login/logout.php?sesskey='+self.sesskey
        r=requests.get(url,cookies=self.cookies)
    
    def test(self):
        print(self.m_password)
        print(self.m_username)
        print(self.sessionid)
        print(self.sesskey)
        print(self.userid)
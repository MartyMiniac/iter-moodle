import requests
from bs4 import BeautifulSoup
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

    def login(self):
        self.getsessionid()
        payload={
            'anchor': '',
            'logintoken': self.sessionid,
            'username': str(self.m_username),
            'password': str(self.m_password)
        }
        r=requests.post('http://136.233.14.6/moodle/login/index.php',data=payload,cookies=self.cookies)
        #print(r.text)
        f=open('testpage.html','w')
        f.write(r.text)
        f.close()

a=app('martyminiac','Qe12ws45!')
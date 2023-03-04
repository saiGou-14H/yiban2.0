import json
import random
import time
from base64 import b64encode
from threading import Thread, RLock
from typing import Dict, AnyStr
import pandas
import requests
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Captcha:
    _user = None
    _pwd = None
    def __init__(self,_user,_pwd):
        self._user = _user
        self._pwd = _pwd


    def base64_api(self,img, typeid):
        softid = "ae34cf3e778c4703be702eb041f23c98"
        data = {"username": self._user, "password": self._pwd, "typeid": typeid, "image": img, "softid": softid}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        if result['success']:
            print(result["data"])
            return result["data"]["result"], result["data"]["id"]
        else:
            return result["message"], ''
        return "", ""

    def report_error(self, id):
        if self._user is None:
            return {'code': -1, 'msg': '打码平台账号获取失败'}
        data = {"id": id}
        ret = requests.post("http://api.ttshitu.com/reporterror.json", json=data).json()
        if ret['success']:
            return "["+id+"]验证码识别错误 "+str({'code': 1, 'msg': ret["message"], 'data': ret["data"]})
        else:
            return str({'code': -1, 'msg': ret["message"]})

    def get_balance(self):
        js={"username":self._user,"password":self._pwd}
        x=requests.get("http://api.ttshitu.com/queryAccountInfo.json",json=js)
        print(x.json())
        if(x.json().get("success")):
            balance=x.json().get("data").get("balance")
            print(balance)
        else:
            balance = -1
        return balance

#os.path.abspath(os.path.join(os.getcwd(), "../"))+
text = pandas.read_csv("./One.csv")
def YiYan() :
    YY = text.iloc[random.randint(1,len(text)-1)]
    return YY['hitokoto'],YY['from']


class BaseYiban:
    def __init__(self):
        self.session = requests.session()

    def request(
            self,
            method: str,
            url: str,
            params: Dict = None,
            headers: Dict = None,
            cookies: Dict = None,
            data: Dict = None,
            body: Dict = None,
            allow_redirects: bool = True
    ) -> requests.Response:
        if body is not None:
            body = {k: v for k, v in body.items() if v is not None}
        if data is not None and isinstance(data, dict):
            data = {k: v for k, v in data.items() if v is not None}

        # 重试五次
        for i in range(1, 6):
            response = self.session.request(method=method, url=url, params=params,
                                            data=data, headers=headers, cookies=cookies,
                                            json=body, allow_redirects=allow_redirects, timeout=20)
            return response
        self._print(f"Request Error {url}")
        raise Exception("Request Error")

    def get(self, url: str, params: dict = None, headers: dict = None,
            cookies: dict = None, allow_redirects: bool = True) -> requests.Response:
        return self.request(method='GET', url=url, params=params, headers=headers,
                            cookies=cookies, allow_redirects=allow_redirects)

    def post(self, url: str, params: dict = None, headers: dict = None,
             data: dict = None, cookies: dict = None,
             body: dict = None, allow_redirects: bool = True) -> requests.Response:
        return self.request(method='POST', url=url, params=params,
                            data=data, headers=headers, cookies=cookies,
                            body=body, allow_redirects=allow_redirects)
# 登录模块
class Login(BaseYiban):
    # iPhone 13 Pro
    UserAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                'Mobile/15E148 yiban_iOS/5.0.8 '
    # Chrome浏览器
    UserAgent2 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/96.0.4664.110 Safari/537.36 '

    # 微信浏览器
    UserAgent3 = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 ' \
                 'Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e) '

    # APP版本
    AppVersion = '5.0.11'

    def __init__(self):
        self.access_token = ''
        super().__init__()

    def get_user_access_token(self, mobile: str, password: str) -> str:
        response = self.post(
            url="https://www.yiban.cn/login/doLoginAjax",

            headers={
                'Origin': 'https://m.yiban.cn',
                'AppVersion': self.AppVersion,
                'User-Agent': self.UserAgent,
                'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'account': mobile,
                'password': password,
            }
        )
        if (response.json()["message"] != '操作成功'):
            return '','', '', False
        self.access_token = response.cookies.get_dict()['yiban_user_token']
        access_token = response.cookies.get_dict()['yiban_user_token']
        return access_token, response.json()["data"]["user_id"], response.cookies.get_dict(), True

    @staticmethod
    def encrypt_rsa(data: str) -> AnyStr:
        rsa_key = """-----BEGIN PUBLIC KEY-----
            MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA6aTDM8BhCS8O0wlx2KzA
            Ajffez4G4A/QSnn1ZDuvLRbKBHm0vVBtBhD03QUnnHXvqigsOOwr4onUeNljegIC
            XC9h5exLFidQVB58MBjItMA81YVlZKBY9zth1neHeRTWlFTCx+WasvbS0HuYpF8+
            KPl7LJPjtI4XAAOLBntQGnPwCX2Ff/LgwqkZbOrHHkN444iLmViCXxNUDUMUR9bP
            A9/I5kwfyZ/mM5m8+IPhSXZ0f2uw1WLov1P4aeKkaaKCf5eL3n7/2vgq7kw2qSmR
            AGBZzW45PsjOEvygXFOy2n7AXL9nHogDiMdbe4aY2VT70sl0ccc4uvVOvVBMinOp
            d2rEpX0/8YE0dRXxukrM7i+r6lWy1lSKbP+0tQxQHNa/Cjg5W3uU+W9YmNUFc1w/
            7QT4SZrnRBEo++Xf9D3YNaOCFZXhy63IpY4eTQCJFQcXdnRbTXEdC3CtWNd7SV/h
            mfJYekb3GEV+10xLOvpe/+tCTeCDpFDJP6UuzLXBBADL2oV3D56hYlOlscjBokNU
            AYYlWgfwA91NjDsWW9mwapm/eLs4FNyH0JcMFTWH9dnl8B7PCUra/Lg/IVv6HkFE
            uCL7hVXGMbw2BZuCIC2VG1ZQ6QD64X8g5zL+HDsusQDbEJV2ZtojalTIjpxMksbR
            ZRsH+P3+NNOZOEwUdjJUAx8CAwEAAQ==
            -----END PUBLIC KEY-----
            """
        data = bytes(data, encoding="utf8")
        encrypt = PKCS1_v1_5.new(RSA.importKey(rsa_key))
        sencrypt = b64encode(encrypt.encrypt(data))
        return sencrypt.decode("utf-8")

class Chrome:

    def __init__(self,mobile,password,captcha,run_id,console,WCBOT,data):
        self.console = console
        self.mobile=mobile
        self.password=password
        self.options = Options()
        self.options.add_argument('headless')
        # self.options.add_argument("start-maximized")

        self.service = Service(r'.\chromedriver.exe')
        self.captcha = captcha
        self.run_id = run_id
        self.WCBOT = WCBOT
        self.data=data

        #self.error_sum = 0
        if self.run_id == None:
            self.run_id = {"签到": True, "点赞": True, "易喵喵评论": True, "易喵喵发帖": True, "易伴云签到": True, "微社区评论": True,"微社区发帖": True}
        if(console==None):
            self.console = print



    def Add_Cookies(self,chrome,cookies):
        isTrue = True
        try:
            chrome.get("https://www.yiban.cn/login")
            for x in cookies:
                chrome.add_cookie(x)
            chrome.get("https://www.yiban.cn/login")
        except Exception as e:
            print(e)
            isTrue = False
            self.console("cookie错误！！")
        return chrome , isTrue

    def Login(self):
        #--------------------模拟点击登录------------------------------------#
        # self.chrome.get("https://www.yiban.cn/login")
        # self.chrome.find_element(By.ID, value="account-txt").send_keys(self.mobile)
        # self.chrome.find_element(By.ID, value="password-txt").send_keys(self.password)
        # time.sleep(1)
        # self.chrome.find_element(By.ID,value="login-btn").click()
        # -----------------------------------------------------------------#

        #api接口登录
        self.login = Login()
        self.UserAgent = self.login.UserAgent
        self.access_token, self.id ,cookies,self.isLogin= self.login.get_user_access_token(mobile=self.mobile, password=self.password)
        self.cookies = []
        if(self.isLogin):
            try:
                self.cookies.append({"name": "YB_SSID", "value": cookies["YB_SSID"]})
                self.cookies.append({"name": "yiban_user_token", "value": cookies["yiban_user_token"]})
                self.cookies.append({"name": "https_waf_cookie", "value": cookies["https_waf_cookie"]})
            except Exception as err:
                print('An exception happened: ' + str(err))
            self.run()
        else:
            self.console("["+self.mobile+"]账号或密码错误!!!")
        return self.isLogin



    def run(self):
        if(self.run_id["签到"]):
            qd = Thread(target=self.qiandao)
            qd.start()
        if(self.run_id["点赞"]):
            dz = Thread(target=self.up)
            dz.start()
        if(self.run_id["易伴云签到"]):
            yby_qd = Thread(target=self.yby_qiandao)
            yby_qd.start()
        if(self.run_id["易喵喵评论"]):
            mm_pl = Thread(target=self.mm_pl)
            mm_pl.start()
        if(self.run_id["易喵喵发帖"]):
            mm = Thread(target=self.send_mm)
            mm.start()
        if(self.run_id["微社区发帖"]):
            wsq = Thread(target=self.wsq)
            wsq.start()
        if(self.run_id["微社区评论"]):
            sq_pl = Thread(target=self.sq_pl)
            sq_pl.start()

    def send_mm(self):
        while True:
            a, b = YiYan()
            if len(a) > 5 and len(a) < 30:
                break
        data = {
            'channel': [{"boardId": "Oa1cGeM6lE65Okd", "orgId": 2006794}],
            'hasVLink': 0,
            'isPublic': 1,
            'summary': "",
            'thumbType': 1,
            'title': a,
            'content': b,
            'kind': '1',
            'id': '1'
        }
        yimiaomiao = requests.get('https://mm.yiban.cn/article/index/add',
                                  headers={'loginToken': self.access_token},
                                  allow_redirects=True,
                                  json=data)
        self.console("["+self.mobile+"]"+yimiaomiao.json()['message']+'  易喵喵发帖')


    def up(self):
        req = requests.get('https://s.yiban.cn/api/forum/getListByBoard?offset=0&count=60&boardId=Oa1cGeM6lE65Okd&orgId=2006794',
                           headers={'loginToken': self.access_token,
                                    'client':'android',
                                    'yiban_user_token':self.access_token
                                    },
                           allow_redirects=True)
        count = 1
        req_csrf=requests.post('https://s.yiban.cn/api/security/getToken',headers={'loginToken': self.access_token,
                                                                                   'client':'android',
                                                                                   'yiban_user_token':self.access_token})
        PHPSESSID = req_csrf.cookies["PHPSESSID"]
        csrf=req_csrf.json()['data']['csrfToken']
        for index in range(len(req.json()['data']['list'])-1):
            if count>30:
                break
            isup=req.json()['data']['list'][index]['isUp']
            postid=req.json()['data']['list'][index]['id']
            userid=req.json()['data']['list'][index]['user']['id']
            if isup is not True:
                chk=requests.get('https://s.yiban.cn/api/post/thumb',
                                 headers={'loginToken': self.access_token,
                                          'client':'android',
                                          'yiban_user_token':self.access_token},
                                 json={'action':'up',
                                       'postId':postid,
                                       'userId':userid},
                                 allow_redirects=True)
                self.console("["+self.mobile+"]"+chk.json()['message']+'第'+str(count)+'次 点赞 ')
                count+=1
                time.sleep(3)
    def mm_pl(self):
        yimm_url='https://mm.yiban.cn/news/index/index3?offset=0&size=40'
        mmlist = requests.get(yimm_url,
                              headers={'loginToken': self.access_token,
                                       'client': 'android',
                                       'yiban_user_token': self.access_token
                                       },
                              allow_redirects=True)
        for index in range(1,6):
            while True:
                a, b = YiYan()
                if len(a) > 5 and len(a) < 30:
                    break
            mmid = mmlist.json()['data']['list'][index]['id']
            com_mm = requests.post('https://mm.yiban.cn/news/comment/add?recommend_type=0',
                                   headers={'loginToken': self.access_token,
                                            'yiban_user_token': self.access_token, 'client': 'android',
                                            'User-Agent': self.UserAgent, },
                                   json={'id': mmid,
                                         'comment': a
                                         },
                                   allow_redirects=True)
            if (com_mm.json()["code"] == 200):
                self.del_mm_comment(mmid, int(com_mm.json()["data"]["id"]))
            self.console("["+self.mobile+"]"+'易喵喵评论 成功'+str(index)+ "次"+'['+a+']')
            time.sleep(60)

    def wsq(self):
        if (self.run_id["点赞"]):
            time.sleep(90)

        index = 1
        while index<21:
            chrome = webdriver.Chrome(options=self.options, service=self.service)
            chrome, _ = self.Add_Cookies(chrome, self.cookies)
            isInCookie =True
            try:
                if (chrome.get_cookies() == []):
                    chrome,isInCookie = self.Add_Cookies(chrome, self.cookies)
            except:
                chrome,isInCookie= self.Add_Cookies(chrome, self.cookies)
            if(isInCookie ==False):
                break
            # 格式限制
            while True:
                a, b = YiYan()
                if len(a) > 5 and len(a) < 30:
                    break


            try:
                chrome.get("https://s.yiban.cn/userPost/detail")
                WebDriverWait(chrome, 8, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, "input"))).send_keys(a)
                chrome.find_elements(By.TAG_NAME, "textarea")[0].send_keys(b)
                content = chrome.find_element(By.ID, "ueditor_0")
                chrome.switch_to.frame(content)
                p = chrome.find_elements(By.TAG_NAME, "p")[0]
                p.send_keys(b)
                time.sleep(0.2)
                chrome.switch_to.default_content()
            except Exception as err:
                self.console('An 微社区帖子 exception happened: ' + str(err))


            try:
                WebDriverWait(chrome, 8, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    "body > div.container > section > div.actions > div > button:nth-child(2) > div"))).click()
                img_LB = WebDriverWait(chrome, 8, 0.5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "shumei_captcha_popup_wrapper")))
                len1 = len(chrome.find_elements(By.CLASS_NAME, "shumei_hide"))
                img = img_LB.screenshot_as_base64
                results, id = self.captcha.base64_api(img=img, typeid=27)
                for result in results.split("|"):
                    x, y = int(result.split(",")[0]), int(result.split(",")[1])
                    print("点击坐标：", x, y)
                    time.sleep(0.5)
                    ActionChains(chrome).move_to_element_with_offset(img_LB, x - 165, y - 135).click().perform()

            except Exception as err:
                print('An exception happened: ' + str(err))

            try:
                time.sleep(1)
                print(len1,len(chrome.find_elements(By.CLASS_NAME, "shumei_hide")))
                if len(chrome.find_elements(By.CLASS_NAME, "shumei_hide")) == 5:
                    self.console('[' + a + ']')
                    self.console('[' + b + ']')
                    self.console("["+self.mobile+"]"+'微社区帖子 成功'+str(index)+ "次")
                    index+=1
                else:
                    self.console("["+self.mobile+"]"+self.captcha.report_error(id))
                    # with lock:
                    #     self.error_sum += 1
                    #     self.console("[" + self.mobile + "] 报错" + str(self.error_sum) + '次')
            except Exception as err:
                self.console('[' + a + ']')
                self.console('[' + b + ']')
                self.console("["+self.mobile+"]"+'微社区帖子 成功'+str(index)+"次")
                index += 1
                print('An exception happened: ' + str(err))
            chrome.quit()
            time.sleep(60)
        try:
            chrome.quit()
        except:
            pass

    def sq_pl(self):
        if (self.run_id["点赞"]):
            time.sleep(90)

        wsq_url='https://s.yiban.cn/api/forum/getListByBoard?offset=0&count=33&boardId=Oa1cGeM6lE65Okd&orgId=2006794'
        sqlist = requests.get(wsq_url,
                              headers={'loginToken': self.access_token,
                                       'client':'android',
                                       'yiban_user_token':self.access_token
                                       },
                              allow_redirects=True)

        req_csrf=requests.post('https://s.yiban.cn/api/security/getToken',headers={'loginToken': self.access_token,
                                                                                   'client':'android',
                                                                                   'yiban_user_token':self.access_token})
        PHPSESSID = req_csrf.cookies["PHPSESSID"]
        csrf=req_csrf.json()['data']['csrfToken']
        index = 1
        while index < 31:
            chrome = webdriver.Chrome(options=self.options, service=self.service)
            chrome, _ = self.Add_Cookies(chrome, self.cookies)
            isInCookie = True
            try:
                if (chrome.get_cookies() == []):
                    chrome,isInCookie= self.Add_Cookies(chrome, self.cookies)
            except:
                chrome,isInCookie= self.Add_Cookies(chrome, self.cookies)
            if (isInCookie == False):
                break

            while True:
                a, b = YiYan()
                if len(a) > 5 and len(a) < 30:
                    break
            postid=sqlist.json()['data']['list'][index]['id']
            userid=sqlist.json()['data']['list'][index]['user']['id']

            try:
                url = "https://s.yiban.cn/app/2004348/post-detail/" + postid
                chrome.get(url)
                WebDriverWait(chrome, 8, 0.5).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "body > div.container.with-bg > section > section.submit > div"))).click()
                WebDriverWait(chrome, 8, 0.5).until(EC.presence_of_element_located(
                    (By.TAG_NAME, "input"))).send_keys(a)
                time.sleep(0.2)
            except Exception as err:
                self.console('An 微社区评论 exception happened: ' + str(err))


            try:
                chrome.find_elements(By.CSS_SELECTOR,
                                     "body > div.container.with-bg > section > section.submit > div > div.inner > div.submit-btn.btn > svg")[
                    0].click()
                img_LB = WebDriverWait(chrome, 8, 0.5).until(EC.visibility_of_element_located(
                    (By.CLASS_NAME, "shumei_captcha_popup_wrapper")))
                len1 = len(chrome.find_elements(By.CLASS_NAME, "shumei_hide"))
                img = img_LB.screenshot_as_base64
                results , id = self.captcha.base64_api(img=img, typeid=27)
                for result in results.split("|"):
                    x, y = int(result.split(",")[0]), int(result.split(",")[1])
                    print("点击坐标：", x, y)
                    time.sleep(0.5)
                    ActionChains(chrome).move_to_element_with_offset(img_LB, x - 165, y - 135).click().perform()
            except Exception as err:
                print('An exception happened: ' + str(err))
            # if(com_sq.json()["status"]):#''删除微社区评论-5网薪''
            #     self.del_sq_comment(com_sq.json()["data"],PHPSESSID)

            try:
                time.sleep(1)
                print(len1,len(chrome.find_elements(By.CLASS_NAME, "shumei_hide")))
                if len(chrome.find_elements(By.CLASS_NAME, "shumei_hide")) == 5:
                    self.console("["+self.mobile+"]"+'微社区评论 成功'+str(index)+"次"+'['+a+']')
                    index+=1
                else:
                    self.console("["+self.mobile+"]"+self.captcha.report_error(id))
                    # with lock:
                    #     self.error_sum += 1
                    #     self.console("[" + self.mobile + "] 报错" + str(self.error_sum) + '次')
            except Exception as err:
                self.console("["+self.mobile+"]"+'微社区评论 成功'+str(index)+"次"+'['+a+'] ')
                index += 1
                print('An exception happened: ' + str(err))
            chrome.quit()
            time.sleep(60)

        try:
            chrome.quit()
        except:
            pass
        if (self.WCBOT != None):
            string = self.data.decode('utf-8')
            string = string + '|成功'
            ls = string.split('|')
            ls[2] = 'TRUE'
            self.string = ls[0] + '|' + ls[1] + '|' + ls[2] + '|' + ls[3]
            self.WCBOT.sendall(bytes(self.string, encoding='utf-8'))



    def del_mm_comment(self, mmid,id):
        url = 'https://mm.yiban.cn/news/comment/del'
        try:
            com_mm_del = requests.post(url,
                                       headers={'loginToken': self.access_token,
                                                'yiban_user_token':self.access_token},
                                       json={'newsid':mmid,
                                             'id':id
                                             },
                                       allow_redirects=True).json()
        except Exception as ex:
            print(ex)

    def qiandao(self):
        option = ''
        chk = requests.get('https://m.yiban.cn/api/v4/home?modules=checkin',
                           headers={'loginToken': self.access_token},
                           allow_redirects=True)
        req = requests.get('https://m.yiban.cn/api/v4/checkin/question',
                           headers={'loginToken': self.access_token},
                           allow_redirects=True)
        reqs = req.json()
        if reqs['response'] == 100:
            option = reqs['data']['survey']['question']['option'][0]['id']
        data={'optionId':option}
        ans = requests.post('https://m.yiban.cn/api/v4/checkin/answer',
                            headers={'loginToken': self.access_token},
                            allow_redirects=True,
                            json=data)

        if json.dumps(ans.json()['data']['status'])== "1":
            self.console("["+self.mobile+"]"+"签到成功 +2")
        else:
            self.console("["+self.mobile+"]"+"重复签到！")



    def yby_qiandao(self):
        try:
            yby_qd = webdriver.Chrome(options=self.options, service=self.service)
            # 加载cookies
            yby_qd ,isInCookie= self.Add_Cookies(yby_qd, self.cookies)
            if(isInCookie==False):
                yby_qd.quit()
                return
            yby_qd.get("https://www.yibanyun.cn/app/sign")
            try:
                time.sleep(0.5)
                yby_qd.find_element(By.CSS_SELECTOR,
                                    "body > main > section.buttons > button.submitBtn.oauth_check").click()
            except:
                pass
            yby_qd.get("https://www.yibanyun.cn/app/sign")
            yby_qd.get("https://www.yibanyun.cn/app/sign/signin")
            yby_qd.quit()
        except:
            pass





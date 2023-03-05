import os
import socketserver
import sys
import time
from threading import Thread
from PySide2 import QtWidgets
from PySide2.QtGui import QTextCursor, QIcon
from PySide2.QtWidgets import QApplication, QHeaderView
import Send
from auto_yiban import Captcha,Chrome,YiYan,Login,BaseYiban
from ui_yiban import Ui_Form



class LoginGui(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(LoginGui, self).__init__()   # 调用父类的初始化方法
        self.setupUi(self)

class UI:
    def __init__(self):
        self.app = QApplication([])
        # self.ui = QUiLoader().load('./yiban.ui')
        self.ui = LoginGui()
        self.app.setWindowIcon(QIcon('x.ico'))
        # --------------界面设置----------------#
        self.ui.setFixedSize(1175, 625)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True);
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);
        self.ui.tableWidget.verticalHeader().setHidden(True)

        # --------------全局变量----------------#
        self.User = []
        self.captcha = None
        self.run_id = {"签到":False,"点赞":False,"易喵喵评论":False,"易喵喵发帖":False,"易伴云签到":False,"微社区评论":False,"微社区发帖":False}
        self.connect()
        self.ui.show()
        sys.exit(self.CLOSE())

    def CLOSE(self):
        try:
            os.system("taskkill /f /im chromedriver.exe /t")
            self.app.exec_()
        except:
            pass

    def connect(self):
        self.ui.tableWidget.cellChanged.connect(self.getUser)
        self.ui.pushButton_4.clicked.connect(self.clearTextBrowser)
        self.ui.pushButton.clicked.connect(self.captchaLogin)
        self.ui.checkBox_qd.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_qd))
        self.ui.checkBox_dz.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_dz))
        self.ui.checkBox_mms.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_mms))
        self.ui.checkBox_mmp.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_mmp))
        self.ui.checkBox_ybyqd.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_ybyqd))
        self.ui.checkBox_wsqs.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_wsqs))
        self.ui.checkBox_wsqp.clicked.connect(lambda:self.handleButtonClick(self.ui.checkBox_wsqp))
        self.ui.pushButton_run.clicked.connect(self.pushButtonRunClick)
        self.ui.pushButton_3.clicked.connect(self.listing)





    def getUser(self):
        len = self.ui.tableWidget.rowCount()
        self.User = []
        for index in range(len):
            try:
                cfgName = self.ui.tableWidget.item(index, 0).text()
                cfgPass = self.ui.tableWidget.item(index, 1).text()
            except:
                continue
            if (cfgName is not None and cfgPass is not None):
                self.User.append([cfgName, cfgPass])
        print(self.User)

    def textBrowser(self,text):
        self.ui.textBrowser.setOverwriteMode(True)
        self.ui.textBrowser.moveCursor(QTextCursor.Start)
        self.ui.textBrowser.insertPlainText(text + '\n')
    def textBrowser_2(self,text):
        self.ui.textBrowser_2.setOverwriteMode(True)
        self.ui.textBrowser_2.moveCursor(QTextCursor.Start)
        self.ui.textBrowser_2.insertPlainText(text + '\n')


    def clearTextBrowser(self):
        self.ui.textBrowser.setPlainText("")

    def captchaLogin(self):
        c_login = Thread(target=self.CAPTCHA_T)
        c_login.start()

    def CAPTCHA_T(self):
        try:
            _user = self.ui.lineEdit_3.text()
            _pass = self.ui.lineEdit_4.text()
            if(_pass=="" or _user==""):
                self.textBrowser("[http://www.ttshitu.com/] 打码平台账号或密码不能为空！")
            else:
                captcha = Captcha(_user, _pass)
                balance = captcha.get_balance()
                print(balance)
                if (balance != -1):
                    self.ui.label_2.setText(balance)
                    self.textBrowser("登陆成功")
                    self.captcha = captcha
                    return captcha
                else:
                    self.textBrowser("[http://www.ttshitu.com/] 打码平台账号密码错误！")
                    self.ui.label_2.setText("0.0")
                    self.captcha = None
        except Exception as e:
            print(e)
            self.textBrowser("[http://www.ttshitu.com/] 打码平台异常！")
            self.captcha = None

    def handleButtonClick(self,button):
        button_text = button.text()
        self.run_id[button_text] = bool(button.checkState())

    def pushButtonRunClick(self):
        if(self.run_id["微社区发帖"]==True or self.run_id["微社区评论"]==True):
            if(self.captcha==None):
                self.textBrowser("[http://www.ttshitu.com/] 验证码任务请先登录打码平台！")
                return
        for user in self.User:
            print(user)
            Chrome(user[0], user[1], captcha=self.captcha, run_id=self.run_id,console = self.textBrowser,WCBOT=None,data=None).Login()

    def Listing(self):
        HOST = '127.0.0.1'
        try:
            PORT = int(self.ui.lineEdit_7.text())
        except:
            pass
        ADDR = (HOST, PORT)
        try:
            server = socketserver.ThreadingTCPServer(ADDR, self.Handler)  # 参数为监听地址和已建立连接的处理类
            self.textBrowser_2(str(PORT) + "端口连接成功")
            # # 监听，建立好TCP连接后，为该连接创建新的socket和线程，并由处理类中的handle方法处理?
            server.serve_forever()
        except Exception as e:
            self.textBrowser_2(str(e))
        # server.handle_timeout()


    def listing(self):
        ls = Thread(target=self.Listing)
        ls.start()

    class Handler(socketserver.BaseRequestHandler):
        BUF_SIZE = 1024
        def handle(self):
            url = "http://127.0.0.1:"+str(8005)+"/"
            global Robot
            Robot = Send.Robot(url=url, token='111', wxid='wxid_zytsdghgtn8412')
            while True:
                data = self.request.recv(self.BUF_SIZE)
                ls = data.decode('utf-8').split('|')[1].split('-')
                if len(ls) == 2:
                    isLogin = Chrome(ls[0], ls[1], captcha=Captcha("70852096","xxxxxxxx"),run_id=None, console=None,WCBOT = self.request,data=data).Login()
                    if(isLogin==False):
                        string = data.decode('utf-8')
                        string = string + '|失败'
                        ls = string.split('|')
                        ls[2] = 'FALSE'
                        wxid = ls[0]
                        time.sleep(2)
                        Robot.SendToPrivate(wxid, '账号或密码错误')
                        string = ls[0] + '|' + ls[1] + '|' + ls[2] + '|' + ls[3]
                        print("string:" + string)
                        self.request.sendall(bytes(string, encoding='utf-8'))
                else:
                    string = data.decode('utf-8')
                    string = string + '|失败'
                    ls = string.split('|')
                    ls[2] = 'FALSE'
                    wxid = ls[0]
                    time.sleep(2)
                    Robot.SendToPrivate(wxid, '格式错误')
                    string = ls[0] + '|' + ls[1] + '|' + ls[2] + '|' + ls[3]
                    print("string:"+string)
                    self.request.sendall(bytes(string, encoding='utf-8'))
                # print(len(ls))
                print('send:', 'response')


APP = UI()


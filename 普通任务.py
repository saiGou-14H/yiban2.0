from os import system

import pandas
from auto_yiban import Chrome
class Run(Chrome):
    def __init__(self,mobile,password):
        self.run_id = {"签到": True, "点赞": True, "易喵喵评论": True, "易喵喵发帖": True, "易伴云签到": True, "微社区评论": False,
                       "微社区发帖": False}
        super(Run, self).__init__(mobile,password,None,self.run_id,None,None,None)
        self.running()
        
    def running(self):
        self.Login()



if __name__ == '__main__':
    system("pause")
    df = pandas.read_excel('data.xlsx', engine='openpyxl')
    print('读取到', len(df), '个账号')
    a = input('回车运行')
    df.apply(lambda x: Run(str(x['Account']), str(x['Password'])), axis=1)
    input()

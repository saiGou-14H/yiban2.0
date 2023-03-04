import requests

class Robot :
    # 初始化的时候填 目标URL ，token，机器人的wxid
    def __init__(self,url,token,wxid) :
        self.url = url
        self.token = token
        self.wxid = wxid

    # 发送给个人 目标 信息内容
    def SendToPrivate(self,target,msg):
        print("SendMSG!!!!!!",msg)
        requests.post(self.url,
            headers={},
            json={
                'token':self.token,
                "api":"SendTextMsg",
                "robot_wxid": self.wxid,
                "to_wxid": target,
                "msg": msg
            })

    # 发送给群 群，@的用户，信息
    def SendToGroup(self,group,user,msg) :
        requests.post(self.url,
        headers = {},
        json = {
            'token':self.token,
            "api":"SendGroupMsgAndAt",
            "robot_wxid": self.wxid,# 机器人ID
            "group_wxid": group,
            "member_wxid":user,
            "msg": msg
        })

    def AccepteTransfer(self, user, pay_id, rev_id, money):
        requests.post(self.url,
        headers = {},
        json = {
            'token': self.token,
            "api": "AccepteTransfer",
            "robot_wxid": self.wxid,  # 机器人ID
            "from_wxid": user,  # user wxID
            "payer_pay_id": pay_id,  # 回调获取
            "receiver_pay_id": rev_id,  # 回调获取
            "paysubtype": 1,
            "money": money
        })
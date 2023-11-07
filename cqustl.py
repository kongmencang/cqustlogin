import requests

'''
@author:茶泡饭
@date:2023-09-02
@use:自动登录科带校园网
'''
def login():
    url = "http://aaa.cqust.edu.cn/eportal/InterFace.do?method=login"
    headers = {
        
    }
    data = {
       
    }
    response = requests.post(url,data,headers=headers).status_code




if __name__  ==  "__main__":
    login()
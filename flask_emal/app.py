#-*- coding: UTF-8 -*-
from flask import Flask,request
from email_class import Email_info
from flask_cors import CORS
app = Flask(__name__)
# 这边需要导入对于的邮件服务的代码部分
CORS(app, supports_credentials=True)
@app.route("/app")
# 这边要注意鸭
def hello_world():
    print "这边做了请求部分"
    return "return 0"

@app.route("/send_email",methods = ["POST","GET"])
def send_email():
    print request.json
    myE = Email_info("2969524644@qq.com","kkutkligbetsdejj")
    myE.send_email(request.json.get("to_addrr"),"ScCd+BB3xcru9giEAshJrVoOXM5lOlDN+99FNfjx8Cs=","hkCKcYcRYHevY8elvHud7Q==","__init__.py")
    return "OK"

@app.route("/getDetailInfo")
def more_info():
    num = request.values.get("num")
    myE = Email_info("2969524644@qq.com", "kkutkligbetsdejj")
    return myE.detail(num)
    # return "yes"
@app.route("/getDetailInfo_send")
def more_info_send():
    num = request.values.get("num")
    myE = Email_info("2969524644@qq.com", "kkutkligbetsdejj")
    return myE.detail2(num)
    # return "yes"

@app.route("/getInfo")
def get_info():
    myE = Email_info("2969524644@qq.com", "kkutkligbetsdejj")
    return_list,num_list,real_Unseen = myE.traversal_unread()
    # print(num_list)
    return {
        "code":"200",
        "data":return_list,
        "key_info" : num_list,
        "Unseen" : real_Unseen
    }
@app.route("/getListfolder")
def folder():
    myE = Email_info("2969524644@qq.com", "kkutkligbetsdejj")
    return str(myE.show_folder())


@app.route("/getSend")
def get_info2():
    myE = Email_info("2969524644@qq.com", "kkutkligbetsdejj")

    return_list,num_list,real_Unseen = myE.traversal_Send()
    # print(num_list)
    return {
        "code":"200",
        "data":return_list,
        "key_info" : num_list,
        "Unseen" : real_Unseen
    }
if __name__ == "__main__":
    app.run(debug=True)
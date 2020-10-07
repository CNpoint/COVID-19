from flask import Flask
from flask import request
from flask import render_template    # 返回模板
import Gtime
from flask import jsonify
import string
from jieba.analyse import extract_tags    #jieba提取关键字

app = Flask(__name__)

@app.route("/time")        # 定义游标
def get_time():
    return Gtime.get_time()



@app.route("/c1")
def get_c1_data():
    data = Gtime.get_c1_data()
    return jsonify({"confirm": data[0],  "heal": data[1], "dead": data[2]})   #  从数据库获取数据

@app.route("/c2")
def get_c2_data():
    res = []  #定义一个空的表
    for mapdata in Gtime.get_c2_data():
        print(mapdata)
        res.append({"name":mapdata[0],"value":int(mapdata[1])})   #城市，感染者数量追加到res
    return jsonify({"data":res})


@app.route("/l1")
def get_l1_data():
    data = Gtime.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:     # 切片，把前面0增加的天数全部去掉,用string
        day.append(a.strftime("%m-%d")) #a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}) # 拿到的数据封装到前端去

@app.route("/l2")
def get_l2_data():
    data = Gtime.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})

@app.route("/r1")
def get_r1_data():
    data = Gtime.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


@app.route("/r2")
def get_r2_data():
    data = Gtime.get_r2_data()
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)  # 移除热搜数字
        v = i[0][len(k):]  # 切片，获取热搜数字
        ks = extract_tags(k)  # 使用jieba 提取关键字
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"kws": d})


@app.route('/')
def hello_world():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()

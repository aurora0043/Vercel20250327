from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>陳琬昀Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=yun>傳送使用者暱稱</a><br>"
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>琬昀簡介網頁</a><br>"
    return homepage


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    # 設定時區為 UTC+8
    tz = timezone(timedelta(hours=8))
    now = datetime.now(tz)  # 根據 UTC+8 時區獲取當前時間
    return render_template("today.html", datetime=str(now))  # 傳遞時間給模板

@app.route("/about")
def me():
    return render_template("rwd.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    w = request.values.get("work")
    return render_template("welcome.html", name=user, work=w)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
        return result
    else:
        return render_template("account.html")


if __name__ == "__main__":
    app.run()

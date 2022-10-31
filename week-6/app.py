from curses import meta
from tkinter import INSERT
from unicodedata import name
from xml.etree.ElementTree import Comment
from flask import Flask, session, request, redirect, render_template, url_for
from mysql.connector import errorcode, MySQLConnection
import mysql.connector
from mysql.connector import (connection)



app= Flask (__name__, static_folder="static", static_url_path="/")
app.secret_key="try it"

cnx = connection.MySQLConnection(user='root', password='',
                                host='127.0.0.1',
                                database='website')
cursor=cnx.cursor
try:
    if cnx.is_connected():
        # 顯示資料庫版本
        db_Info = cnx.get_server_info()
        print("資料庫版本：", db_Info)
        # 顯示目前使用的資料庫
        cursor = cnx.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)
        
        cursor.execute("SELECT id,username,password FROM member")
        for i in cursor:
            print(i)
        
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

# INDEX
@app.route("/")
def index():
    if 'user' in session:
        return redirect("/member")
    return render_template("homepage.html")

#SIGN-UP
@app.route("/signup", methods=["POST"])
def signup():
    reg_acct=request.form['user']
    reg_pwd=request.form['p']
    reg_name=request.form['name']
    cursor.execute("SELECT * FROM member WHERE username = %s",(reg_acct,))
    account=cursor.fetchone()
    print(reg_acct)
    print(reg_name)
    print(reg_pwd)
    if account:
        message=request.args.get("message", "帳號已經被註冊！") 
        return redirect(url_for("error", message=message))
    elif len(reg_acct)==0 or len(reg_pwd)==0 or len(reg_name)==0:
        message=request.args.get("message", "內容不得為空白！") 
        return redirect(url_for("error", message=message))
    else:
        cursor.execute("INSERT INTO member (username, password, name) VALUES (%s, %s, %s)", (reg_acct, reg_pwd, reg_name,))
        cnx.commit()
        return redirect("/")
        

# SIGN-IN
@app.route("/signin", methods=["POST"])
def signin():
    acct = request.form["user"]
    pword = request.form["p"]
    cursor.execute('SELECT * FROM member WHERE username = %s AND password = %s', (acct, pword,))
    account=cursor.fetchone()
    if account:
        session["id"]=account[0]
        session["name"]=account[1]
        session["user"]=account[3]
        session["signin"]=True
        return redirect("/member")
    elif len(acct)==0 or len(pword)==0:
        message=request.args.get("message", "請輸入帳號及密碼！") 
        return redirect(url_for("error", message=message))
    else:
        message=request.args.get("message", "帳號或密碼輸入錯誤！") 
        return redirect(url_for("error", message=message))

# SIGN-OUT
@app.route("/signout")
def signout():
    session.pop('user', None)
    session.pop('name', None)
    session.pop('id', None)
    session.pop('signin', None)
    return redirect("/")
    

# MEMBER
@app.route("/member")
def member():
    if 'user' in session:
        name=session["user"]
        cursor.execute("SELECT name, content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY member.id")
        content=cursor.fetchall()
        return render_template("member.html", name=name, content=content)
    return redirect(url_for('index'))
    

# ERROR
@app.route("/error", methods=["GET"])
def error():
    message=request.args.get("message")
    return render_template("error.html", message=message)

#MESSAGE
@app.route("/message", methods=["POST"])
def message():
    name=session["name"]
    memberId=session["id"]
    comment=request.form["msg"]
    cursor.execute("INSERT INTO message (content, member_id) VALUE (%s, %s) ", (comment,memberId))
    cnx.commit()
    return redirect(url_for("member"))

    

app.run(port=3000)

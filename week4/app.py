from email import message
from random import seed
from flask import Flask, session, request, redirect, render_template, url_for
app= Flask (__name__, static_folder="static", static_url_path="/")
app.secret_key="try it"

# INDEX
@app.route("/")
def index():
    if 'user' in session:
        return redirect("/member")
    return render_template("homepage.html")

# SIGN-IN
@app.route("/signin", methods=["POST"])
def signin():
    acct = request.form["user"]
    pword = request.form["p"]
    if acct == "test" and pword=="test":
        session["user"]=acct
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
    return redirect("/")
    

# MEMBER
@app.route("/member")
def member():
    name=session["user"]
    return render_template("member.html", data=name)

# ERROR
@app.route("/error", methods=["GET"])
def error():
    message=request.args.get("message")
    return render_template("error.html", message=message)

# OPTIONAL SQUARE


app.run(port=3000)

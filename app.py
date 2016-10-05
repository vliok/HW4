#Vincent Liok
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood.
#2016-10-4

from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("mainpage.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html",message="")

@app.route("/authL", methods=["POST"])
def authenticateL():
    print app
    print request
    print request.form
    print request.form["username"]
    print request.form["password"]
    print request.headers
    f = open("accounts.csv","r")
    username = request.form["username"]
    password = request.form["password"]
    h = hashlib.sha1()
    h.update(password)
    password = h.hexdigest()
    for line in f:
        pair = line.split(",")
        pair[1] = pair[1].rstrip("\n")
        if username == pair[0] and password == pair[1]:
            f.close()
            return render_template("success.html")
        if username == pair[0] and password != pair[1]:
            f.close()
            return render_template("login.html",message="Wrong password!")
        if username != pair[0] and password == pair[1]:
            f.close()
            return render_template("login.html",message="Wrong username!")
    f.close()
    return render_template("login.html",message="Incorrect username and password!")

@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html",message="")

@app.route("/authR", methods=["POST"])
def authenticateR():
    print app
    print request
    print request.form
    print request.form["username"]
    print request.form["password"]
    print request.headers
    f = open("accounts.csv","r")
    username = request.form["username"]
    password = request.form["password"]
    h = hashlib.sha1()
    h.update(password)
    password = h.hexdigest()
    for line in f:
        pair = line.split(",")
        pair[1] = pair[1].rstrip("\n")
        if username == pair[0]:
            f.close()
            return render_template("register.html",message="Username already taken!")
    f.close()
    f = open("accounts.csv","a")
    f.write( username + "," + password + "\n" )
    f.close()
    return render_template("login.html",message="Account created!")

if __name__ == "__main__" :
    app.debug = True
    app.run()

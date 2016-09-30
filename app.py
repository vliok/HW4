from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def authenticate():
    print app
    print request
    print request.form
    print request.form["username"]
    print request.headers
    if request.form["username"] == "meow" and request.form["password"] == "12345" :
        return render_template("success.html")
    else:
        return render_template("failure.html")

if __name__ == "__main__" :
    app.debug = True
    app.run()

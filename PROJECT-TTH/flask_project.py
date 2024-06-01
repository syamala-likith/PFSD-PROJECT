from flask import *
from pymongo import MongoClient
#creating instance
app=Flask(__name__)
client=MongoClient('mongodb://127.0.0.1:27017')
#creating database
db=client["Registration"]
data=db.details
#routing
@app.route("/")
def home():
    return render_template('home.html')
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("Registration.html")

@app.route("/aboutus")
def sample1():
    return render_template("aboutus.html")
@app.route("/contact")
def sample4():
    return render_template("contact.html")
@app.route("/form/register")
def sample3():
    return render_template("Registration.html")
@app.route("/successfull", methods=('GET','POST'))
def onsubmit():
    email=request.form.get('email')
    fn=request.form.get('fn')
    ln=request.form.get('ln')
    pword=request.form.get('pword')
    mobileno=request.form.get('mobileno')
    a={"Email":email,"FirstName":fn,"LastName":ln,"Password":pword,"MobileNo":mobileno}
    data.insert_one(a)
    return render_template('login.html')
@app.route("/loginuser",methods=["post"])
def sample2():
    entered_username = request.form.get("email")
    entered_password = request.form.get("pword")
    tofind1 = {"Email":entered_username }
    tofind2 = {"Password":entered_password}
    c = 0
    for x in tofind1:
        if (data.find_one(tofind1)):
            c = 1
    for x in tofind2:
        if (data.find_one(tofind2)):
            c = 2
    if (c == 2):
        return render_template('tourism.html')
    else:
        return "Please enter correct details!"


if __name__=="__main__":
    app.run()
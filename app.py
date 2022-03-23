from black import out
from flask import Flask, render_template,request
import Modelling
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sub",methods=['POST'])
def submit():
    if request.method=="POST":
        CreditScore= float(request.form["CreditScore"])
        MIP= float(request.form["MIP"])
        Units= float(request.form["Units"])
        OCLTV= float(request.form["OCLTV"])
        DTI= float(request.form["DTI"])
        OrigUPB= float(request.form["OrigUPB"])
        LTV= float(request.form["LTV"])
        OrigInterestRate= float(request.form["OrigInterestRate"])
        PPM= float(request.form["PPM"])
        MonthsInRepayment=float(request.form["MonthsInRepayment"])

        output=Modelling.prediction(CreditScore,MIP,Units,OCLTV,DTI,OrigUPB,LTV,OrigInterestRate,PPM,MonthsInRepayment)


    return render_template("sub.html", output=output) 


if __name__=="__main__":
    app.run(debug=True)

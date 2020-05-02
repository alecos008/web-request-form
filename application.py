from flask import Flask, render_template, request

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)

form = "form-control"
@app.route("/index.html")
def index ():
    return render_template ("index.html")

@app.route("/appoint.html")
def appoint ():
    return render_template ("appoint.html")

@app.route("/scheduled.html", methods=["POST"])
def scheduled ():
    form =  request.form.get ("form-control")
    name = request.form.get ("name")
    date = request.form.get ("date")
    email = request.form.get ("email")

  
    return render_template ("scheduled.html", name=name, date=date, email=email)
    

    
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    department = request.form["department"]

    return render_template(
        "success.html",
        name=name,
        email=email,
        department=department
    )

if __name__ == "__main__":
    app.run(debug=True)
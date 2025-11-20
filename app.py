from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "syncup_secret_key"

# Mock users
users = {"vaibhav@college.edu.in": "1234", "sainipriyanshi@college.edu.in": "0000"}

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and users[email] == password:
            session["user"] = email
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/studyhub")
def studyhub():
    return render_template("studyhub.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/skillswap")
def skillswap():
    return render_template("skillswap.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)

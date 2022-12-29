from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods = ["POST"])
def add_license_plate():
    license_plate = request.form.get("license_plate").upper()
    shelf = request.form.get("shelf").upper()
    flash(f"Registerings numret {license_plate} är nu registrerat på hylla {shelf}", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug = True, host= "0.0.0.0" )
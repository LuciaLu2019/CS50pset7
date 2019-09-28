import cs50
import csv


from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

errList = []

@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    ins = {}
    ins['fname'] = request.form.get("fname")
    ins['lname'] = request.form.get("lname")
    ins['email'] = request.form.get("email")
    ins['city'] = request.form.get("city")
    ins['state'] = request.form.get("state")
    ins['lean'] = request.form.get("lean")
    ins['party'] = request.form.get("party")

    for i in ins:
        if not ins[i]:
            errList.append(f"{i}")
            return render_template("error.html", message=errList)
    fieldnames = [i for i in ins]
    with open("survey.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        for i in [ins]:
            writer.writerow(i)
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.DictReader(file)
        participants = list(reader)
    return render_template("sheet.html", participants = participants)

from flask import Flask, redirect, url_for, render_template, request
from database import *


app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def main():
    
    revenue_list = load_database()
    revenue_list = sort_through_date(revenue_list)
    balance_info = balance_counter(revenue_list)
    return render_template("index.html", revenue_list=revenue_list, balance_info=balance_info)

@app.route("/add", methods = ["POST", "GET"])
def add():
    if request.method == "POST":
        amount = request.form["amount"]
        currency = request.form["currency"]
        name = request.form["name"]
        kind = request.form["kind"]
        description = request.form["description"]
        #category = request.form["category"]
        date = request.form["date"]
        add_to_database(name, amount, currency, kind, description, date)
        return redirect(url_for("main"))

@app.route("/delete/<num>", methods = ["POST", "GET"])
def delete(num):

    delete_from_database(num)
    return redirect(url_for("main"))


@app.route("/edit/<num>", methods = ["POST", "GET"])
def edit(num):
    if request.method == "POST":
        amount = request.form["amount"]
        currency = request.form["currency"]
        name = request.form["name"]
        kind = request.form["kind"]
        description = request.form["description"]
        #category = request.form["category"]
        date = request.form["date"]
        update_from_database(num, name, amount, currency, kind, description, date)
    
    return redirect(url_for("main"))


@app.route("/stats", methods = ["POST", "GET"])
def stats():

    revenue_list = load_database()
    revenue_list = sort_through_date(revenue_list)
    balance_info = balance_counter(revenue_list)
    chart_info = data_for_chart(revenue_list)

    dates = [object['date'] for object in chart_info]
    balance = [object['balance'] for object in chart_info]
    outcome = ['Przychody [PLN]', 'Koszty [PLN]']
    income = [balance_info['income'], balance_info['outcome']]


    return render_template("stats.html", outcome=outcome, income=income, dates = dates, balance = balance)



if __name__ == "__main__":
    app.run(debug=True)
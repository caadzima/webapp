from flask import Flask, render_template, Blueprint, g, request
import sqlite3

app = Flask(__name__)

DATABASE = 'mydb.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def template():
    with app.app_context():
        cur = get_db().cursor()
        cur = get_db().execute("Select * FROM USER", ())
        rv = cur.fetchall()
        print(rv)
    return render_template("template.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    with app.app_context():
        cur = get_db().cursor()
    if request.method=='POST':
        userEmail = request.form['userEmail']
        userPassword = request.form['userPassword']
        print(userEmail, userPassword)
        return render_template("main2.html")
    else:
        return render_template("login.html")
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")
@app.route("/main2")
def main2():
    return render_template("main2.html")
@app.route("/recipe")
def recipe():
    return render_template("recipe.html")


if __name__ == "__main__":
    app.run(debug=True)
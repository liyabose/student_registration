from flask import Flask, render_template, request, redirect
from db import connection, cursor

app = Flask(__name__)

@app.route("/")
def home():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    return render_template("index.html", students=students)


@app.route("/add")
def add_student():

    return render_template("add_student.html")


@app.route("/save", methods=["POST"])
def save_student():

    name = request.form["name"]

    age = request.form["age"]

    course = request.form["course"]

    sql = """
    INSERT INTO students(name, age, course)
    VALUES(%s,%s,%s)
    """

    values = (name, age, course)

    cursor.execute(sql, values)

    connection.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
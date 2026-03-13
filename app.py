from flask import Flask, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return """
    <h1>Student Manager</h1>
    <a href='/add'>Add Student</a><br>
    <a href='/list'>Student List</a>
    """

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        students.append(name)
        return "Student added! <a href='/'>Back</a>"

    return """
    <h2>Add Student</h2>
    <form method="post">
    Name: <input name="name">
    <input type="submit">
    </form>
    """

@app.route("/list")
def list_students():
    result = "<h2>Student List</h2>"
    for s in students:
        result += s + "<br>"
    result += "<br><a href='/'>Back</a>"
    return result

app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # jednoduchá "databáze" v paměti

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        tasks.append(title)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

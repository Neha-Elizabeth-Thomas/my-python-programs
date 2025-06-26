from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["username"]
        return render_template("form.html", name=name)
    return render_template("form.html", name=None)

if __name__ == "__main__":
    app.run(debug=True)

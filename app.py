from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "sucessfully working on aks using git action and argocd"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        return f"Thanks for contacting us, {name}!"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000, debug=True)

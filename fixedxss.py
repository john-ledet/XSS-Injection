from flask import Flask, request, render_template
from markupsafe import escape  
import bleach 

app = Flask(__name__)

comments = []

@app.route("/", methods=['GET'])
def load_home():
    return render_template("home.html")

@app.route("/stored", methods=['GET', 'POST'])
def stored_xss():
    if request.method == "POST":
        comment = request.form.get("comment")
        if comment:  
            safe_comment = bleach.clean(comment)
            comments.append(safe_comment)  
            print("Stored Comments:", comments)  

    return render_template("stored.html", comments=comments)  

@app.route("/reflected", methods=['GET', 'POST'])
def load_reflected():
    name = request.args.get("name", "Guest")
    safe_name = escape(name)
    return render_template("reflected.html", name=safe_name)

if __name__ == "__main__":
    app.run(debug=True)

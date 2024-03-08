from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #Flask will look for templates in the "templates" folder.
    #All other files like CSS and JS will be looked in "static" folder.
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

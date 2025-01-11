from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hellow_world():
  return render_template("index.html")


@app.route('/personal_website')
def personal_website():
  return render_template("Personal_Site.html")


if __name__ == ('__main__'):
  app.run(debug=True)
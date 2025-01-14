from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hellow_world():
  return 'Home page'


@app.route('/personal_website')
def personal_website():
  return render_template("index.html")


if __name__ == ('__main__'):
  app.run(debug=True)
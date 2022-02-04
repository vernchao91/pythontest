from flask import (Flask, render_template)
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])

@app.route('/')
def index():
  return render_template("index.html", var="Python test")
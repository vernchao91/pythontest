from app import app

@app.route('/')
def index():
  return render_template("index.html", var="Python test")
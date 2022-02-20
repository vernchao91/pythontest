from app import app

@app.route('/')
def index():
  return render_template("index.html", var="Python test")

@app.route('/help')
def help():
  return "<h1>help</h1>"

@app.route('/item/<id>')
def item(id):
  

from flask import Blueprint, render_template, redirect

@bp.route('/')
def index():
  return render_template("index.html", title="Welcome Python Tester")

@bp.route('/help')
def help():
  return "<h1>help</h1>"
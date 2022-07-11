from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)
@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@my_view.route('/aboutmusic')
def aboutmusic():
    return render_template("aboutmusic.html")

@my_view.route('/fuser')
def fuser():
    return render_template("fuser.html")

@my_view.route('/aboutmusicproduction')
def aboutmusicproduction():
    return render_template("aboutmusicproduction.html")

@my_view.route('/aboutdj')
def aboutdj():
    return render_template("aboutdj.html")


@my_view.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@my_view.route('/javascript')
@my_view.route('/js')
@my_view.route('/home')
def index_redirect():
    return redirect(url_for("my_view.index"))

from flask import Flask, render_template, Blueprint, redirect, url_for, request

#template routes for all pages below from index. 
my_view = Blueprint('my_view', __name__)
@my_view.route("/")
def index():
    return render_template("index.html")

#about me page route.
@my_view.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

#about music page route.
@my_view.route('/aboutmusic')
def aboutmusic():
    return render_template("aboutmusic.html")

#about fuser page route. 
@my_view.route('/fuser')
def fuser():
    return render_template("fuser.html")

#about music production page route. 
@my_view.route('/aboutmusicproduction')
def aboutmusicproduction():
    return render_template("aboutmusicproduction.html")

#about DJ'in page route
@my_view.route('/aboutdj')
def aboutdj():
    return render_template("aboutdj.html")

#admin page route
@my_view.route('/admin')
def admin():
    return render_template("admin.html")

#404 custom error handling page
@my_view.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# Route for handling the admin login page
@my_view.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            return render_template('405.html' ,error=error)
        else:
            return redirect(url_for('my_view.index'))
    return render_template('admin.html', error=error) 



#Re-routing using java scripts.
@my_view.route('/javascript')
@my_view.route('/js')
@my_view.route('/home')
def index_redirect():
    return redirect(url_for("my_view.index"))
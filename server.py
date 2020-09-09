"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/movies')
def view_movies():
    movie_list = crud.all_movies()
    return render_template("all_movies.html", movie_list=movie_list)

@app.route('/movies/<movie_id>')
def movie_detail(movie_id):
    
    movie_info = crud.get_movie_by_id(movie_id)
    
    return render_template("movie_details.html",movie_info=movie_info)

@app.route('/users')
def view_users():
    user_list = crud.all_users()
    return render_template("all_users.html", user_list=user_list)

@app.route('/users/<user_id>')
def user_profile(user_id):

    user_info = crud.get_user_by_id(user_id)

    return render_template("user_profile.html",user_info=user_info)

@app.route('/users', methods=['POST'])
def register_user():

    user_email = request.form.get('email')
    user_password = request.form.get('password')

    user = crud.get_user_by_email(user_email)

    if user:
        flash("You can't create an account with that email")
    else:
        crud.create_user(user_email, user_password)
        flash("Successfully created account!")
    return redirect('/')

@app.route('/', methods=['POST'])
def login_user():

    login_email = request.form.get('login_email')
    login_password = request.form.get('login_password')

    user = crud.get_user_by_email(login_email)
    print(user)
    if user:
        if user.password != login_password:
            flash("Incorrect password")
            return redirect('/')
        else:   
            session['login_email'] = login_email
            flash("Logged in")
            return redirect('/')
    else:
        flash("Not a valid account")
        return redirect('/users')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
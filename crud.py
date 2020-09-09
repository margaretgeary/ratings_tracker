"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db, datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def all_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def all_movies():

    return Movie.query.all()

def get_movie_by_id(movie_id):

    return Movie.query.get(movie_id)

def create_rating(score, user, movie):
    """Create and return a new movie."""

    rating = Rating(score=score, user = user, movie = movie)

    db.session.add(rating)
    db.session.commit()

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
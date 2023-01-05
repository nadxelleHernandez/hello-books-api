from flask import Blueprint, jsonify, make_response, request,abort
from app import db
from app.models.author import Author
from app.models.book import Book
from app.models.genre import Genre
from app.routes.book_routes import validate_model

genre_bp = Blueprint("genres", __name__, url_prefix="/genres")

@genre_bp.route("",methods=["POST"])
def create_genre():
    request_body = request.get_json()
    new_genre = Genre.from_dict(request_body)

    db.session.add(new_genre)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_genre.name} successfully created"), 201)

@genre_bp.route("",methods=["GET"])
def get_all_genres():
    genres = Genre.query.all()

    genres_response = [genre.to_dict() for genre in genres]

    return jsonify(genres_response)

@genre_bp.route("<genre_id>/books",methods=["POST"])
def create_book_with_genre(genre_id):
    request_body = request.get_json()
    genre = validate_model(Genre,genre_id)
    new_book = Book.from_dict(request_body)
    new_book.author_id = request_body["author_id"]
    new_book.genres = [genre]

    db.session.add(new_book)
    db.session.commit()

    msg = f"Book {new_book.title} by {new_book.author.name} successfully created"
    return make_response(jsonify(msg),201)

@genre_bp.route("<genre_id>/books",methods=["GET"])
def get_books_by_genre(genre_id):
    genre = validate_model(Genre,genre_id)

    books_response = [book.to_dict() for book in genre.books]

    return jsonify(books_response)


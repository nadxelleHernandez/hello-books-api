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
    new_genre = Genre(name=request_body["name"])

    db.session.add(new_genre)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_genre.name} successfully created"), 201)

@genre_bp.route("",methods=["GET"])
def get_all_genres():
    genres = Genre.query.all()

    genres_response = [genre.to_dict() for genre in genres]

    return jsonify(genres_response)

    
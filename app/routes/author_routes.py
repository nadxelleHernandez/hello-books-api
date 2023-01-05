from flask import Blueprint, jsonify, make_response, request,abort
from app import db
from app.models.author import Author
from app.models.book import Book
from app.routes.book_routes import validate_model

author_bp = Blueprint("authors", __name__, url_prefix="/authors")

@author_bp.route("",methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author(name=request_body["name"],)

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created"), 201)

@author_bp.route("",methods=["GET"])
def get_all_authors():
    authors = Author.query.all()

    authors_response = [author.to_dict() for author in authors]

    return jsonify(authors_response)

@author_bp.route("/<author_id>/books", methods=["POST"])
def create_book_by_author(author_id):
    author = validate_model(Author,author_id)
 
    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author=author
    )

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)

@author_bp.route("/<author_id>/books", methods=["GET"])
def get_books_by_author(author_id):
    author = validate_model(Author,author_id)
 
    books = author.books

    books_response = [book.to_dict() for book in books]

    return jsonify(books_response)
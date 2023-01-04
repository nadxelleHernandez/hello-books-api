from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request,abort

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def get_all_books():
    books_response = []
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    for book in books:
        books_response.append(book.to_dict())
        
    return jsonify(books_response)

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)


def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response(jsonify({"message":f"book {book_id} invalid"}), 400))

    book = Book.query.get(book_id)

    if not book:
        abort(make_response(jsonify({"message":f"book {book_id} not found"}), 404))

    return book

@books_bp.route("/<book_id>", methods=["GET"])
def get_book(book_id):
    book = validate_book(book_id)

    return jsonify(book.to_dict())

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully updated"))

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"))
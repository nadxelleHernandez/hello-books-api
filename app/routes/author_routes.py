from flask import Blueprint, jsonify, make_response, request,abort
from app import db
from app.models.author import Author

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

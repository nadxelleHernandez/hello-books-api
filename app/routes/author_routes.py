from flask import Blueprint, jsonify, make_response, request,abort
from app import db
from app.models.author import Author

author_bp = Blueprint("authors", __name__, url_prefix="/authors")

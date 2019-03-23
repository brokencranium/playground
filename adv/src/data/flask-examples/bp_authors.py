
import flask
from flask import Blueprint, jsonify, request, abort

from .util import state, url_for, get_author_or_404, jsonify_author, verify_password

mod = Blueprint('authors', __name__)

@mod.route('<author_id>')
def get_author(author_id):
    author = get_author_or_404(author_id)
    return jsonify_author(author_id, author)

@mod.route('<author_id>', methods=['PUT'])
def update_author(author_id):
    verify_password()
    author = get_author_or_404(author_id)
    author.update({
        **request.json,
    })
    return jsonify_author(author_id, author)

from flask import Flask, render_template, request, redirect, url_for
from repositories import author_repository
from repositories import book_repository
from models.book import Book


from flask import Blueprint
books_blueprint = Blueprint("books", __name__)

#INDEX
#VIEW ALL BOOKS
@books_blueprint.route('/books')
def books():
    # Get all tasks from the db
    books = book_repository.select_all()
    return render_template('books/index.html', all_books=books)
# NEW
# GET '/books/new'

@books_blueprint.route('/books/new_book')
def new_book():
    return render_template('/books/new.html')

# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'


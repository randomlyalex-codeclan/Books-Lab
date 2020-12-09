from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository



def save(book):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [book.first_name, book.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        book = Book(row['first_name'], row['last_name'], row['id'] )
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        book = Book(result['first_name'], result['last_name'], result['id'] )
    return book


def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(book):
    sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [book.first_name, book.last_name, book.id]
    run_sql(sql, values)

def books(author):
    books = []

    sql = "SELECT * FROM books WHERE user_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['genre'], row['publish'], author, row['id'] )
        books.append(book)
    return books

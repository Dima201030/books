from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/books/<book_id>')
def download_book(book_id):
    # Здесь вы можете выполнить логику для поиска книги по идентификатору
    # и вернуть путь к файлу для загрузки
    book_path = f'path/to/books/{book_id}.pdf'  # Замените на путь к вашим книгам

    if os.path.isfile(book_path):
        return send_from_directory(os.path.dirname(book_path), os.path.basename(book_path), as_attachment=True)
    else:
        return 'Книга не найдена', 404

if __name__ == '__main__':
    app.run()
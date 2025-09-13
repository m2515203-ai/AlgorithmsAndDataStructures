import json


def find_books_by_author(author_name, filename='array.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            books = json.load(file)

        found_books = [
            book for book in books
            if author_name.lower() in book['автор'].lower()
        ]

        return found_books

author_to_search = "Толстой"
found_books = find_books_by_author(author_to_search)

print(f"Книги автора '{author_to_search}':")
for book in found_books:
    print(f"- {book['название']} ({book['год']})")
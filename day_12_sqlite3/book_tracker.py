import sqlite3

# DB Creation Logic
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS books (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title TEXT NOT NULL,
		author TEXT NOT NULL,
		price REAL,
		published_year INTEGER
	)
""")
conn.commit()

def add_book(title, author, price, year):
	cursor.execute("""
		INSERT INTO books (title, author, price,
			published_year) VALUES (?, ?, ?, ?)
	""",
	(title, author, price, year)
	)
	conn.commit()
	print("Book Added Sucessfully")

def view_books():
	cursor.execute("""
		SELECT * FROM books;
	""")
	books = cursor.fetchall()

	if not books:
		print("No Books Found")
		return

	print("Books List")
	for book in books:
		print(f"id: {book[0]}, titel: {book[1]}")

def update_book_price(book_id, new_price):
	query = f"UPDATE books SET price = {new_price} WHERE id = {book_id}"
	cursor.execute(query)
	conn.commit()

	if cursor.rowcount == 0:
		print("Book Id not found")
	else:
		print("Book details update fine")

# """ - Multi Line String

"""
Hi How Are You ?
"""
def delete_book(book_id):
	cursor.execute("""
		DELETE FROM books WHERE id = ?
	""", (book_id,))
	conn.commit()

	if cursor.rowcount == 0:
		print("Book Id not found")
	else:
		print("Book details deleted")

def show_menu():
	print("Book Tracker Menu")
	print("1. Add Book")
	print("2. View All Book")
	print("3. Update book price")
	print("4. Delete Book")
	print("5. Exit")

while True:
	show_menu()
	choice = input("Enter your choice : ")

	if choice == "1":
		title = input("Enter book title : ")
		author = input("Enter author name : ")
		price = float(input("Enter book price : "))
		year = int(input("Enter year of publish : "))

		add_book(title, author, price, year)

	elif choice == "2":
		view_books()

	elif choice == "3":
		book_id = input("Enter book id : ")
		new_price = float(input("Enter new book price : "))
		update_book_price(book_id, new_price)

	elif choice == "4":
		book_id = int(input("Enter book id : "))
		delete_book(book_id)

	elif choice == "5":
		print("[+] Exiting book tracker")
		break

	else:
		print("Invalid Choice. Please select 1-5")

conn.close()
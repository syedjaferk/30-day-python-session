import sqlite3

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

# Sample Insert
# cursor.execute("""
# 	INSERT INTO books (title, author, price,
# 		published_year) VALUES ('Deepa', 'Social Science',
# 		150.50, 2024)
# """)

# conn.commit()

# Sample Select

cursor.execute("""
	SELECT * FROM books;
""")
books = cursor.fetchall()
for book in books:
	print(book)

# Sample Update

cursor.execute("""
	UPDATE books SET price = 105.50 WHERE id = 1
""")

conn.commit()


# Sample Delete

cursor.execute("""
	DELETE FROM books WHERE id = 1
""")
conn.commit()

conn.close()
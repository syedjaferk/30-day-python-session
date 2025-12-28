import argparse
import sqlite3
import logging

DB_FILE = "todos.db"
LOG_FILE = "todos.log"

logging.basicConfig(
	filename=LOG_FILE,
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_connection():
	# SQL Connection
	return sqlite3.connect(DB_FILE)

def init_db():
	with get_connection() as conn:
		conn.execute("""
			CREATE TABLE IF NOT EXISTS todolist (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				description TEXT NOT NULL,
				completed INTEGER DEFAULT 0,
				created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			)
		""")
		conn.commit()

def add_task(description):
	with get_connection() as conn:
		conn.execute(
			"""
			INSERT INTO todolist (description) VALUES (?)
			""",
			(description,)
		)
		logging.info(f"[+] Task added : {description}")

def list_tasks(completed=False):
	if completed:
		query = "SELECT id, description, completed FROM todolist WHERE completed = 1"
	else:
		query = "SELECT id, description, completed FROM todolist WHERE completed = 0"

	with get_connection() as conn:
		tasks = conn.execute(query).fetchall()

	if not tasks:
		print("No Tasks Found")

	for task in tasks:
		print(task)

def mark_as_complete(task_id):
	with get_connection() as conn:
		cursor = conn.execute("""
			UPDATE todolist SET completed = 1 WHERE id = ?
			""",
			(task_id, )
		)

	if cursor.rowcount == 0:
		print("Task not found to update")
		return

	logging.info(f"Task id {task_id} marked as done ")

def main():
	init_db()
	parser = argparse.ArgumentParser(description="CLI TODO App")

	subparsers = parser.add_subparsers(dest="command")

	add_parser = subparsers.add_parser("add", help="To add a new task")
	add_parser.add_argument("description", help="Task description")

	list_parser = subparsers.add_parser("list", help="List tasks")
	list_parser.add_argument("--completed", action="store_true", help="Show completed tasks only")
	list_parser.add_argument("--pending", action="store_true", help="Show pending tasks only")

	completed_parser = subparsers.add_parser("complete", help="Mark as completed")
	completed_parser.add_argument("id", type=int, help="Task id to be completed")


	args = parser.parse_args()

	if args.command == "add":
		add_task(description=args.description)
	elif args.command == "list":
		if args.completed:
			list_tasks(completed=True)
		else:
			list_tasks(completed=False) # Pending
	elif args.command == "complete":
		mark_as_complete(task_id=args.id)

	else:
		parser.print_help()

main()
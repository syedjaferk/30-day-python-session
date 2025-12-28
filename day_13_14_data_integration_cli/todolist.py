import argparse
import sqlite3
import sys
import logging
from pathlib import Path

# ---------------- CONFIG ----------------
DB_FILE = "todo.db"
LOG_FILE = "todo.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- DATABASE ----------------
def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# ---------------- COMMANDS ----------------
def add_task(title):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )
        conn.commit()
    logging.info(f"Task added: {title}")
    print("✅ Task added")

def list_tasks(show_completed=None):
    query = "SELECT id, title, completed FROM tasks"
    params = ()

    if show_completed is True:
        query += " WHERE completed = 1"
    elif show_completed is False:
        query += " WHERE completed = 0"

    with get_connection() as conn:
        tasks = conn.execute(query, params).fetchall()

    if not tasks:
        print("📭 No tasks found")
        return

    for task in tasks:
        status = "✔" if task[2] else "✗"
        print(f"{task[0]}. [{status}] {task[1]}")

def mark_done(task_id):
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )
        conn.commit()

    if cursor.rowcount == 0:
        print("❌ Task not found")
        sys.exit(1)

    logging.info(f"Task completed: ID {task_id}")
    print("✔ Task marked as completed")

def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()

    if cursor.rowcount == 0:
        print("❌ Task not found")
        sys.exit(1)

    logging.info(f"Task deleted: ID {task_id}")
    print("🗑 Task deleted")

# ---------------- CLI ----------------
def main():
    init_db()

    parser = argparse.ArgumentParser(
        description="📝 Command Line To-Do Application"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")

    # List
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--completed",
        action="store_true",
        help="Show completed tasks only"
    )
    list_parser.add_argument(
        "--pending",
        action="store_true",
        help="Show pending tasks only"
    )

    # Done
    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)

    elif args.command == "list":
        if args.completed:
            list_tasks(show_completed=True)
        elif args.pending:
            list_tasks(show_completed=False)
        else:
            list_tasks()

    elif args.command == "done":
        mark_done(args.id)

    elif args.command == "delete":
        delete_task(args.id)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

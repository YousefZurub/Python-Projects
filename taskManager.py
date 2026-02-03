import sqlite3
from os import system


DB_NAME = "tasks.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    done INTEGER
)
""")
conn.commit()


OP_ADD_TASK = '1'
OP_MARK_DONE = '2'
OP_SHOW_UNDONE = '3'
OP_EXIT = '0'


option = ""

while option != OP_EXIT:
    system("clear")  

    print("\n--- TASK MANAGER ---")
    print(OP_ADD_TASK + ". Add task")
    print(OP_MARK_DONE + ". Mark task as done")
    print(OP_SHOW_UNDONE + ". Show unfinished tasks")
    print(OP_EXIT + ". Exit")

    option = input("Choose option: ")

    
    if option == OP_ADD_TASK:
        title = input("Task title: ")

        if title != "":
            cursor.execute(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                (title, 0)
            )
            conn.commit()
            print("Task added.")
        else:
            print("Task title cannot be empty.")

    
    if option == OP_MARK_DONE:
        try:
            task_id = int(input("Task ID to mark as done: "))
            cursor.execute(
                "UPDATE tasks SET done = 1 WHERE id = ?",
                (task_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                print("Task not found.")
            else:
                print("Task marked as done.")
        except:
            print("Invalid ID.")

    
    if option == OP_SHOW_UNDONE:
        cursor.execute(
            "SELECT id, title FROM tasks WHERE done = 0"
        )
        tasks = cursor.fetchall()

        if len(tasks) == 0:
            print("No unfinished tasks.")
        else:
            for task in tasks:
                print(str(task[0]) + ". " + task[1])

    
    if option != OP_EXIT:
        input("Press Enter to return to menu")


conn.close()

import json
import os
from datetime import datetime

# ── File where tasks are saved ─────────────────────────────────────────────────
SAVE_FILE = "tasks.json"

# ── Load tasks from file ───────────────────────────────────────────────────────
def load_tasks():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []

# ── Save tasks to file ─────────────────────────────────────────────────────────
def save_tasks(tasks):
    with open(SAVE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# ── Display all tasks ──────────────────────────────────────────────────────────
def show_tasks(tasks, filter_done=None):
    print()
    if not tasks:
        print("  📭 No tasks yet. Add one!")
        return

    shown = 0
    for i, task in enumerate(tasks, 1):
        if filter_done is not None and task["done"] != filter_done:
            continue
        status = "✅" if task["done"] else "⬜"
        date   = task.get("created", "")
        print(f"  {i:>2}. {status} {task['title']:<35} {date}")
        shown += 1

    if shown == 0:
        print("  (no tasks match this filter)")
    print()

# ── Add a task ─────────────────────────────────────────────────────────────────
def add_task(tasks):
    title = input("  Task title: ").strip()
    if not title:
        print("  ⚠️  Task title cannot be empty.")
        return
    tasks.append({
        "title":   title,
        "done":    False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_tasks(tasks)
    print(f"  ✅ Added: '{title}'")

# ── Mark a task as done ────────────────────────────────────────────────────────
def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to mark as done: ").strip())
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"  ✅ '{tasks[num-1]['title']}' marked as done!")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

# ── Delete a task ──────────────────────────────────────────────────────────────
def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to delete: ").strip())
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  🗑️  Deleted: '{removed['title']}'")
        else:
            print("  ⚠️  Invalid number.")
    except ValueError:
        print("  ⚠️  Please enter a valid number.")

# ── Clear all completed tasks ──────────────────────────────────────────────────
def clear_done(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    removed = before - len(tasks)
    print(f"  🧹 Cleared {removed} completed task(s).")

# ── Menu ───────────────────────────────────────────────────────────────────────
def print_menu():
    print("\n" + "=" * 40)
    print("  📝  To-Do List")
    print("=" * 40)
    print("  1. View all tasks")
    print("  2. View pending tasks")
    print("  3. Add a task")
    print("  4. Mark task as done")
    print("  5. Delete a task")
    print("  6. Clear completed tasks")
    print("  7. Quit")
    print("=" * 40)

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    tasks = load_tasks()
    print("\n📋 Welcome to your To-Do List! Your tasks are saved automatically.")

    while True:
        print_menu()
        choice = input("  Choose an option (1-7): ").strip()

        if   choice == "1": show_tasks(tasks)
        elif choice == "2": show_tasks(tasks, filter_done=False)
        elif choice == "3": add_task(tasks)
        elif choice == "4": complete_task(tasks)
        elif choice == "5": delete_task(tasks)
        elif choice == "6": clear_done(tasks)
        elif choice == "7":
            print("\n  👋 Goodbye! Your tasks have been saved.\n")
            break
        else:
            print("  ⚠️  Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()

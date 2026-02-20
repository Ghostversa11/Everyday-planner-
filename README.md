# 📝 To-Do List App (Python)

A simple terminal-based to-do list app that saves your tasks automatically to a file — so nothing gets lost when you close the program.

## About

Keeping track of tasks doesn't have to be complicated. This app gives you a clean, menu-driven interface right in your terminal. Add tasks, check them off when done, delete ones you no longer need, and clear out completed tasks to keep your list tidy. Everything is saved automatically to a local `tasks.json` file so your list is always there when you come back.

## Features

- Add tasks with a title and automatic timestamp
- Mark tasks as done with a simple checkmark
- Delete individual tasks
- Clear all completed tasks at once
- Filter view to show only pending tasks
- Tasks are saved automatically to `tasks.json` after every change
- No external libraries needed — uses Python's built-in `json` and `os` modules

## How It Works

Tasks are stored as a list of objects in a local JSON file. Each task has a title, a done/not-done status, and the date and time it was created. Every time you make a change (add, complete, delete), the file is updated immediately so you never lose your data even if the program closes unexpectedly.

## Requirements

- Python 3.7+
- No extra libraries needed

## Check Python Version

Make sure you have Python 3.7 or higher before running:

```bash
python --version
```

## Installation & Usage

Download the file and run it:

```bash
python todo_app.py
```

You'll see a simple menu:

```bash
========================================
  📝  To-Do List
========================================
  1. View all tasks
  2. View pending tasks
  3. Add a task
  4. Mark task as done
  5. Delete a task
  6. Clear completed tasks
  7. Quit
========================================
  Choose an option (1-7):
```

Example of adding a task:

```bash
Choose an option (1-7): 3
  Task title: Buy groceries
  ✅ Added: 'Buy groceries'
```

Example task list view:

```bash
   1. ⬜ Buy groceries                       2024-06-01 09:15
   2. ✅ Call the bank                        2024-06-01 10:30
   3. ⬜ Finish Python project               2024-06-01 11:00
```




## View Your Saved Tasks File

Your tasks are stored in `tasks.json` in the same folder. You can inspect it anytime:

```bash


type tasks.json
```

## Reset / Clear All Tasks

To start fresh, simply delete the tasks file:

```bash

del tasks.json
```

## File Storage

Your tasks are saved in a file called `tasks.json` in the same folder as the script. You can back it up, copy it to another machine, or open it in any text editor to view your tasks.


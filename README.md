# Task Tracker CLI

A simple command-line task tracker built with Python. The application allows users to create, update, delete, and manage tasks directly from the terminal, with data persisted in a local JSON file.

This project was developed as part of the [Task Tracker project](https://roadmap.sh/projects/task-tracker) from [roadmap.sh](https://roadmap.sh/).

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as in progress
* Mark tasks as completed
* List all tasks
* Filter tasks by status
* Persist tasks using a JSON file
* Validate command-line arguments and task IDs

## Requirements

* Python 3.10+
* No external dependencies

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/task-tracker.git
```

Navigate to the project directory:

```bash
cd task-tracker
```

## Usage

Run the application using Python:

```bash
python3 task-cli.py <command>
```

### Add a task

```bash
python3 task-cli.py add "Study Python"
```

### Update a task

```bash
python3 task-cli.py update 1 "Study Python functions"
```

### Delete a task

```bash
python3 task-cli.py delete 1
```

### Mark a task as in progress

```bash
python3 task-cli.py mark-in-progress 1
```

### Mark a task as completed

```bash
python3 task-cli.py mark-done 1
```

### List all tasks

```bash
python3 task-cli.py list
```

### List tasks by status

```bash
python3 task-cli.py list todo
```

```bash
python3 task-cli.py list in-progress
```

```bash
python3 task-cli.py list done
```

## Task Structure

Each task is stored as an object in `tasks.json`:

```json
{
  "id": 1,
  "description": "Study Python",
  "status": "todo"
}
```

Tasks use three possible statuses:

* `todo`
* `in-progress`
* `done`

## Project Structure

```text
task-tracker/
├── task-cli.py
├── tasks.json
└── README.md
```

## What I Practiced

This project was built to practice fundamental Python and software development concepts, including:

* Command-line arguments with `sys.argv`
* Functions and program organization
* Conditional logic
* Lists and dictionaries
* JSON file handling
* Reading and writing files
* Input validation
* Error handling
* Working with file paths
* Basic data persistence
* Structuring a CLI application

## Challenges

One of the main challenges was handling invalid or incomplete command-line arguments without causing the application to crash.

The project also required careful handling of the JSON file, including loading existing tasks, updating data, and keeping the application working when executed from different directories.

## Future Improvements

Possible improvements for future versions include:

* Refactoring the CLI argument handling
* Improving the project's internal data structures
* Adding automated tests
* Separating the application into multiple modules
* Improving error messages
* Adding more robust input validation

## Project

This project is based on the roadmap.sh challenge:

[Task Tracker](https://roadmap.sh/projects/task-tracker)

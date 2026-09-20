# Expense Tracker CLI

A command-line expense tracker built with Python. The application allows users to manage their expenses, view spending summaries, and filter expenses by month.

This project was developed as part of the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## Features

* Add expenses with a description and amount
* Update existing expenses
* Delete expenses
* List all expenses
* View a summary of total expenses
* View a summary for a specific month
* Persist expense data locally using JSON
* Validate command-line arguments and expense IDs
* Handle invalid inputs and edge cases

## Requirements

* Python 3.10+
* No external dependencies

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/expense-tracker.git
```

Navigate to the project directory:

```bash
cd expense-tracker
```

## Usage

The application runs through the command line using Python.

### Add an expense

```bash
python3 expense-tracker.py add --description "Lunch" --amount 20
```

Example output:

```text
Expense added successfully (ID: 1)
```

### Update an expense

```bash
python3 expense-tracker.py update --id 1 --description "Lunch at restaurant" --amount 25
```

### Delete an expense

```bash
python3 expense-tracker.py delete --id 1
```

Example output:

```text
Expense deleted successfully
```

### List expenses

```bash
python3 expense-tracker.py list
```

Example output:

```text
ID  Date        Description          Amount
1   2026-09-20  Lunch                $20
2   2026-09-20  Transportation       $10
```

### View expense summary

```bash
python3 expense-tracker.py summary
```

Example output:

```text
Total expenses: $30
```

### View monthly summary

To view expenses for a specific month of the current year:

```bash
python3 expense-tracker.py summary --month 9
```

Example output:

```text
Total expenses for September: $30
```

## Data Storage

Expenses are stored locally in a JSON file.

Each expense contains information such as its ID, date, description, and amount.

Example:

```json
[
    {
        "id": 1,
        "date": "2026-09-20",
        "description": "Lunch",
        "amount": 20
    }
]
```

## Project Structure

```text
expense-tracker/
├── expense-tracker.py
├── expenses.json
└── README.md
```

## What I Practiced

This project was built to practice fundamental Python and CLI development concepts, including:

* Command-line argument parsing
* Functions and program organization
* Lists and dictionaries
* JSON data handling
* File reading and writing
* Date and time handling
* Filtering and aggregating data
* Input validation
* Error handling
* Working with the filesystem
* Building a command-line interface

## Challenges

One of the main challenges was designing the logic for managing expense data while keeping the CLI commands organized and predictable.

The project also involved handling invalid inputs, validating expense IDs, working with dates, and calculating summaries based on the stored data.

## Future Improvements

Possible improvements for future versions include:

* Adding expense categories
* Filtering expenses by category
* Adding monthly budgets
* Displaying budget warnings
* Exporting expenses to CSV
* Adding automated tests
* Separating the application into multiple modules
* Improving the CLI interface

## Project

This project is based on the roadmap.sh challenge:

[Expense Tracker](https://roadmap.sh/projects/expense-tracker)

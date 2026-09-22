import argparse
import sys
import json
import os
import datetime
from tabulate import tabulate

EXPENSES_FILE = 'expenses.json'

def build_parser() -> argparse.ArgumentParser:
    """Build and configure the argument parser for the Expense Tracker CLI,
    registering the add, update, list, delete and summary subcommands."""
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # 'add' subcommand
    add_parser = subparsers.add_parser('add', help="Add an expense")
    add_parser.add_argument('--description', type=str, required=True)
    add_parser.add_argument('--amount', type=float, required=True)

    # 'update' subcommand
    update_parser = subparsers.add_parser('update', help="Update an existing expense")
    update_parser.add_argument('--id', type=int, required=True)
    update_parser.add_argument('--description', type=str, required=False)
    update_parser.add_argument('--amount', type=float, required=False)
    
    # 'delete' subcommand
    delete_parser = subparsers.add_parser('delete', help="Remove an expense")
    delete_parser.add_argument('--id', type=int, required=True)

    # 'list' subcommand
    subparsers.add_parser('list', help="List expenses")

    # 'summary' subcommand
    summary_parser = subparsers.add_parser('summary', help="Show expense summary")
    summary_parser.add_argument('--month', type=int, default=None)

    return parser


def route_commands(parser, args):
    """Route to the matching handler based on the command provided;
    fall back to the help message if the command is missing or invalid."""
    try:
        if args.command == 'add':
            add_expense(args.description, args.amount)
        elif args.command == 'update':
            update_expense(args.id, args.description, args.amount)
        elif args.command == 'delete':
            pass
        elif args.command == 'list':
            list_expense()
        elif args.command == 'summary':
            pass
        else:
            parser.print_help()
    except ValueError as e:
        print(f"Error: {e}")


def amount_validate(amount):
    """Skip validation if no amount was provided (relevant for update, 
    where it's optional)"""
    if amount is None:
        return

    # Ensure the amount is a positive number
    if amount < 0:
        raise ValueError("A non-negative value is required")


def load_expenses(path, default=None):
    """Read a JSON file and return its contents as a Python object (usually a dict).
    If the file doesn't exist yet, return a default value instead of crashing."""
    # Check if the file exists before trying open it
    if default is None:
        default = []

    if not os.path.exists(path):
        return default

    # Open the file in read mode ("r") with utf-8 encoding
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return default
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            print(f"Warning: {path} is corrupted or invalid. Starting fresh.", file=sys.stderr)
            return default


def save_expenses(path, data):
    """Write a Python object (usually a dic) to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def next_id(expenses):
    if not expenses:
        return 1
    return max(item['id'] for item in expenses) + 1


def add_expense(description, amount):
    amount_validate(amount)
    expenses = load_expenses(EXPENSES_FILE, default=[])

    # Get the next available Expense ID
    new_id = next_id(expenses)

    # Add the new expense to the data dictionary
    expenses.append({   
        'id': new_id,
        'created_at': datetime.date.today().isoformat(),
        'description': description,
        'amount': amount,
    })

    # Call the functon to write the updated expense to the JSON file
    save_expenses(EXPENSES_FILE, expenses)

    print(f"Expense added successfully (ID: {new_id})")


def update_expense(expense_id, description, amount):
    """Update the description and/or amount of an existing expense.
    Only the fields explicitly provided (not None) are overwritten,
    leaving the rest of the expense unchanged."""
    amount_validate(amount)
    expenses = load_expenses(EXPENSES_FILE, default=[])

    # Search for the expense matching the given id
    for expense in expenses:
        # Only overwrite fields that were actually provided
        if expense['id'] == expense_id:
            if description is not None:
                expense['description'] = description
            if amount is not None:
                expense['amount'] = amount
            
            # Persist changes and confirm to the user
            save_expenses(EXPENSES_FILE, expenses)
            print(f"Expense (ID: {expense_id}) updated successfully")
            break
    else:
        # This runs only if the loop completed without hitting 'break'
        print(f"Expense (ID: {expense_id}) not found", file=sys.stderr) 


def list_expense():
    """Load all expenses and print them as a formatted table,
    with one row per expense and columns for id, date,
    description and amount."""
    expenses = load_expenses(EXPENSES_FILE, default=[])
    
    # Avoid printing an empty/awkward table when there's nothing to show
    if not expenses:
       print("No expenses found.")
       return

    # Render the list of expense dicts as a grid-style table,
    # mapping each dict key to a human-readable column header
    print(
        tabulate(
            expenses,
            headers={
                "id": "ID",
                "created_at": "Date",
                "description": "Description",
                "amount": "Amount",
            },
            tablefmt="grid"
        )
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    route_commands(parser, args)


if __name__ == "__main__":
    main()

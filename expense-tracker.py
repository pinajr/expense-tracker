import argparse
import sys
import json
import os
import datetime

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
            add_expensive(args.description, args.amount)
        elif args.command == 'update':
            pass
        elif args.command == 'delete':
            pass
        elif args.command == 'list':
            pass
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
    if not os.path.exists(path):
        return default if default is not None else {}

    # Open the file in read mode ("r") with utf-8 encoding
    with open(path, "r", encoding="utf-8") as f:
        # json.load() converts the JSON text into a Python object (dict/list)
        return json.load(f)


def save_expanses(path, data):
    """Write a Python object (usually a dic) to a JSON file."""
    # Open the file in write mode ("w") — this creates the file if it
    # doesn't exist, or overwrites it if it does
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False, sort_keys=True)
    

def add_expensive(description, amount):
    amount_validate(amount)
    data = load_expenses('expense.json')

    # Get the next available Expense ID
    id = max(data.keys(), default=0) + 1

    # Add the new expense to the data dictionary
    data.update(
        {
            id: {
                'CreatedAt': datetime.date.today().isoformat(),
                'description': description,
                'amount': amount,
            }
        }
    )

    # Call the functon to write the updated expense to the JSON file
    save_expanses('expense.json', data)

    print(f"Expense added successfully (ID: {id})")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    route_commands(parser, args)


if __name__ == "__main__":
    main()

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
            print(f"Warning: {path} is corrupted or invalid. Startint fresh.", file=sys.stderr)
            return default


def save_expanses(path, data):
    """Write a Python object (usually a dic) to a JSON file."""
    # Open the file in write mode ("w") — this creates the file if it
    # doesn't exist, or overwrites it if it does
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def next_id(expenses):
    if not expenses:
        return 1
    return max(item['id'] for item in expenses) + 1


def add_expensive(description, amount):
    amount_validate(amount)
    expenses = load_expenses('expense.json', default=[])

    # Get the next available Expense ID
    new_id = next_id(expenses)

    # Add the new expense to the data dictionary
    expenses.append({   
        'id': new_id,
        'CreatedAt': datetime.date.today().isoformat(),
        'description': description,
        'amount': amount,
    })

    # Call the functon to write the updated expense to the JSON file
    save_expanses('expense.json', expenses)

    print(f"Expense added successfully (ID: {new_id})")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    route_commands(parser, args)


if __name__ == "__main__":
    main()

import argparse
import sys
import json
import time

def build_parser() -> argparse.ArgumentParser:
    # Set up the parser and all subcommands.
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # 'add' subcommand
    add_parser = subparsers.add_parser('add', help="Add an expense")
    add_parser.add_argument('--description', nargs=1, type=str, required=True)
    add_parser.add_argument('--amount', nargs=1, type=float, required=True)

    # 'update' subcommand
    update_parser = subparsers.add_parser('update', help="Update an existing expense")
    update_parser.add_argument('--id', type=int, required=True)
    update_parser.add_argument('--description', type=str, required=False)
    update_parser.add_argument('--amount', type=float, required=False)
    
    # 'list' subcommand
    subparsers.add_parser('list', help="List expenses")

    # 'summary' subcommand
    summary_parser = subparsers.add_parser('summary', help="Show expense summary")
    summary_parser.add_argument('--month', type=int, default=None)

    # 'delete' subcommand
    delete_parser = subparsers.add_parser('delete', help="Remove an expense")
    delete_parser.add_argument('--id', nargs=1, type=int, required=True)

    args = parser.parse_args()

def add_expensive(args):
    pass


def main() -> None:
    build_parser()


if __name__ == "__main__":
    main()

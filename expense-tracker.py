import argparse
import sys
import json
import datetime

def build_parser() -> argparse.ArgumentParser:
    """Build and configure the argument parser for the Expense Tracker CLI,
    registering the add, update, list, delete and summary subcommands."""
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
    
    # 'delete' subcommand
    delete_parser = subparsers.add_parser('delete', help="Remove an expense")
    delete_parser.add_argument('--id', nargs=1, type=int, required=True)

    # 'list' subcommand
    subparsers.add_parser('list', help="List expenses")

    # 'summary' subcommand
    summary_parser = subparsers.add_parser('summary', help="Show expense summary")
    summary_parser.add_argument('--month', type=int, default=None)

    return parser


    def route_commands(parser, args):
        """Route to the matching handler based on the command provided;
        fall back to the help message if the command is missing or invalid"""
        if args == 'add':
            pass
        elif args == 'update':
            pass
        elif args == 'delete':
            pass
        elif args == 'list':
            pass
        elif args == 'summary':
            pass
        else:
            parser.print_help()


def add_expensive(args):
    pass


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    route_commands(parser, args)


if __name__ == "__main__":
    main()

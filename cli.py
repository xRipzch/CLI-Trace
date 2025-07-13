# clitrance/cli.py
import argparse
from main import run_command

def main():
    parser = argparse.ArgumentParser(description="CLITrance: OSINT reconnaissance tool")
    subparsers = parser.add_subparsers(dest="command")

    # user command
    user_parser = subparsers.add_parser("user", help="Check username across platforms")
    user_parser.add_argument("username", type=str, help="Username to search")

    args = parser.parse_args()
    run_command(args)

if __name__ == "__main__":
    main()

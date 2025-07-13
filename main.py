# clitrance/main.py
from modules import user

def run_command(args):
    if args.command == "user":
        user.run(args.username)
    else:
        print("Invalid Command. Please try again.")

#!/usr/bin/python3

from argparser import create_parser
from modules import add_todo, get_all_todos, display_todos, set_todo_status, delete_by_index, clear, update_by_index, expire_todos


def main():
    expire_todos()

    parser = create_parser()

    args = parser.parse_args()  # Dictionary with key names as options

    todos = get_all_todos()

    args = vars(args)
    if all(args[key] == None for key in args.keys()):
        display_todos()
    else:
        if args["new"] != None:
            if args["due"] is not None:
                add_todo(args["new"], args["due"][0])
            else:
                add_todo(args["new"], None)
        if args["done"] != None:
            set_todo_status(todos, int(args["done"][0]), True)
        if args["undone"] != None:
            set_todo_status(todos, int(args["undone"][0]), False)
        if args["remove"] != None:
            delete_by_index(todos, int(args["remove"][0]))
        if args["edit"] != None:
            update_by_index(todos, int(args["edit"][0]))
        if args["clear"] != None:
            clear()
        if args["expire"] != None:
            expire_overdue_todos(todos)
        display_todos()


if __name__ == "__main__":
    main()

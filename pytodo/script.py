#!/usr/bin/python3

from pymongo import MongoClient
from datetime import datetime, timedelta
from quotes import get_random_quote
from priority import date_sort
from argparser import create_parser

client = MongoClient()
db = client["todo-app"]
collection = db.todos


def parse_date(date):
    """
    Returns a datetime object from a string input.
    """
    if date is not None:
        day, month, year = date.split("-")
        day, month, year = int(day), int(month), int(year)
        return datetime(year, month, day)
    else:
        return None


def add_todo(todo_text, due_date):
    """ Adds an new todo to the DB.
        -----
        todo_text: Text of the todos to be added
    """
    todo = {
        "text": todo_text,
        "is_done": False,
        "created": datetime.now(),
        "due": parse_date(due_date),
    }
    return collection.insert_one(todo).inserted_id


def get_all_todos():
    """ Returns a list of all todo objects in the DB. """
    return date_sort(list(collection.find()))


def display_todos():
    """ 
    Displays the existing todos.
    """
    todos = get_all_todos()
    if len(todos) == 0:
        print("No todos!")
        return
    lengths = [len(todo["text"]) for todo in todos]
    max_len = max(lengths)
    print()
    print(get_random_quote())
    for index, todo in enumerate(todos):
        status_text = "Done" if todo["is_done"] else "PENDING"
        due_text = (
            "\tDue " + todo["due"].strftime("%d %b %y")
            if todo["due"] != None and not todo["is_done"]
            else ""
        )
        spaces = (max_len - len(todo["text"]) + 1) * " "
        display_text = (
            f"{index} - {todo['text']}" + spaces + "-" + status_text + due_text
        )
        print(display_text)
    print()


def set_todo_status(todos, index, status):
    """
    Set the status of a todo.
    -----
    todos: List of todo objects retrieved from the db\n
    index: Index of the task to be marked as seen in the terminal\n
    status: Boolean True => Done, False => Undone
    """
    try:
        todo = todos[index]
        collection.find_one_and_update(
            {"_id": todo["_id"]}, {"$set": {"is_done": status}}
        )
    except IndexError as error:
        print("SELECT THE CORRECT TODO INDEX!!\n")


def delete_by_index(todos, index):
    """
    Delete a todo by its index in the list of todos
    """
    try:
        todo = todos[index]
        delete_by_id(todo["_id"])
    except IndexError as error:
        print("SELECT THE CORRECT TODO INDEX!!\n")


def delete_by_id(id):
    """
    Finds and deletes a todo from the database by id.
    """
    collection.find_one_and_delete({"_id": id})

def clear():
    """
    Clears all todos from the database.
    """
    collection.delete_many({})


def update_by_index(todos, index):
    """
    Updates the text of a todo
    """
    try:
        todo = todos[index]
        new_text = input("Enter new text: ")
        collection.find_one_and_update(
            {"_id": todo["_id"]}, {"$set": {"text": new_text}}
        )
    except IndexError:
        print("SELECT THE CORRECT TODO INDEX!!\n")


def expire_todos():
    """
    Removes a todo from the database once it is marked as done.\n
    Currently removes a todo is it is marked as done and one hour has passed since its time of creation.
    """
    for todo in collection.find():
        if datetime.now() - todo["created"] > timedelta(hours=1) and todo["is_done"]:
            delete_by_id(todo["_id"])


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
        display_todos()


if __name__ == "__main__":
    main()

from pymongo import MongoClient
from priority import date_sort
from datetime import datetime, timedelta
from quotes import get_random_quote


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
        "quotes_disabled": False,
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
    if not todos[0]["quotes_disabled"] :
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
    Updates the text and due date of a todo
    """
    try:
        todo = todos[index]
        print("Do you want to update the title? [y/n]: ", end="")
        ans1 = input().lower()
        if ans1 == 'y':
            new_text = input("Enter new text: ")
            collection.find_one_and_update(
                {"_id": todo["_id"]}, {"$set": {"text": new_text}}
            )
        elif ans1 == 'n':
            pass
        else:
            print("NO PROPER INPUT GIVEN")
        print("Do you want to update the due date? [y/n]: ", end="")
        ans2 = input().lower()
        if ans2 == 'y':
            new_date = input("Enter new due date in the format dd-mm-yyyy: ")
            collection.find_one_and_update(
                {"_id": todo["_id"]}, {"$set": {"due": parse_date(new_date)}}
            )
        elif ans1 == 'n':
            pass
        else:
            print("NO PROPER INPUT GIVEN")
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


def expire_overdue_todos(todos):
    """
    Removes all overdue todos irrespective of their status
    """
    for todo in todos:
        if datetime.now() > todo["due"]:
            delete_by_id(todo["_id"])


def disable_quotes(flag):
    """
    Enables/Disables the display of random quotes
    """
    if flag != 0 and flag != 1:
        print("USE 0 FOR ENABLING QUOTES\nUSE 1 FOR DISABLING QUOTES")
        return
    collection.update(
        {},{"$set": {"quotes_disabled": bool(flag)}}
    )	

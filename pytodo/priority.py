from datetime import datetime


def date_sort(todo_list):
    """
    Sorts the todos by due date and returns a new list of todos.\n
    If a todo doesn't have a due date, it places it at the end of the list.
    """
    dated_todos = [element for element in todo_list if element["due"] != None]
    non_dated_todos = [element for element in todo_list if element["due"] == None]
    return sorted(dated_todos, key=lambda i: i["due"]) + non_dated_todos

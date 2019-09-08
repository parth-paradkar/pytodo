from datetime import datetime

def date_sort(todo_list):
    dated_todos = [element for element in todo_list if element['due'] != None]
    non_dated_todos = [element for element in todo_list if element['due'] == None]
    return sorted(dated_todos, key = lambda i: i['due']) + non_dated_todos
 

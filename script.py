#!/usr/bin/python3

import argparse
from pymongo import MongoClient
from datetime import datetime, timedelta
from quotes import get_random_quote

client = MongoClient()
db = client['todo-app']
collection = db.todos

def add_todo(todo_text):
    """ Adds an new todo to the DB 
        -----
        todo_text: Text of the todos to be added
    """
    todo = {
        'text': todo_text,
        'is_done': False,
        'created': datetime.now()
    }
    return collection.insert_one(todo).inserted_id


def get_all_todos():
    """ Returns a list of all todo objects in the DB """
    return list(collection.find())

def display_todos():
    """ 
    Displays the existing todos
    """
    todos = get_all_todos()
    if(len(todos) == 0):
        print('No todos!')
        return
    lengths = [len(todo['text']) for todo in todos ]
    max_len = max(lengths)
    print()
    print(get_random_quote())
    for index, todo in enumerate(todos):
        status_text = 'Done' if todo['is_done'] else 'PENDING'
        spaces = (max_len - len(todo['text']) + 1) * ' '
        display_text = f"{index} - {todo['text']}" + spaces + '-' + status_text
        print(display_text)
    print()

def set_todo_status(todos, index, status):
    """
    Set the status of a todo
    -----
    todos: List of todo objects retrieved from the db\n
    index: Index of the task to be marked as seen in the terminal\n
    status: Boolean True=> Done, False=> Undone
    """
    todo = todos[index]
    collection.find_one_and_update({'_id': todo['_id']}, {'$set': {'is_done': status}})

def delete_by_id(id):
    collection.find_one_and_delete({ '_id': id })

def expire_todos():
    for todo in collection.find():
        if(datetime.now() - todo['created'] > timedelta(hours=1) and todo['is_done']):
            delete_by_id(todo['_id'])

def main():
    expire_todos()
    parser = argparse.ArgumentParser()
    parser.add_argument('--new', dest='new')
    parser.add_argument('--done', action='append')
    parser.add_argument('--undone', action='append')
    args = parser.parse_args() # Object with attribute names as the option names

    # --new => create an new todo
    # --done => mark an existing todo as done
    # --undone => unmark an existing todo as done
    todos = get_all_todos()
    args = vars(args)
    if(all(args[key] == None for key in args.keys())):
        display_todos()
    else:
        if(args['new'] != None):
            add_todo(args['new'])
        if(args['done'] != None):
            set_todo_status(todos, int(args['done'][0]), True)
        if(args['undone'] != None):
            set_todo_status(todos, int(args['undone'][0]), False)
        display_todos()
        
if __name__ == '__main__':
    main()
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('--new', dest='new', help='create an new todo')
    parser.add_argument('--done', action='append', help='mark an existing todo as done')
    parser.add_argument('--undone', action='append', help='unmark an existing todo as done')
    parser.add_argument('--remove', action='append', help='remove a todo from db')
    parser.add_argument('--due', action='append', help='due date of the todo in the format dd-mm-yyyy')
    return parser

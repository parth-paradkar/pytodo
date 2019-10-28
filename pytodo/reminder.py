import script
from datetime import datetime,timedelta

def reminder_func():
    print("Welcome to your terminal. Here are your tasks!")
    print()
    todos = script.get_all_todos()
    print(script.get_random_quote())
    pending_list = list()
    for todo in todos:
        if todo["is_done"]==False and todo["due"]!=None:
            pending_list.append((todo['text'],todo['due']))
    curr_date = datetime.now().date()
    rem_list_due_today = list()
    rem_list_due_tomo = list()
    for rem in range(0,len(pending_list)):
        if pending_list[rem][1].date() == curr_date:
            rem_list_due_today.append(pending_list[rem])
        elif pending_list[rem][1].date() == curr_date+timedelta(days=1):
            rem_list_due_tomo.append(pending_list[rem])
    print("Tasks due today!")
    for i in range(0,len(rem_list_due_today)):
        print(i+1, '-', rem_list_due_today[i][0])
    print()
    print("Tasks due tomorrow!")
    for i in range(0,len(rem_list_due_tomo)):
        print(i+1, '-', rem_list_due_tomo[i][0])


    

reminder_func()

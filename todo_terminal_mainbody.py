from todo_functions import *
import json
welcome = '''
Command Line Todo application
=========================

Command line arguments:
        -l  Lists all compeleted tasks.
        -la Lists all tasks. 
        -a <Task name> Add multiple new tasks:
                       <Entry instruction: Separate tasks by "/">
        -r <Task ID> remove a tasks
                        <Entry instruction: Separate task IDs by space>
        -c <Task ID> Compelete a tasks
                        <Entry instruction: Separate task IDs by space>
        -h   Show Help
        -e   exit
'''

print(welcome)
load_file()
while True:
    command = get_command()
    command.strip()
    if command == '-e': break
    elif command == '-h':
        print(welcome)
    elif command.startswith('-l') and len(command.strip()) == 2:
        list_compeleted_task()
    elif command.startswith('-la') and len(command.strip()) == 3:
        list_all_task()      
    elif command.startswith('-a'):
        add_task(command[2:])
    elif command.startswith('-c'):
        get_stat(command[2:])
    elif command.startswith('-r'):
        remove_task(command[2:])
    else: print('\033[3;33mYou have entered wrong command! Try again or insert "-h" for help.\u001b[0m')     
write_to_file()

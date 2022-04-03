import json
# ---------------------Read from file function----------------------------
def load_file():
    global task_list
    try:
        loaded_file = open('C:\[Iman]\[1]IBS Materials\ImanTabari_TO_DO_APP\Todo.json','r')
        task_list = json.loads(loaded_file.read())
    except:
        task_list = []        
    return task_list           

#---------------------Get command function--------------------------------
def get_command():
    u_command = input('\033[1;36m Please enter your command:\u001b[0m')
    return u_command

#---------------------print all task on the screen function------------------------
def list_all_task():
    if len(task_list) == 0:
        print ('\033[4;37mNo todos for today! :)\u001b[0m')
        print ('\033[3;33mTo add tasks use "-a" argument; for more help insert "-h".\u001b[0m')
    else:   
        task_id = 1    
        for task in task_list:
            if task['status'] == 'DONE':
                print(f"{task_id}-  [x] {task['name']}")
            else:
                print(f"{task_id}-  [ ] {task['name']}")
            task_id += 1     

#------------------print all compeleted tasks on the screen function------------
def list_compeleted_task():
        task_id = 1
        compeleted_task = [task['name'] for task in task_list if task['status'] == 'DONE' ]
        if len(compeleted_task) > 0:  
            for elm in compeleted_task:  
                print(f"{task_id}-  [x] {elm}")
                task_id += 1
        else: print('\033[4;37mNo job has been compeleted yet!!\u001b[0m')  

#---------------------Add tasks function-----------------------------------
def add_task(task):
    task = task.strip()
    if len(task) == 0:
        print('\033[1;31mUnable to add: no task provided; try agin. For more help insert "-h".\u001b[0m')
        return
    else:
        for items in task.split('/'):
            task_list.append({'name':items,'status':'NOT DONE'})
        print(f'\033[3;32mTasks "{task}" are added successfully :)\u001b[0m')
    write_to_file()                        

#---------------------Change the status of tasks(Compeleted/Not Compeleted) function----------
def get_stat(indL):
    indL = indL.strip()
    if len(indL) == 0:
        print('\033[1;31mUnable to remove: no index provided; try agin. For more help insert "-h".\u001b[0m')
        return
    for index in indL.split():
        try: 
            task_list[int(index)-1]['status'] = 'DONE'
            print(f'\033[3;32mTasks "{index}"th are compeleted successfully :)\u001b[0m')
        except ValueError:
            print(f'\033[1;31mUnable to compeleted "{index}" task: index is not a number\u001b[0m')
        except IndexError:
            print(f'\033[1;31mUnable to compeleted "{index}th" task: index is out of bound\u001b[0m')
    write_to_file()            

#---------------------Remove tasks function----------------------------
def remove_task(indL):
    indL = indL.strip()
    if len(indL) == 0:
        print('\033[1;31mUnable to remove: no index provided; try agin. For more help insert "-h".\u001b[0m')
        return
    for index in sorted(indL.split(), reverse = True):
        try:
            del task_list[int(index)-1]
            print(f'\033[3;32mTasks "{index}" are deleted successfully :)\u001b[0m')
        except ValueError:
            print(f'\033[1;31mUnable to remove"{index}" task: index is not a number\u001b[0m')
        except IndexError:
            print(f'\033[1;31mUnable to remove"{index}th" task: index is out of bound\u001b[0m')   
    write_to_file()         

#---------------------Save all changes to a file Function-----------------------
def write_to_file(): 
    fname = open('C:\[Iman]\[1]IBS Materials\ImanTabari_TO_DO_APP\Todo.json','w')
    fl = list()
    for elm in task_list:
        fl.append(elm)
    fname.write(json.dumps(fl)) 

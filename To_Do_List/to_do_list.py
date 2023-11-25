
to_do_list =[]
run = True
print('Wlcome to my ToDoList, I hope you manage to achieve all of them :)')
while run:
    print('Your ToDoList is empty of any tasks, lets add some goals')
    init_input = input('Enter (a) to add your first task, or (c) to close the program ').lower()
    if init_input == 'a':
        new_task= input('Enter the new task ')
            
    elif init_input == 'c':
        run= False
        break
    else:
        print(f'the program didnt support this command: {init_input}')
        continue
    to_do_list.append(new_task)
    while to_do_list != []:
        print('the current ToDoList is: ')
        print(to_do_list)
        user_input= input('What is your next step, select one of these options: (a) for add new task, (d) for removing a task, (c) for close the program ').lower()
        if user_input == 'a':
            new_task= input('Enter the new task ')
            to_do_list.append(new_task)
        elif user_input == 'd':
            task_index= int(input('enter the number of the task which you want to remove '))-1
            to_do_list.remove(to_do_list[task_index])
        elif user_input == 'c':
            break
        else:
            print(f'the program didnt support this command: {user_input}')
    run = False

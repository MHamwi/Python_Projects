class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the ToDoList."""
        self.tasks.append(task)

    def remove_task(self, task_index):
        """Remove a task from the ToDoList based on its index."""
        try:
            del self.tasks[task_index]
        except IndexError:
            print("Invalid task index. Task not found.")

    def display_tasks(self):
        """Display the current tasks in the ToDoList."""
        print('The current ToDoList is:')
        print(self.tasks)

def main():
    print('Welcome to my ToDoList. I hope you manage to achieve all of them :)')

    run_outer_loop = True
    todo_list = ToDoList()

    while run_outer_loop:
        print('Your ToDoList is empty of any tasks, let\'s add some goals')
        init_input = input('Enter (a) to add your first task, or (c) to close the program ').lower()

        if init_input == 'a':
            new_task = input('Enter the new task ')
            todo_list.add_task(new_task)
        elif init_input == 'c':
            run_outer_loop = False  # Break out of the outer loop if the user enters 'c'
        else:
            print(f'The program didn\'t support this command: {init_input}')
            continue

        while todo_list.tasks:
            todo_list.display_tasks()
            user_input = input('Select one of these options: (a) for add new task, (d) for removing a task, (c) for close the program ').lower()

            if user_input == 'a':
                new_task = input('Enter the new task ')
                todo_list.add_task(new_task)
            elif user_input == 'd':
                try:
                    task_index = int(input('Enter the number of the task you want to remove ')) - 1
                    todo_list.remove_task(task_index)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
            elif user_input == 'c':
                run_outer_loop = False  # Break out of both loops if the user enters 'c'
                break

if __name__ == "__main__":
    main()

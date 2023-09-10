# Todo list
# Created By Cameron Krane
#
# Create a Todo List

# Create an array for the list to use as storage
lists = []
# Function to add a task to the list
def add_task(list):
    lists.append(list)
    print("\nTask added to list\n", list)

# Function to remove a task from the list
def remove_task(list):
    if lists:
        choice = int(list) - 1
        print("\nYour item to delete is index \n", choice)
        del lists[choice]
        print("\nTask removed\n", )
        input("Press Enter to Continue")
        print("Your remaining items are: ")
        show_list()

    else:
        print("\nNo task found\n", list)

# Function to show the list
def show_list():
    if lists:
        print("\nTodo Items:")
        for index, list in enumerate(lists, start=1):
            print(f"{index}. {list}")
        else:
            print("\nEnd of list \n")
    input("Press Enter to Continue")


# Choose item, input choice, run choice
while True:
    print("\nTodo List - Menu:")
    print("1 - Add Item")
    print("2 - Remove Item")
    print("3 - Show Items")
    print("4 - Quit")

    choice = input("\nChoose the number that best represents your choice and hit enter:   ")

    if choice == '1':
        list = input("What is your task?  ")
        add_task(list)
    elif choice == '2':
        list = input("Enter the task to remove. Please use the number corresponding to the task. ")
        remove_task(list)
    elif choice == '3':
        show_list()
    elif choice == '4':
        print("\nGoodbye and Goodnight\n")
        break
    else:
        print("Incorrect input.  Please start application over again. ")

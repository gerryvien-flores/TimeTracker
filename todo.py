#!/usr/bin/python3

#Create a to do list application.
"""
Instructions:
#Your to do list must have a Create, Read, and Delete Functionality.
#Your program must automatically generate a task file with a '.txt' extension.
#Your program should also contain a looping mechanism that allows user to continuously use the program.
#The user must have an option to create, read or delete a task.
When users Schoose to:
    Create a task - the program must ask them for the name, due date, and notes of the task then after the user input all
        the necessary data, the program must store those data into the task file.
    Delete a task - the users must be able to specify the number of the task that they want to delete.
        Then the program will automatically delete the numbers along with its contents in the file.
    Read a task - the program must show all the contents of the task file. This function must also be executed when
        the user will create or delete a file.

Below is a layout that you can use:


def createTaskFile():
   - Generate a task file, If the file is created then retun "Task File is created successfully."
   - If task file already existed then the program will return "Task File is Ready."

def addTask():
   - Will allow user to add a task information(Name, Due Date, Note) to the task file.

def readTask():
   - Will show all the contents of the task file.
   - Generate task in an ordered list using numbers as bullet.

def deleteTask(numOfTask):
   - Will remove a specific task
   - This method should have a parameter which is the number of task that you want to delete.

def main():
   - File creation process will occur here.
   - Will contain the looping mechanism.
   - Ask the user what they want to do.
   - If the user enter:
        1 - Create a Task
        2 - Read Tasks
        3 - Delete a Task
   - If the user enters an invalid input print "Invalid Input. Please enter a valid input." then ask the user again.

while True:
    - Will be the mainloop of your program.
    - After using a function. Ask the user if he want to try again. Use "Y" to indicate Yes, and "n" to indicate.
    - If the user enters "Y" then reloop the main function.
    - If the user enters "n" then thank the user for using the program, and terminate the program.
    - If the user enters an invalid input print "Invalid Input" then terminate the program.

Note: You may rename the methods, and you may use a different structurOpen task.txt of code.
Additional Note:
- Try except is allowed.
- Use at least one fruitful method.
- Use a method with a parameter.
- The filename of your file should be in this format: <Team Number>-<Submission Date>.py e.g. TEAM5 - 11/22/2022
- Failure to follow instructions will result into the deduction of points.


"""

def createTaskFile():
    try:
        taskFile = open("task.txt", "x")
        return "Task File is created successfully."
    except FileExistsError:
        return "Task File is Ready"

def addTask():
    newTask = input("Add a task: ")
    taskDue = input("Due of task: ")
    taskNote = input("Add task note: ")
    taskFile = open("task.txt", "a")
    taskFile.write(newTask + "~~~" + taskDue + "~~~" + taskNote + "\n")
    taskFile.close()

def readTask():
    n = 1
    tableHeader = "No. \tTask~~~~~Due Date~~~~~Notes"
    print(' '.join(map(str, tableHeader.split("~"))))
    with open("task.txt", "r") as taskFile:
        for line in taskFile:
            line = line.strip().split("~")
            print(str(n), ' '.join(map(str, line)), sep = "\t")
            n += 1
        taskFile.close()

def deleteTask(indexOfTask):
    with open("task.txt", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            if number not in [indexOfTask - 1]:
                fp.write(line)

def main():
    print(createTaskFile())
    while True:
        query = input("Select 1 - Add Task, 2 - Read Task, 3 - Delete Task: ")
        match(query):
            case "1":
                readTask()
                addTask()
                break
            case "2":
                readTask()
                break
            case "3":
                readTask()
                taskToDelete = input("Please enter the number of the task you want to delete: ")
                deleteTask(int(taskToDelete))
                break
            case _:
                print("Invalid Input. Please enter a valid option.")

while True:
    main()
    question = input("Do you want to try again?[Y/n]: ").casefold()
    match(question):
        case "y":
            continue
        case "n":
            print("Thank you!")
            break
        case _:
            print("Invalid Input.")
            break


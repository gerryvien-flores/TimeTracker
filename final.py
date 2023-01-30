#!/usr/bin/python3

from tkinter import *

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
            print(n, ' '.join(map(str, line)), sep = "\t")
            n += 1
        taskFile.close()

window = Tk()
window.title("TimeTracker")
window.geometry("500x500")
window.resizable(0,0)
taskFrame = Frame(root)
newTask

window.mainloop()


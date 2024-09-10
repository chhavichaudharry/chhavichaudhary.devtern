from tkinter import *


from tkinter import messagebox


tasks_list = []



def inputError():
  
  
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty.")
        return 0
    return 1



def clear_taskField():
    enterTaskField.delete(0, END)

#

def insertTask():
    
    
    if inputError() == 0:
        return

  
  
    task = enterTaskField.get()
    tasks_list.append({"task": task, "status": "Incomplete"})

   
   
    clear_taskField()
    viewTasks()


def viewTasks():
    TextArea.delete(1.0, END)
    for i, task in enumerate(tasks_list, 1):
        status = "[Completed]" if task["status"] == "Complete" else "[Pending]"
        TextArea.insert(END, f"[ {i} ] {task['task']} {status}\n")



def updateTask():
    task_no = taskNumberField.get(1.0, END).strip()
    if not task_no.isdigit() or int(task_no) <= 0 or int(task_no) > len(tasks_list):
        messagebox.showerror("Input Error", "Invalid task number.")
        return
    task_no = int(task_no) - 1
    new_task = enterTaskField.get()
    if new_task == "":
        messagebox.showerror("Input Error", "Task field cannot be empty.")
        return
    tasks_list[task_no]["task"] = new_task
    clear_taskField()
    clear_taskNumberField()
    viewTasks()


def completeTask():
    task_no = taskNumberField.get(1.0, END).strip()
    if not task_no.isdigit() or int(task_no) <= 0 or int(task_no) > len(tasks_list):
        messagebox.showerror("Input Error", "Invalid task number.")
        return
    task_no = int(task_no) - 1
    tasks_list[task_no]["status"] = "Complete"
    clear_taskNumberField()
    viewTasks()



def deleteTask():
    task_no = taskNumberField.get(1.0, END).strip()
    if not task_no.isdigit() or int(task_no) <= 0 or int(task_no) > len(tasks_list):
        messagebox.showerror("Input Error", "Invalid task number.")
        return
    task_no = int(task_no) - 1
    tasks_list.pop(task_no)
    clear_taskNumberField()
    viewTasks()


def clear_taskNumberField():
    taskNumberField.delete(0.0, END)



if __name__ == "__main__":

    gui = Tk()



    gui.configure(background="light green")

   
    gui.title("To-Do List App")


    gui.geometry("300x400")

   
   
    enterTask = Label(gui, text="Enter Your Task", bg="light green")

  
  
    enterTaskField = Entry(gui)

 
 
    Submit = Button(gui, text="Add Task", fg="Black", bg="Red", command=insertTask)

 
 
    TextArea = Text(gui, height=10, width=30, font="lucida 13")


    taskNumber = Label(gui, text="Task Number", bg="blue")

    taskNumberField = Text(gui, height=1, width=5, font="lucida 13")



    View = Button(gui, text="View Tasks", fg="Black", bg="Yellow", command=viewTasks)
    Update = Button(gui, text="Update Task", fg="Black", bg="Orange", command=updateTask)
    Complete = Button(gui, text="Complete Task", fg="Black", bg="Green", command=completeTask)
    Delete = Button(gui, text="Delete Task", fg="Black", bg="Red", command=deleteTask)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)



    enterTask.grid(row=0, column=1)
    enterTaskField.grid(row=1, column=1, ipadx=50)
    Submit.grid(row=2, column=1, pady=5)
    TextArea.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    taskNumber.grid(row=4, column=1, pady=5)
    taskNumberField.grid(row=5, column=1)
    View.grid(row=6, column=1, pady=5)
    Update.grid(row=7, column=1, pady=5)
    Complete.grid(row=8, column=1, pady=5)
    Delete.grid(row=9, column=1, pady=5)
    Exit.grid(row=10, column=1, pady=5)



    gui.mainloop()
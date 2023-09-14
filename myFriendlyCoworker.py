# environment dev 2 (installed tk and pillow), wichtig für Readme File
# send picture with github
import tkinter as tk
from PIL import Image, ImageTk
import random

# create the GUI and configure it
root = tk.Tk()
root.title('My Friendly Coworker')
root.geometry("405x720")

# create a window frame for every page of a function for the app
f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)
f5 = tk.Frame(root)
frame_calculator = tk.Frame(root)

# read the image you want to use for the first frame
img = Image.open('images_app/pink.jpeg')
# resize the image
img = img.resize((405, 720), Image.LANCZOS)

# add this code to view the image as the frame
pic = ImageTk.PhotoImage(img)
Lab = tk.Label(f1, image=pic)
Lab.pack()
f1.pack()

# create a headline
head1 = tk.Label(f1, text='Welcome to Your Friendly Coworker,', font='lucinda 15 bold', bg='Pink', fg='Black')
head1.place(x=30, y=50)

head2 = tk.Label(f1, text='who can...', font='lucinda 16', bg='Pink', fg='Black')
head2.place(x=30, y=80)

# code for switching between frames from:
# https://www.tutorialspoint.com/how-to-switch-between-two-frames-in-tkinter#:~:text=In%20most%20cases%2C%20you%20need,many%20widgets%20in%20the%20application.

def forget_all():
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f5.pack_forget()
    frame_calculator.pack_forget()

# when you push the button all the frames get forgotten and only the corresponding frame gets packed again with all its widgets

def habittracker():
    forget_all()
    f2.pack(fill='both', expand=1)
    root.title("Habit Tracker")
    f2.configure(background="pink")

def workinghours():
    forget_all()
    f3.pack(fill='both', expand=1)
    root.title("Working Time Tracker")

    # something where you type in your workhours and it calculates your workhours per week and if it shows whether it is right/wrong

def todolist():
    forget_all()
    f4.pack(fill='both', expand=1)
    root.title("To Do List")

    # create a simple to do list editor

    taskinp = tk.StringVar()
    inptask = tk.Entry(f4, textvariable=taskinp, font='Lucinda 20 bold')
    inptask.place(x=30, y=50)


def chatbot():
    forget_all()
    f5.pack(fill='both', expand=1)
    root.title("Chatbot")

    # maybe a Chatbot working with a simple if/else print function and buttons


# These variables save the input from the calculator.
input_worktime = tk.IntVar()
input_sleeptime = tk.IntVar()
input_careworktime = tk.IntVar()
input_freetime = tk.IntVar()

frame_calculator.configure(background="pink")

header = tk.Label(frame_calculator, text="Welcome to the Work-Life-Balance Calculator!", font='lucinda 11 bold',
                  bg='Pink', fg='Black')
header.place(x=30, y=50)

explanation_part1 = tk.Label(frame_calculator, text="Type in how much time you spend on", font='lucinda 11 bold',
                             bg='Pink', fg='Black')
explanation_part1.place(x=30, y=80)

explanation_part2 = tk.Label(frame_calculator, text="each task and press calculate.", font='lucinda 11 bold',
                             bg='Pink', fg='Black')
explanation_part2.place(x=30, y=100)

# These are input fields for the hours spent on each task of your day to calculate later.

input_field_work = tk.Entry(frame_calculator, textvariable=input_worktime)
input_field_work.place(x=150, y=130)
work_label = tk.Label(frame_calculator, text="WORK", font='lucinda 11 bold', fg='Black')
work_label.place(x=30, y=130)

input_field_sleep = tk.Entry(frame_calculator, textvariable=input_sleeptime)
input_field_sleep.place(x=150, y=160)
sleep_label = tk.Label(frame_calculator, text="SLEEP", font='lucinda 11 bold', fg='Black')
sleep_label.place(x=30, y=160)

input_field_carework = tk.Entry(frame_calculator, textvariable=input_careworktime)
input_field_carework.place(x=150, y=190)
carework_label = tk.Label(frame_calculator, text="CARE WORK", font='lucinda 11 bold', fg='Black')
carework_label.place(x=30, y=190)

input_field_freetime = tk.Entry(frame_calculator, textvariable=input_freetime)
input_field_freetime.place(x=150, y=220)
freetime_label = tk.Label(frame_calculator, text="FREE TIME", font='lucinda 11 bold', fg='Black')
freetime_label.place(x=30, y=220)

# This creates the calculate button.

calculate_button = tk.Button(frame_calculator, text="CALCULATE", font='lucinda 15 bold', height=1, width=15,
                             command=lambda: calculate_worklifebalance())
calculate_button.place(x=30, y=270)


def calculator():
    forget_all()
    frame_calculator.pack(fill='both', expand=1)
    root.title("Work-Life-Balance Calculator")
    root.update()


def calculate_worklifebalance():
    summe_hours = input_worktime.get() + input_sleeptime.get() + input_careworktime.get() + input_freetime.get()
    summe_label = tk.Label(frame_calculator, text=f"The sum is {summe_hours}.", font='lucinda 11 bold', fg='Black')
    summe_label.place(x=30, y=330)
    work_percentage_label = tk.Label(frame_calculator, text=f"Work makes up "f"{int((input_worktime.get() *100) / summe_hours)}% of your time.", font='lucinda 11 bold', fg='Black')
    work_percentage_label.place(x=30, y=360)
    sleep_percentage_label = tk.Label(frame_calculator, text=f"Sleep makes up "f"{int((input_sleeptime.get() *100) / summe_hours)}% of your time.", font='lucinda 11 bold', fg='Black')
    sleep_percentage_label.place(x=30, y=390)
    carework_percentage_label = tk.Label(frame_calculator, text=f"Carework makes up "f"{int((input_careworktime.get() *100) / summe_hours)}% of your time.", font='lucinda 11 bold', fg='Black')
    carework_percentage_label.place(x=30, y=420)
    freetime_percentage_label = tk.Label(frame_calculator, text=f"Freetime makes up "f"{int((input_freetime.get() *100) / summe_hours)}% of your time.", font='lucinda 11 bold', fg='Black')
    freetime_percentage_label.place(x=30, y=450)
    calculator()

# create the buttons for every function with a little explanatory text underneath

 # Habit Tracker Button


hbutton = tk.Button(f1, text="Habit Tracker 📈", font='lucinda 15 bold', height=1, width=15, command=lambda: habittracker())
hbutton.place(x=10, y=350)
hexplain = tk.Label(f1, text='...encourage you to healthier habits.', font='lucinda 8', bg='Pink', fg='Black')
hexplain.place(x=10, y=400)

# Working Hours Tracker
wbutton = tk.Button(f1, text="Working Hours🕖", font='lucinda 15 bold', height=1, width=15, command=lambda: workinghours())
wbutton.place(x=210, y=350)
wexplain = tk.Label(f1, text='...help you track your work hours.', font='lucinda 8', bg='Pink', fg='Black')
wexplain.place(x=210, y=400)

# To Do List
tbutton = tk.Button(f1, text="To Do List ✔", font='lucinda 15 bold', height=1, width=15, command=lambda: todolist())
tbutton.place(x=10, y=250)
texplain = tk.Label(f1, text='...remind you of your To Dos.', font='lucinda 8', bg='Pink', fg='Black')
texplain.place(x=10, y=300)

# ChatBot
chbutton = tk.Button(f1, text="Chatbot", font='lucinda 15 bold', height=1, width=15, command=lambda: chatbot())
chbutton.place(x=210, y=250)
chexplain = tk.Label(f1, text='...provide you with information about', font='lucinda 8', bg='Pink', fg='Black')
chexplain.place(x=210, y=300)
chexplain = tk.Label(f1, text='work safety, stress relief and more.', font='lucinda 8', bg='Pink', fg='Black')
chexplain.place(x=210, y=320)

# Calculator
calcbutton = tk.Button(f1, text="Calculator", font='lucinda 30 bold', command = lambda: calculator())
calcbutton.place(x=80, y=450)
calcexplain = tk.Label(f1, text='...help you calculate your Work-Life-Balance Score.', font='lucinda 8', bg='Pink', fg='Black')
calcexplain.place(x=75, y=550)


def homescreen():
    # switching to Frame1
    forget_all()
    f1.pack(fill='both', expand=1)
    root.title("My Friendly Coworker")

homescreen()

# This code creates the buttons on the taskbar.

home_button = tk.Button(text="🛖", font='lucinda 20 bold', command=lambda: homescreen())
home_button.place(x=25, y=650)

habittracker_button = tk.Button(text="📈", font='lucinda 20 bold', command=lambda: habittracker())
habittracker_button.place(x=125, y=650)

workhours_button = tk.Button(text="🕖", font='lucinda 20 bold', command=lambda: workinghours())
workhours_button.place(x=225, y=650)

todolist_button = tk.Button(text="✔", font='lucinda 20 bold', command=lambda: todolist())
todolist_button.place(x=325, y=650)

# This line is to execute the code.
root.mainloop()

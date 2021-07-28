import tkinter
from tkinter import ttk
import datetime
import os
import pandas as pd

d = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def ButtonOnclick(event):
    dictionary = {}
    print("ButtonClicked")
    global tasks
    global vs
    global df
    try:
        df = pd.read_csv("achievement.csv")
    except:
        df = pd.DataFrame()
    count = 0
    for i, a in enumerate(vs):

        if a.get() == True:
            dictionary[tasks[i]] = True
            print("{} is checked".format(tasks[i]))
            count += 1
        else:
            dictionary[tasks[i]] = False
    print(count)
    d = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    dfn = pd.DataFrame(dictionary,index=[d])
    df = pd.concat([df,dfn],axis = 1)
    df.to_csv("achievement.csv")
    print(df)
def Saver():
    #save some shit
    pass

root = tkinter.Tk()
s = ttk.Style(root).theme_use('clam')
#print(s.theme_names())

tasks = ["Workout", "Skill learning", "One coffee only", "No bad habits", "Read", "Track monthly goals",
        "Prepare next day", "Stick to routine", "Around motivated people", "Walk", "Podcast", "Meditate",
        "Journal", "Gratefulness", "Record win"]

#It seems like that this must be below root = tkinter.Tk().
v = tkinter.BooleanVar()
vs = []
for a in tasks:
    vs.append(tkinter.BooleanVar())


root.title("Software Title")
root.geometry("800x600")


txt1 = tkinter.Label(text =u"test")

txt1.pack()
#txt1.place(x=300,y = 200)
button1 = tkinter.Button(text = u"button", width = 50)
button1.bind("<Button-1>", ButtonOnclick)
button1.pack()
for i,task in enumerate(tasks):

    tkinter.Checkbutton(text = task, variable = vs[i]).pack()





root.mainloop()

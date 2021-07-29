import tkinter
from tkinter import ttk
import datetime
import os
import pandas as pd
import pickle

d = datetime.datetime.now().strftime('%Y%m%d')

def pickler(X):
    filenameX = ("achievement.sav")
    pickle.dump(X, open(filenameX, "wb"))

#Utilities below.
def loader():
    filenameX = ("achievement.sav")
    with open(filenameX, mode="rb") as f:
        X = pickle.load(f)
    return X

def nice_counter():
    nice_counter = 0
    try:
        data = loader()
        for i,a in enumerate(data):
            for j,b in enumerate(data[a]):
                if data[a][b] == True:
                    nice_counter += 1
        return nice_counter/(i+1)
    except:
        return 0


def ButtonOnclick(event):
    dictionary = {}
    print("ButtonClicked")
    global tasks
    global vs
    global df
    try:
        data = loader()
    except:
        data = {}
    count = 0
    for i, a in enumerate(vs):

        if a.get() == True:
            dictionary[tasks[i]] = True
            print("{} is checked".format(tasks[i]))
            count += 1
        else:
            dictionary[tasks[i]] = False
    print(count)
    d = datetime.datetime.now().strftime('%Y%m%d')
    data[d] = dictionary
    pickler(data)
    #dfn = pd.DataFrame(dictionary,index=[d])
    #df = pd.concat([df,dfn],axis = 1)
    #df.to_csv("achievement.csv")
    print(data)
def Saver():
    #save some shit
    pass

root = tkinter.Tk()
s = ttk.Style(root).theme_use('clam')
print(nice_counter())  #move it out already.
#print(s.theme_names())

tasks = ["Workout", "Skill learning", "One coffee only", "No bad habits", "Read", "Track monthly goals",
        "Prepare next day", "Stick to routine", "Around motivated people", "Walk", "Podcast", "Meditate",
        "Journal", "Gratefulness", "Record win"]
#tasks = ["1","2"]
#It seems like that this must be below root = tkinter.Tk().
v = tkinter.BooleanVar()
vs = []

for a in tasks:
    vs.append(tkinter.BooleanVar())
try:
    data = loader()
except:
    data = {}
print(data)
d = datetime.datetime.now().strftime('%Y%m%d')

try:
    for i, dt in enumerate(data[d]):
        if data[d][dt] == True:
            vs[i].set(True)
        else:
            vs[i].set(False)
except:
    print("First save today")


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

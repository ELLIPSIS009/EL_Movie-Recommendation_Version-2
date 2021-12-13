from tkinter import *
import tkinter as tk
import tkinter.font as tkfont
import pandas as pd
import numpy as np

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

def activate(a):
   if a[0] == 1:
      entry1.config(state='normal')
   if a[1] == 1:
      entry2.config(state='normal')
   if a[2] == 1:
      entry3.config(state='normal')
   if a[3] == 1:
      entry4.config(state='normal')
   
def allstates():
   activate(list(lng.state()))

def back():
   root.destroy()
   import homepage

def search():
   a = entry1.get()
   d = entry2.get()
   r = entry3.get()
   g = entry4.get()
   if a == '':
      a = 'zzzzz'
   if d == '':
      d = 'zzzzz'
   if r == '':
      r = 100
   else:
      r = int(r)
   if g == '':
      g = 'zzzzz'
   index = 0
   check1, check2, check3, check4 = [], [], [], []
   index = 0
   for r4 in df['Actors']:
      for j4 in r4.split(","):
         if a.lower() in j4.lower():
               check4.append(index+1)
      index += 1
   index = 0
   for r4 in df['Director']:
      for j4 in r4.split(","):
         if d.lower() in j4.lower():
               check4.append(index+1)
      index += 1
   index = 0
   for r3 in df["Rating"]:
      if r in np.arange(r3-0.5, r3+0.6, 0.1):
         check3.append(index)
      index += 1
   index = 0
   for r4 in df['Genre']:
      for j4 in r4.split(","):
         if g.lower() in j4.lower():
               check4.append(index+1)
      index += 1
   m = [check1, check2, check3, check4]
   for i in range(4):
      if len(m[i]) == 0:
         for j in range(4):
            if len(m[j]) != 0:
               m[i] = m[j]
   common = m[0] and m[1] and m[2] and m[3]
   listbox_update('')
   j = 0
   for i in common:
      movie_title = df[df.Rank == i]['Title'].values[0]
      listbox.insert(5, f'{movie_title}')
      j = j+1
      if j>11:
         break

def on_keyrelease_actor(event):
   value = event.widget.get()
   value = value.strip().lower()
   if value == '':
      data = ''
   else:
      data =[]
      for i in df['Actors']:
         for j in i.split(","):
            if value in (j.lower()).strip():
               data.append(j)
      data = list(set(data))
   listbox_update(data)

def on_keyrelease_director(event):
   value = event.widget.get()
   value = value.strip().lower()
   if value == '':
      data = ''
   else:
      data =[]
      for i in df['Director']:
         for j in i.split(","):
            if value in (j.lower()).strip():
               data.append(j)
      data = list(set(data))
   listbox_update(data)

def on_keyrelease_genre(event):
   value = event.widget.get()
   value = value.strip().lower()
   if value == '':
      data = ''
   else:
      data =[]
      for i in df['Genre']:
         for j in i.split(","):
            if value in (j.lower()).strip():
               data.append(j)
      data = list(set(data))
   listbox_update(data)

def listbox_update(data):
    listbox.delete(0, 'end')
    data = sorted(data, key=str.lower)
    for item in data:
        listbox.insert('end', item)


root = Tk()
root.geometry('900x550')
root.title('Movie Search')
root.config(bg='black')

df = pd.read_csv('IMDB-Movie-Data.csv')

title = Label(root, text="Movie Search", font=tkfont.Font(family="Lucida Grande", size=25), bg='black', fg='white')
title.pack(padx=10, pady=10)

button0=Button(root, text='Search By', command=allstates,font=10, borderwidth=5, bg='black', fg='white')
button0.place(relx=0.375 ,rely=0.18, relwidth=0.25,relheight=0.075)

lng = Checkbar(root, ['Actor', 'Director', 'Rating', 'Genre'])
lng.pack(side=TOP,  fill=X)

Label1 = Label(root, text="Search by Actor:", bg='black', fg='white', font=('Courier', 9))
Label1.place(relx=0.02, rely=0.31, relwidth=0.15, relheight=0.1)
entry1 = Entry(root, width=40, font=10, bg='black', fg='white', borderwidth=5, insertbackground='white', state='disabled', disabledbackground='#303030')
entry1.bind("<Button-1>", lambda event: entry1.delete(0, 'end'))
entry1.place(relx=0.2,rely=0.3, relwidth=0.35,relheight=0.1)
entry1.bind('<KeyRelease>', on_keyrelease_actor)

Label2 = Label(root, text="Search by Director:", bg='black', fg='white', font=('Courier', 9))
Label2.place(relx=0.02, rely=0.43, relwidth=0.15, relheight=0.1)
entry2 = Entry(root, width=40, font=10, bg='black', fg='white', borderwidth=5, insertbackground='white', state='disabled', disabledbackground='#303030')
entry2.bind("<Button-1>", lambda event: entry2.delete(0, 'end'))
entry2.place(relx=0.2,rely=0.42, relwidth=0.35,relheight=0.1)
entry2.bind('<KeyRelease>', on_keyrelease_director)

Label3 = Label(root, text="Search by Rating:", bg='black', fg='white', font=('Courier', 9))
Label3.place(relx=0.02, rely=0.55, relwidth=0.15, relheight=0.1)
entry3 = Entry(root, width=40, font=10, bg='black', fg='white', borderwidth=5, insertbackground='white', state='disabled', disabledbackground='#303030')
entry3.bind("<Button-1>", lambda event: entry3.delete(0, 'end'))
entry3.place(relx=0.2,rely=0.54, relwidth=0.35,relheight=0.1)

Label4 = Label(root, text="Search by Genre:", bg='black', fg='white', font=('Courier', 9))
Label4.place(relx=0.02, rely=0.67, relwidth=0.15, relheight=0.1)
entry4 = Entry(root, width=40, font=10, bg='black', fg='white', borderwidth=5, insertbackground='white', state='disabled', disabledbackground='#303030')
entry4.bind("<Button-1>", lambda event: entry4.delete(0, 'end'))
entry4.place(relx=0.2,rely=0.66, relwidth=0.35,relheight=0.1)
entry4.bind('<KeyRelease>', on_keyrelease_genre)

listbox = tk.Listbox(root, width = 40, height = 7, font = 10, bg = 'black', fg = 'white')
listbox.place(relx=0.6 ,rely=0.3, relwidth=0.35,relheight=0.475)

button1=Button(root, text='Back', command=back,font=10, borderwidth=5, bg='black', fg='white')
button1.place(relx=0.175 ,rely=0.85, relwidth=0.25,relheight=0.075)

button2 = Button(root, text='Search ', font=10, borderwidth=5, bg='black', fg='white', command=search)
button2.place(relx=0.575 ,rely=0.85, relwidth=0.25,relheight=0.075)

root.mainloop()
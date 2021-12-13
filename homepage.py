import tkinter as tk
import tkinter.font as tkfont

def movie():
    root.destroy()
    import movie

def search():
    root.destroy()
    import searchmovie

root = tk.Tk()
root.geometry('700x300')
root.title('Movie Recomendation Engine')
root.config(bg='black')

title = tk.Label(root, text="Movie Recommendation Engine", font=tkfont.Font(family="Lucida Grande", size=25), bg='black', fg='white')
title.pack(padx=10, pady=10)

button1 = tk.Button(root, text='Movie Recommendations', font=10, borderwidth=5, bg='black', fg='white', command = movie)
button1.place(relx=0.04, rely=0.4, relwidth=0.45, relheight=0.2)

button2 = tk.Button(root, text='Search Movie', font=10, borderwidth=5, bg='black', fg='white', command = search)
button2.place(relx=0.51, rely=0.4, relwidth=0.45, relheight=0.2)

madeby = tk.Label(root, text="", font=10, bg='black', fg='white')
madeby.place(relx=0.15, rely=0.8, relwidth=0.7, relheight=0.1)

root.mainloop()
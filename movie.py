from tkinter import *
import tkinter as tk
import tkinter.font as tkfont
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# on key release for searchbar
def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)
    # update data in listbox
    listbox_update(data)

# updating the searchbar
def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')
    # sorting data 
    data = sorted(data, key=str.lower)
    # put new data
    for item in data:
        listbox.insert('end', item)

# on selecting movie from searchbar
def on_select(event):
    # display element selected on list
    entry.delete(0, "end")
    entry.insert(0, event.widget.get(event.widget.curselection()))

# movie recomendation engine
def mre():
    # Getting the selecteed movie
    title = entry.get()

    # Storing the data
    df = pd.read_csv('IMDB-Movie-Data.csv')

    # Adding new column to hold Movie_ID
    df['Movie_id'] = range(0,1000)

    # Create a column to hold the combined string
    df['important_features'] = get_important_features(df)

    # Convert Text to Matrix of token counts
    # It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.
    cm = CountVectorizer().fit_transform(df['important_features'])

    # Get the Cosine Similarity Martix from count Matrix
    # it measures the cosine angle between two vectors in a multi-dimensional space
    cs = cosine_similarity(cm)

    # Find the Movie's id
    movie_id = df[df.Title == title]['Movie_id'].values[0]

    # Create a list of enumerations for the similarity score [(movie_id, similarity score), (...), ....]
    scores = list(enumerate(cs[movie_id]))

    # Sorting the list
    sorted_scores = sorted(scores, key = lambda x : x[1], reverse = True)
    sorted_scores = sorted_scores[1:]

    # Printing the top 5 similar movies
    listbox_recomendation.delete(0, 'end')
    listbox_recomendation.insert(0, f"Recommended Movies for {title} are :")
    j = 0
    for item in sorted_scores:
        movie_title = df[df.Movie_id == item[0]]['Title'].values[0]
        listbox_recomendation.insert(5, f'{j+1}. {movie_title}')
        j = j+1
        if j>4:
            break

# Functions to combine values of important columns into a single string
def get_important_features(data):
    important_features = []
    for i in range(0, data.shape[0]):
      important_features.append(data['Actors'][i] + ' ' + data['Director'][i] + ' ' + data['Genre'][i] + ' ' + data['Title'][i] + ' ' + str(data['Rating'][i]))
    return important_features

def back():
    root.destroy()
    import homepage

# Loading all the movies
df = pd.read_csv('IMDB-Movie-Data.csv')
test_list = tuple(df['Title'])

# Creating Tkinter window
root = tk.Tk()
root.geometry('700x600')
root.title('Movie Recomendation Engine')
root.config(bg = 'black')

# Body of the window
title = tk.Label(root, text = "Movie Recomendation Engine", font = tkfont.Font(family="Lucida Grande", size=25), bg = 'black', fg = 'white')
title.pack(padx = 10, pady = 10)

entry = tk.Entry(root, width = 40, font = 10, bg = 'black', fg = 'white', borderwidth = 5, insertbackground = 'white')
# Creating Placeholder text
entry.insert(0, 'Search')
entry.bind("<Button-1>", lambda event: entry.delete(0, 'end'))
entry.pack(padx = 10, pady = 10)
# Running search in the list for the text entered
entry.bind('<KeyRelease>', on_keyrelease)

listbox = tk.Listbox(root, width = 40, height = 7, font = 10, bg = 'black', fg = 'white')
listbox.pack(padx = 10, pady = 10)
# selecting movie from the list
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(test_list)

find = tk.Button(root, text = 'Find Recommendations', command = mre, font = 10, borderwidth = 5, bg = 'black', fg = 'white')
find.pack()

listbox_recomendation = tk.Listbox(root, width = 50, height = 6, font = 10, bg = 'black', fg = 'white')
listbox_recomendation.pack(padx = 10, pady = 10)

back = tk.Button(root, text = 'Back', command = back, font = 10, borderwidth = 5, bg = 'black', fg = 'white')
back.pack()

madeby = tk.Label(root, text = "", font = 10, bg = 'black', fg = 'white')
madeby.pack(pady = 20, padx = 10)

root.mainloop()
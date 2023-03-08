from tkinter import *
import random

korean = ["kimbab","Kimchi-rice","shit"]
japanese = ["ramen","sushi","udon"]
chinese = ["dumplins","fried rice","beijing corn"]
def recommendation():
    country =  whitebox.get()
    if country == "korean":
        food = random.choice(korean)
    elif country == "japanese":
        food = random.choice (japanese)
    elif country == "chinese":
        food = random.choice(chinese)
    text1.config(text="try "+food)
window = Tk()
window.title("Menu Recommendation")
window.geometry("500x500")

text1 = Label(window,text="eat what?  (Enter korean/chinese/japanese)")
text1.pack()

whitebox = Entry(window)
whitebox.pack()

btn = Button(window, text="Recommend", command=recommendation)
btn.pack()

window.mainloop()

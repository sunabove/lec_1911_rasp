# coding: utf-8
from guizero import App, ListBox, Text

def change_color(value):
    t.text_color = value

a = App()

t = Text(a, text="Its a ListBox", color="black")

items=["red", "green", "blue", "yellow", "purple", "turquoise", "pink", "orange", "black", "brown", "cyan"]

listbox = ListBox(
    a, 
    items=items, 
    selected="black", 
    command=change_color,
    scrollbar=True)

a.display()


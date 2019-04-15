# coding: utf-8
from guizero import App, Waffle

app = App()

my_waffle = Waffle(app)
my_waffle[2,1].color = "red"
my_waffle[1,1].dotty = True

app.display()

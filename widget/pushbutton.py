# coding: utf-8
from guizero import App, PushButton

def do_nothing():
  print("Button was pressed")

app = App()
button = PushButton(app, command=do_nothing)
app.display()

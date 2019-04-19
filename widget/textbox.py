# coding: utf-8
from guizero import App, TextBox
app = App()
input_box = TextBox(app, text="Type lines here", width=20, height=10, multiline=True)
app.display()

# coding: utf-8
from guizero import App, Box, Text
app = App(title="My app", height=300, width=400)
box = Box(app)
text1 = Text(box, text="Hello from the box", size=14, color="red", font="Arial")
text2 = Text(app, text="Hello from the app", size=14, color="blue", font="Courier New")
app.display()

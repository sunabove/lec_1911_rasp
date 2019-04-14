# coding: utf-8
from guizero import App, ButtonGroup, Text

def update_text():
    what_is_selected.value = activities.value

app = App()
activities = ButtonGroup(app, options=[
                ["Roller Skating", "skate"],
                ["White water rafting", "WWR"],
                ["Mountain climbing", "climb"]
            ],
            selected="skate", command=update_text)

what_is_selected = Text(app, text="skate")
app.display()

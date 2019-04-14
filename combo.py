# coding: utf-8
from guizero import App, Text, Combo
def you_chose(selected_value):
    if selected_value == "Tiny goblet":
        result.value = "You chose...wisely"
    else:
        result.value = "You chose...poorly"

app = App()
instructions = Text(app, text="Choose a goblet")
options = ["", "Huge golden goblet", "Jewel encrusted goblet", "Tiny goblet"]
combo = Combo(app, options=options, command=you_chose)
result = Text(app)
app.display()


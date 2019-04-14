# coding: utf-8
from guizero import App, Text, CheckBox, TextBox
def calculate_extras():
    total = 0
    if syrup.value == 1:
        total += 20
    if sprinkles.value == 1:
        total += 10
    if cream.value == 1:
        total += 50
    cost.value = total


app = App()

questions = Text(app, text="What would you like with your coffee?")

syrup = CheckBox(app, text="Caramel syrup (20p)", command=calculate_extras)
sprinkles = CheckBox(app, text="Chocolate sprinkles (10p)", command=calculate_extras)
cream = CheckBox(app, text="Whipped cream (50p)", command=calculate_extras)

cost_of_extras = Text(app, text="Cost of extras:")
cost = TextBox(app, text="0")

app.display()

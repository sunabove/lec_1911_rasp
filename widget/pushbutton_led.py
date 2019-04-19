# coding: utf-8
from gpiozero import *
from guizero import *

led = LED(17)

def when_button_clicked():
  print("Button was pressed")
  led.toggle()
  if led.value :
    status.value = "LED is on."
  else :
    status.value = "LED is off."

app = App()
button = PushButton(app, text="LED", command=when_button_clicked)
status = Text(app, text="Click the button to toggle the LED" )
app.display()

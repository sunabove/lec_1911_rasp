# coding: utf-8
from guizero import App, MenuBar
def file_function():
    print("File option")

def edit_function():
    print("Edit option")

app = App()
options=[
            [ ["File option 1", file_function], ["File option 2", file_function] ],
            [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
        ]
menubar = MenuBar(app,
        toplevel=["File", "Edit"],
        options=options
        )
app.display()

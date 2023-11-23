# code for getting the lexemes of the .lol file

from tkinter import *

root = Tk()
root.title("The Lords of the Strings Lexical Analyzer")

topFrame = Frame(root)
bottomFrame = Frame(root)

fileExplorer = Label(topFrame, text="File Explorer")

#defining text editor
textEditor = Text(topFrame, width=43, height=10)
textEditor.pack()

tokenList = Label(topFrame, text="Token List")

# display frames
topFrame.pack()
bottomFrame.pack(side=BOTTOM)

# Set the width and height of the window
window_width = 1200
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 3 # Add padding on top
root.geometry(f"+{x}+{y}")

root.mainloop()
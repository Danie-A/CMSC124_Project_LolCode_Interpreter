# code for getting the lexemes of the .lol file
from tkinter import *

root = Tk()
root.title("The Lords of the Strings Lexical Analyzer")

topFrame = Frame(root)
bottomFrame = Frame(root)

fileExplorer = Label(topFrame, text="File Explorer")
textEditor = Text(topFrame, width=43, height=10)
tokensView = Label(topFrame, text="Token List")
symbolTable = Label(topFrame, text="Symbol Table")

executeButton = Button(bottomFrame, text="Execute")
console = Label(bottomFrame, text="Console")

fileExplorer.grid(row=0, column=0, padx=10, pady=10)
textEditor.grid(row=1, column=0, padx=10, pady=10)
tokensView.grid(row=1, column=1, padx=10, pady=10)
symbolTable.grid(row=1, column=2, padx=10, pady=10)

executeButton.grid(row=0, column=0, padx=10, pady=10)
console.grid(row=1, column=0, padx=10, pady=10)

# display frames
topFrame.pack(side=TOP)
bottomFrame.pack(side=TOP)

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

reg = {
    "varident": r'^[a-zA-Z][a-zA-Z0-9_]*$',
    "numbr_literal": r'^-?([1-9][0-9]*|0)$',
    "numbar_literal": r'^(-?[0-9]*(\.[0-9]+)?)$',
    "yarn_literal": r'^\"[^\"\']*\"$',
    "troof_literal": r'^(WIN|FAIL)$',
    "type_literal": r'^(NOOB|NUMBR|NUMBAR|YARN|TROOF)$',
    "hai": r'^HAI$',
    "kthxbye": r'^KTHXBYE$',
    "wazzup": r'^WAZZUP$',
    "buhbye": r'^BUHBYE$',
    "btw": r'^BTW$',
    "obtw": r'^OBTW$',
    "tldr": r'^TLDR$',
    "ihasa": r'^I HAS A$',
    "itz": r'^ITZ$',
    "r": r'^R$',
    "sum": r'^SUM OF$',
    "diff": r'^DIFF OF$',
    "produkt": r'^PRODUKT OF$',
    "quoshunt": r'^QUOSHUNT OF$',
    "mod": r'^MOD OF$',
    "biggr": r'^BIGGR OF$',
    "smallr": r'^SMALLR OF$',
    "both": r'^BOTH OF$',
    "either": r'^EITHER OF$',
    "won": r'^WON OF$',
    "not": r'^NOT$',
    "any": r'^ANY OF$',
    "all": r'^ALL OF$',
    "bothsaem": r'^BOTH SAEM$',
    "diffrint": r'^DIFFRINT$',
    "visible": r'^VISIBLE$',
}


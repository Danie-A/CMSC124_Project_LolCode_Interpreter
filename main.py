import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog

from lexical import Token, parse

# Global Vairables ===
fileLoaded = False

# ====================

# Color ======
bgcolor1 = "#C9E4DE"
bgcolor2 = "#BDE0FE"
bgcolor3 = "#FFDAC1"
bgcolor4 = "#FFE1E9"
bgcolor5 = "#55CBCD"
# ============

# Font =======
defaultFont = ("Microsoft YaHei UI", 8, "normal")
labelFont = ("Microsoft YaHei UI", 8, "bold") 
texteditorFont = ("Courier New", 10, "normal") 
# ============

# GUI Functions ===============
# Events
def on_resize(event):
    width = root.winfo_width()
    height = root.winfo_height()
    topFrame.configure(width=width, height=height // 2)
    bottomFrame.configure(width=width, height=height // 2)

        
def insert_spaces(event):
    textEditor.insert(tk.INSERT, " " * 4)
    return 'break'

# Program Functions
def open_file():
    global fileLoaded
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Lolcode files", "*.lol"), ("All files", "*.*")])
    if file_path:
        fileLoaded = True
        filepathText.config(state=tk.NORMAL)
        filepathText.delete("1.0","end")
        filepathText.insert(tk.END, file_path)
        filepathText.config(state=tk.DISABLED)
        read_file_lexical(file_path)
        
def read_file_lexical(file_path):
    tokens = parse(file_path)
    print(tokens)
    for token in tokens:
        lexemeTable.insert("", "end", values=(token.tokenvalue, token.tokentype))

def execute_code():
    pass

# =============================


root = tk.Tk()
root.title("The Lords of the Strings LOLCODE Interpreter")
root.geometry('1300x700')
root.minsize(1300,700)

font.nametofont("TkDefaultFont").configure(family=defaultFont[0], size=defaultFont[1])

topFrame = tk.Frame(root, bg=bgcolor1)
bottomFrame = tk.Frame(root, bg=bgcolor4)

# Top Frame =====
# Text Editor
textEditorFrame = tk.Frame(topFrame, width=400,bg=bgcolor1)
openfileUI = tk.Frame(textEditorFrame)
filepathText = tk.Text(openfileUI, height = 1, width=54)
openfileButton = tk.Button(openfileUI, text="Open", command=open_file)
filepathText.configure(state=tk.DISABLED)

textEditFrame = tk.Frame(textEditorFrame)
textEditor = tk.Text(textEditFrame, height = 10, width = 60, wrap='none', font=texteditorFont)

textEditorvsb = ttk.Scrollbar(textEditFrame, orient="vertical", command=textEditor.yview)
textEditor.configure(yscrollcommand=textEditorvsb.set)
textEditorvsb.pack(side=tk.RIGHT, fill=tk.Y)

textEditorhsb = ttk.Scrollbar(textEditFrame, orient="horizontal", command=textEditor.xview)
textEditor.configure(xscrollcommand=textEditorhsb.set)
textEditorhsb.pack(side=tk.BOTTOM, fill=tk.X)

openfileButton.pack(side=tk.RIGHT, fill=tk.X, expand=False)
filepathText.pack(side=tk.RIGHT, fill=tk.X, expand=True)
openfileUI.pack(side=tk.TOP, fill=tk.X, expand=False)
textEditor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

textEditFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
textEditorFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Lexemes Table
lexemeFrame = tk.Frame(topFrame, width=300, bg=bgcolor3)
lexemeTableLabel = tk.Label(lexemeFrame, text="Lexeme Table", bg=bgcolor3, font=labelFont)

lexemeTableFrame = tk.Frame(lexemeFrame, width=300, bg=bgcolor3)

lexemeTable = ttk.Treeview(lexemeTableFrame, columns=("lexeme", "classification"), show='headings')
lexemeTable.heading("lexeme", text="Lexeme")
lexemeTable.heading("classification", text="Classification")

lexemevsb = ttk.Scrollbar(lexemeTableFrame, orient="vertical", command=lexemeTable.yview)
lexemeTable.configure(yscrollcommand=lexemevsb.set)
lexemevsb.pack(side=tk.RIGHT, fill=tk.Y)

lexemeTableLabel.pack(side=tk.TOP)
lexemeTable.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
lexemeTableFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

lexemeFrame.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

# Symbol Table
symbolFrame = tk.Frame(topFrame, width=300, bg=bgcolor2)
symbolTableLabel = tk.Label(symbolFrame, text="Symbol Table", bg=bgcolor2, font=labelFont)

symbolTableFrame = tk.Frame(symbolFrame, width=300, bg=bgcolor2)

symbolTable = ttk.Treeview(symbolTableFrame, columns=("identifier", "value"), show='headings')
symbolTable.heading("identifier", text="Identifier")
symbolTable.heading("value", text="Value")

symbolvsb = ttk.Scrollbar(symbolTableFrame, orient="vertical", command=symbolTable.yview)
symbolTable.configure(yscrollcommand=symbolvsb.set)
symbolvsb.pack(side=tk.RIGHT, fill=tk.Y)

symbolTableLabel.pack(side=tk.TOP)
symbolTable.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
symbolTableFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

symbolFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# ===============

# Bottom Frame ==
executeButton = tk.Button(bottomFrame, text="EXECUTE", font=labelFont, command=execute_code)
executeButton.pack(side=tk.TOP, fill=tk.X)

outputFrame = tk.Frame(bottomFrame, bg=bgcolor4)
outputText = tk.Text(outputFrame, height = 10, width = 60, wrap='none', font=texteditorFont)

outputTextvsb = ttk.Scrollbar(outputFrame, orient="vertical", command=outputText.yview)
outputText.configure(yscrollcommand=outputTextvsb.set)
outputTextvsb.pack(side=tk.RIGHT, fill=tk.Y)

outputTexthsb = ttk.Scrollbar(outputFrame, orient="horizontal", command=outputText.xview)
outputText.configure(xscrollcommand=outputTexthsb.set)
outputTexthsb.pack(side=tk.BOTTOM, fill=tk.X)

outputText.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
outputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
outputText.configure(state=tk.DISABLED)
# ===============

topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# Event Binds
textEditor.bind("<Tab>", insert_spaces)
root.bind('<Configure>', on_resize) 

# print(font.families())
root.mainloop()
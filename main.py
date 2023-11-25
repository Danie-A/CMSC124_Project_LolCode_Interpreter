import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Color ======
bgcolor1 = "#C9E4DE"
bgcolor2 = "#BDE0FE"
# ============

def on_resize(event):
    width = root.winfo_width()
    height = root.winfo_height()

    # Configure the frames to expand with the window
    topFrame.configure(width=width, height=height // 2)
    bottomFrame.configure(width=width, height=height // 2)
    
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_label.config(text=file_path)

root = tk.Tk()
root.title("The Lords of the Strings Lexical Analyzer")
root.geometry('1300x700')
root.minsize(1300,700)

topFrame = tk.Frame(root, bg=bgcolor1)
bottomFrame = tk.Frame(root,)

# Top Frame =====
# Text Editor
textEditorFrame = tk.Frame(topFrame, width=root.winfo_width() ,bg=bgcolor2)
openfileUI = tk.Frame(textEditorFrame, height)


# ===============

topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



root.bind('<Configure>', on_resize) 
root.mainloop()
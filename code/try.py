# line = "   \t\n"
# result = line.strip()

# if result:
#     print("Line has content")
# else:
#     print("Line is empty or contains only whitespace characters")

# print(str("sleighulet ") + ' sleigh')

# import tkinter as tk

# def update_line_numbers(event=None):
#     line_numbers.delete('1.0', 'end')
#     num_lines = outputText.index('end - 1 line').split('.')[0]
#     line_numbers.insert('1.0', '\n'.join(str(i) for i in range(1, int(num_lines) + 1)))

# root = tk.Tk()

# line_numbers = tk.Text(root, width=4, padx=3, takefocus=0, border=0, background='khaki', state='disabled', wrap='none')
# line_numbers.pack(side='left', fill='y')

# outputText = tk.Text(root, wrap='word')
# outputText.pack(side='right', fill='both', expand=True)

# outputText.bind('<Any-KeyPress>', update_line_numbers)
# outputText.bind('<Any-KeyRelease>', update_line_numbers)

# root.mainloop()

# var = input("inputsmth: ")
# print("input is: ["+var+"]")

# num = ("a", "b", "c", 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
# print("numis ", num[1])

# ans = True
# if ans == True and ans != 1:
#     print("true")
# if ans == True:
#     print("true na yarn")
# elif ans == False and ans != 0:
#     print("false")
# else:
#     print("hala ka")

# ans = True + False
# print(ans)
# a = None
# print(str(a)+"b")

# a = 1.0
# if (a==True):
#     print("true")
# else: print("false")

# a = False and False
# print(a)

# print(None)
# def eme():
#     print("eme2")
# def eme():
#     print("eme")


# x = 5.0
# y = 5
# print(x==y)

# line = ""
# print("line is: [",line.strip(), "]")

new_value = 0
var_value = False
if isinstance(var_value, bool) and var_value == True:
    new_value = "WIN"
elif isinstance(var_value, bool) and var_value == False:
    new_value = "FAIL"

print("new value is ", new_value)

import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("280x360")  
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), borderwidth=3, relief="ridge", justify="right")
entry.pack(fill=tk.X, ipady=8, padx=4, pady=4)  # ipady kam kiya

frame = tk.Frame(root)
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == '=':
            cmd = calculate
        else:
            cmd = lambda x=btn: click_button(x)
        # Button size aur padding kam
        tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 13),fg="black", 
                  command=cmd).grid(row=i, column=j, padx=3, pady=3)

tk.Button(root, text="Clear", width=18, height=1, font=("Arial", 11), 
          command=clear).pack(pady=6)

root.mainloop()
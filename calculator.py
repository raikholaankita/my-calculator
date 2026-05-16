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
root.geometry("320x550")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

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
        tk.Button(frame, text=btn, width=6, height=3, font=("Arial", 14), command=cmd).grid(row=i, column=j, padx=5, pady=5)

tk.Button(root, text="Clear", width=20, height=2, font=("Arial", 12), command=clear).pack(pady=15)

root.mainloop()
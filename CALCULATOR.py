import tkinter as tk
import tkinter.font as font
import math
def calculate(event):
    button = event.widget.cget("text")
    global inp
    try:
        if button == "c": inp.set("") #Clears the input
        elif button == "<-": inp.set(inp.get()[:-1]) #removes the last character from the input.
        elif button == "=": inp.set(eval(inp.get()))
        elif button == u"\u221A": inp.set(math.sqrt(float(inp.get())))
        elif button == "log": inp.set(math.log(float(inp.get())))
        elif button == "sin": inp.set(math.sin(math.radians(float(inp.get()))))
        elif button == "cos": inp.set(math.cos(math.radians(float(inp.get()))))
        elif button == "tan": inp.set(math.tan(math.radians(float(inp.get()))))
        elif button == "x^2": inp.set(float(inp.get()) ** 2)
        elif button == "1/x": inp.set(1 / float(inp.get()))
        elif button == "e": inp.set(math.exp(float(inp.get())))
        else: inp.set(inp.get() + str(button))
    except Exception as e:
        inp.set("Error: " + str(e))
root = tk.Tk()
root.geometry("380x480")
root.title("Calculator")
root.resizable(1,1)
inp = tk.StringVar()
screen = tk.Entry(root, text=inp, width=30, justify='right', font=font.Font(size=15), bd=6)
screen.grid(row=0, column=0, columnspan=4, padx=15, pady=15, ipady=5)
buttons = [
    "c", "<-", u"\u221A", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "(", "0", ")", "=",
    "sin", "cos", "tan", "x^2",
    "1/x", "log", ".", "e"
]
for i, button_text in enumerate(buttons):
    btn = tk.Button(root, bd=1, text=button_text, font=font.Font(size=15))
    btn.grid(row=i // 4 + 1, column=i % 4, padx=15, pady=5, ipadx=5, ipady=5)
    btn.bind('<Button-1>', calculate)
    if button_text.isdigit() or button_text in ["+", "-", "*", "/", "(", ")", "."]:
        btn.configure(bg="sky blue", fg="white")
root.mainloop()

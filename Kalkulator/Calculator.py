"""
Kalkulator standardowy i naukowy
"""


from tkinter import *
import tkinter.messagebox
import standard, scientific


root = Tk()
root.title("Kalkulator")
root.resizable(width=True, height=True)
root.geometry("400x400")

app = Frame(root)
app.grid()

title = Label(app, text="Kalkulator", font=("arial", 20, "bold"))
title.grid(row=0, column=1, sticky=W, pady=30)

lbl = Label(app, text="Wybierz rodzaj kalkulatora z górnego menu.", font=("arial", 12), width=42)
lbl.grid(row=1, column=0, columnspan=2, sticky=W)


def iExit():
    iExit = tkinter.messagebox.askyesno("Kalkulator", "Czy na pewno chcesz wyjść?")
    if iExit > 0:
        root.destroy()
        return

def Standard():
    root1 = Tk()
    root1.resizable(width=True, height=True)
    standard.Calculator(root1)
    root1.geometry("300x320")
    root1.title("Kalkulator standardowy")
    app1 = Frame(root1)
    app1.grid()
    root1.mainloop()

def Scientific():
    root1 = Tk()
    root1.resizable(width=True, height=True)
    scientific.Calculator(root1)
    root1.geometry("768x532")
    root1.title("Kalkulator naukowy")
    app1 = Frame(root1)
    app1.grid()
    root1.mainloop()


menubar = Menu(app)
# Menu wyboru
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Rodzaj kalkulatora", menu=filemenu)
filemenu.add_command(label="Standardowy", command=Standard)
filemenu.add_command(label="Naukowy", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

# Menu pomocy
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Pomoc", menu=helpmenu)
helpmenu.add_command(label="Pokaż pomoc")

root.config(menu=menubar)
root.mainloop()
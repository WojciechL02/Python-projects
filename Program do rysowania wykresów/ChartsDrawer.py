from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math as mt


class Application(Frame):
    """Program do rysowania wykresów."""
    def __init__(self, master):
        """Inicjalizacja ramki."""
        super(Application, self).__init__(master)
        self.grid()
        self.widgets()

    def widgets(self):
        """Widżety"""
        # etykieta tytułowa
        self.title_lbl = Label(self, width=30, font=("Goudy Stout", 20), text="Charts Drawer 2D", pady=20)
        self.title_lbl.grid(row=1, column=0, columnspan=3)

        # pole tekstowe Entry
        self.pt_ent = Entry(self, font=("Century", 12), justify=CENTER)
        self.pt_ent.grid(row=2, column=1)

        # informacje dla użytkownika
        self.inf_field = Label(self, font=('Century', 12), text="abs(x) - wartość bezwzględna\n"
                                                              "x^ - potęgowanie\n"
                                                              "sin(x), cos(x) - funkcje trygonometryczne\n"
                                                                "p - liczba pi", padx=10, pady=10, bg="white", relief=RIDGE, borderwidth=5)
        self.inf_field.grid(row=4, column=1, pady=10)

        # przycisk rysowania
        self.bttn1 = Button(self, text="RYSUJ!", font=("Century", 12), command=self.matplotCanvas, pady=10)
        self.bttn1.grid(row=5, column=1)

        # przycisk zapisywania
        self.save_bttn = Button(self, text="Zapisz", font=("Century", 12), padx=7, pady=10, command=self.save)
        self.save_bttn.grid(row=5, column=1, sticky=E)

    def matplotCanvas(self):
        f = Figure(figsize=(9, 5.5), dpi=80)
        plt.style.use('fivethirtyeight')
        x = np.arange(int(przedzial(self.pt_ent.get())[0]), int(przedzial(self.pt_ent.get())[1]), 0.00001)
        y = eval(wzor_funkcji(self.pt_ent.get()))
        f.add_subplot(111, title=self.pt_ent.get(), xlabel="oś x", ylabel="oś y").plot(x, y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().grid(row=6, column=0, columnspan=3, pady=15)

    def save(self):
        f = Figure(figsize=(10, 7), dpi=80)
        plt.style.use('fivethirtyeight')
        x = np.arange(int(przedzial(self.pt_ent.get())[0]), int(przedzial(self.pt_ent.get())[1]), 0.00001)
        y = eval(wzor_funkcji(self.pt_ent.get()))
        f.add_subplot(111, title=self.pt_ent.get(), xlabel="oś x", ylabel="oś y").plot(x, y)
        extent = f.get_window_extent().transformed(f.dpi_scale_trans.inverted())
        f.savefig("wykres.png", bbox_inches=extent)


def wzor_funkcji(n):
    tekst = ""
    i = 0
    while i < len(n):
        if n[i] == "p":
            tekst += "np.pi"
            i += 1
        elif n[i] == "s" and i != 0 and n[i - 1] != "b":
            tekst += "np.sin"
            i += 3
        elif n[i] == "s" and i == 0:
            tekst += "np.sin"
            i += 3
        elif n[i] == "c":
            tekst += "np.cos"
            i += 3
        elif n[i] == "^":
            tekst += "**"
            i += 1
        else:
            tekst += n[i]
            i += 1
    return tekst


def przedzial(n):
    p = -8
    k = 8
    if ")*(" in n:
        p = -100
        k = 100
    return p, k


# main
root = Tk()
root.title("ChartsDrawer")
root.geometry("1000x760")

app = Application(root)

root.mainloop()

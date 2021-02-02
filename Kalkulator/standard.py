"""
Moduł kalkulatora prostego
"""

from tkinter import *
import math as m


class Calculator(Frame):
    """Kalkulator"""
    def __init__(self, master):
        """Okno kalkulatora"""
        super(Calculator, self).__init__(master)
        self.grid()
        self.widgets()

    def widgets(self):
        """Przyciski"""
        # pole tekstowe Entry
        self.entry = Entry(self, font=("arial", 20), width=18, relief=SUNKEN, borderwidth=8, justify=RIGHT)
        self.entry.grid(row=0, column=0, columnspan=5, padx=2, pady=5, sticky=N)

    # PIERWSZY WIERSZ #
        # przycisk 7
        self.bttn7 = Button(self, text="7", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(7))
        self.bttn7.grid(row=1, column=0)
        # przycisk 8
        self.bttn8 = Button(self, text="8", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(8))
        self.bttn8.grid(row=1, column=1)
        # przycisk 9
        self.bttn9 = Button(self, text="9", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(9))
        self.bttn9.grid(row=1, column=2)
        # przycisk pierwiastka
        self.bttn_sqrt = Button(self, text="√", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                                command=self.pierwiastek)
        self.bttn_sqrt.grid(row=1, column=3)
        # przycisk C
        self.bttn_clear = Button(self, text="C", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            bg="#A52A2A", command=self.clear)
        self.bttn_clear.grid(row=1, column=4)
    # DRUGI WIERSZ #
        # przycisk 4
        self.bttn4 = Button(self, text="4", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(4))
        self.bttn4.grid(row=2, column=0)
        # przycisk 5
        self.bttn5 = Button(self, text="5", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(5))
        self.bttn5.grid(row=2, column=1)
        # przycisk 6
        self.bttn6 = Button(self, text="6", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(6))
        self.bttn6.grid(row=2, column=2)
        # przycisk -
        self.bttn_minus = Button(self, text="-", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                                 command=lambda: self.click("-"))
        self.bttn_minus.grid(row=2, column=3)
        # przycisk /
        self.bttn_dziel = Button(self, text="/", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click("/"))
        self.bttn_dziel.grid(row=2, column=4)
    # TRZECI WIERSZ #
        # przycisk 1
        self.bttn1 = Button(self, text="1", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(1))
        self.bttn1.grid(row=3, column=0)
        # przycisk 2
        self.bttn2 = Button(self, text="2", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(2))
        self.bttn2.grid(row=3, column=1)
        # przycisk 3
        self.bttn3 = Button(self, text="3", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(3))
        self.bttn3.grid(row=3, column=2)
        # przycisk +
        self.bttn_plus = Button(self, text="+", font=("arial", 18), width=3, height=3, relief=RAISED, borderwidth=6,
                                command=lambda: self.click("+"))
        self.bttn_plus.grid(row=3, rowspan=2, column=3)
        # przycisk x
        self.bttn_x = Button(self, text="x", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click("x"))
        self.bttn_x.grid(row=3, column=4)
    # CZWARTY WIERSZ #
        # przycisk +/-
        self.bttn_change = Button(self, text="+/-", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=self.change)
        self.bttn_change.grid(row=4, column=0)
        # przycisk 0
        self.bttn0 = Button(self, text="0", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click(0))
        self.bttn0.grid(row=4, column=1)
        # przycisk ,
        self.bttn_float = Button(self, text=",", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                            command=lambda: self.click("."))
        self.bttn_float.grid(row=4, column=2)
        # przycisk =
        self.bttn_equal = Button(self, text="=", font=("arial", 18), width=3, relief=RAISED, borderwidth=6,
                                 command=self.equal)
        self.bttn_equal.grid(row=4, column=4)

    def click(self, number):
        l = len(self.entry.get())
        self.entry.insert(l, number)

    def clear(self):
        self.entry.delete(0, END)

    def equal(self):
        a = self.entry.get()
        if a != "":
            self.entry.delete(0, END)
            b = wynik(a)
            dl = len(b) - 1
            if len(a) != 1:
                if b[-2] == "/" and b[dl] == "0":
                    c = "ERROR"
                else:
                    c = eval(b)
            else:
                c = a
            self.entry.insert(0, c)

    def pierwiastek(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if float(a) >= 0:
            b = m.sqrt(float(a))
        else:
            b = "ERROR"
        self.entry.insert(0, b)

    def change(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, float(a)*-1)

def wynik(n):
    w = ""
    for z in n:
        if z == "x":
            w += "*"
        else:
            w += z
    return w


if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
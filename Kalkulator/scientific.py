"""
Moduł kalkulatora naukowego
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
        # Pole tekstowe Entry
        self.entry = Entry(self, font=("arial", 24), width=22, bg="black", fg="white", borderwidth=8, relief=SUNKEN,
                           justify=RIGHT)
        self.entry.grid(row=0, column=0, columnspan=5, padx=2, pady=4, sticky=W)

        # etykieta tytułowa
        self.label = Label(self, text="Scientific Calculator", font=("arial", 20), justify=LEFT)
        self.label.grid(row=0, column=5, columnspan=3, pady=5, sticky=W)

    # PIERWSZY WIERSZ #
        # przycisk C
        self.bttn_clear = Button(self, text="C", font=("arial", 20), width=5, height=2, borderwidth=4,
                                 bg="#A52A2A", activebackground="#A52A2A", command=self.clear)
        self.bttn_clear.grid(row=1, column=0, padx=1, pady=1)

        # przycisk pierwiastka
        self.bttn_sqrt = Button(self, text="√", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                borderwidth=4, command=self.pierwiastek)
        self.bttn_sqrt.grid(row=1, column=1, padx=1, pady=1)

        # przycisk silnia
        self.bttn_factorial = Button(self, text="n!", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                     borderwidth=4, command=self.factorial)
        self.bttn_factorial.grid(row=1, column=2, padx=1, pady=1)

        # przycisk +
        self.bttn_plus = Button(self, text="+", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                borderwidth=4, command=lambda: self.click("+"))
        self.bttn_plus.grid(row=1, column=3, padx=1, pady=1)

        # przycisk pi
        self.bttn_pi = Button(self, text="π", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                              borderwidth=4, command=self.pi)
        self.bttn_pi.grid(row=1, column=4, padx=1, pady=1)

        # przycisk sinus
        self.bttn_sin = Button(self, text="sin", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.sinus)
        self.bttn_sin.grid(row=1, column=5, padx=1, pady=1)

        # przycisk cosinus
        self.bttn_cos = Button(self, text="cos", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.cosinus)
        self.bttn_cos.grid(row=1, column=6, padx=1, pady=1)

        # przycisk tangens
        self.bttn_tan = Button(self, text="tan", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.tangens)
        self.bttn_tan.grid(row=1, column=7, padx=1, pady=1)

    # DRUGI WIERSZ #
        # przycisk 7
        self.bttn7 = Button(self, text="7", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(7))
        self.bttn7.grid(row=2, column=0, padx=1, pady=1)

        # przycisk 8
        self.bttn8 = Button(self, text="8", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(8))
        self.bttn8.grid(row=2, column=1, padx=1, pady=1)

        # przycisk 9
        self.bttn9 = Button(self, text="9", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(9))
        self.bttn9.grid(row=2, column=2, padx=1, pady=1)

        # przycisk -
        self.bttn_minus = Button(self, text="-", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                 borderwidth=4, command=lambda: self.click("-"))
        self.bttn_minus.grid(row=2, column=3, padx=1, pady=1)

        # przycisk 2pi
        self.bttn_2pi = Button(self, text="2π", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.two_pi)
        self.bttn_2pi.grid(row=2, column=4, padx=1, pady=1)

        # przycisk sinush
        self.bttn_sinh = Button(self, text="sinh", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                borderwidth=4, command=self.sinush)
        self.bttn_sinh.grid(row=2, column=5, padx=1, pady=1)

        # przycisk cosinush
        self.bttn_cosh = Button(self, text="cosh", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                borderwidth=4, command=self.cosinush)
        self.bttn_cosh.grid(row=2, column=6, padx=1, pady=1)

        # przycisk tangensh
        self.bttn_tanh = Button(self, text="tanh", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                borderwidth=4, command=self.tangensh)
        self.bttn_tanh.grid(row=2, column=7, padx=1, pady=1)

    # TRZECI WIERSZ #
        # przycisk 4
        self.bttn4 = Button(self, text="4", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(4))
        self.bttn4.grid(row=3, column=0, padx=1, pady=1)

        # przycisk 5
        self.bttn5 = Button(self, text="5", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(5))
        self.bttn5.grid(row=3, column=1, padx=1, pady=1)

        # przycisk 6
        self.bttn6 = Button(self, text="6", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(6))
        self.bttn6.grid(row=3, column=2, padx=1, pady=1)

        # przycisk x
        self.bttn_x = Button(self, text="x", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                             borderwidth=4, command=lambda: self.click("x"))
        self.bttn_x.grid(row=3, column=3, padx=1, pady=1)

        # przycisk log
        self.bttn_log = Button(self, text="log", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.log)
        self.bttn_log.grid(row=3, column=4, padx=1, pady=1)

        # przycisk mod
        self.bttn_mod = Button(self, text="mod", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=lambda: self.click("mod"))
        self.bttn_mod.grid(row=3, column=5, padx=1, pady=1)

        # przycisk |x|
        self.bttn_abs = Button(self, text="|x|", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.absolut)
        self.bttn_abs.grid(row=3, column=6, padx=1, pady=1)

        # przycisk e
        self.bttn_e = Button(self, text="e", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                             borderwidth=4, command=self.euler)
        self.bttn_e.grid(row=3, column=7, padx=1, pady=1)

    # CZWARTY WIERSZ #
        # przycisk 1
        self.bttn1 = Button(self, text="1", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(1))
        self.bttn1.grid(row=4, column=0, padx=1, pady=1)

        # przycisk 2
        self.bttn2 = Button(self, text="2", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(2))
        self.bttn2.grid(row=4, column=1, padx=1, pady=1)

        # przycisk 3
        self.bttn3 = Button(self, text="3", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(3))
        self.bttn3.grid(row=4, column=2, padx=1, pady=1)

        # przycisk /
        self.bttn_dziel = Button(self, text="/", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                 borderwidth=4, command=lambda: self.click("/"))
        self.bttn_dziel.grid(row=4, column=3, padx=1, pady=1)

        # przycisk log2
        self.bttn_log2 = Button(self, text="log2", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                borderwidth=4, command=self.log2)
        self.bttn_log2.grid(row=4, column=4, padx=1, pady=1)

        # przycisk exp
        self.bttn_exp = Button(self, text="exp", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.exp)
        self.bttn_exp.grid(row=4, column=5, padx=1, pady=1)

        # przycisk 2^x
        self.bttn_power2 = Button(self, text="2^x", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                  borderwidth=4, command=self.power2_x)
        self.bttn_power2.grid(row=4, column=6, padx=1, pady=1)

        # przycisk rad
        self.bttn_rad = Button(self, text="rad", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                               borderwidth=4, command=self.rad)
        self.bttn_rad.grid(row=4, column=7, padx=1, pady=1)

    # PIĄTY WIERSZ #
        # przycisk 0
        self.bttn0 = Button(self, text="0", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                            borderwidth=4, command=lambda: self.click(0))
        self.bttn0.grid(row=5, column=0, padx=1, pady=1)

        # przycisk ,
        self.bttn_float = Button(self, text=",", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                 borderwidth=4, command=lambda: self.click("."))
        self.bttn_float.grid(row=5, column=1, padx=1, pady=1)

        # przycisk +/-
        self.bttn_change = Button(self, text="+/-", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                  borderwidth=4, command=self.change)
        self.bttn_change.grid(row=5, column=2, padx=1, pady=1)

        # przycisk =
        self.bttn_equal = Button(self, text="=", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                 borderwidth=4, command=self.equal)
        self.bttn_equal.grid(row=5, column=3, padx=1, pady=1)

        # przycisk log10
        self.bttn_log10 = Button(self, text="log10", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                 borderwidth=4, command=self.log10)
        self.bttn_log10.grid(row=5, column=4, padx=1, pady=1)

        # przycisk x^2
        self.bttn_xpower = Button(self, text="x^2", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                  borderwidth=4, command=self.x_power_2)
        self.bttn_xpower.grid(row=5, column=5, padx=1, pady=1)

        # przycisk x^y
        self.bttn_power = Button(self, text="x^y", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                 borderwidth=4, command=lambda: self.click("^"))
        self.bttn_power.grid(row=5, column=6, padx=1, pady=1)

        # przycisk 10^x
        self.bttn_power10 = Button(self, text="10^x", font=("arial", 20), width=5, height=2, bg="black", fg="white",
                                   borderwidth=4, command=self.power10)
        self.bttn_power10.grid(row=5, column=7, padx=1, pady=1)


    def click(self, number):
        l = len(self.entry.get())
        self.entry.insert(l, number)

    def clear(self):
        self.entry.delete(0, END)

    def equal(self):
        a = self.entry.get()
        if a == "mod":
            self.entry.delete(0, END)
        elif a != "":
            self.entry.delete(0, END)
            b = wynik(a)
            if b == "ERROR":
                c = "ERROR"
            else:
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

    def factorial(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            if "." in a:
                b = "ERROR"
            else:
                if float(a) >= 0:
                    b = m.factorial(float(a))
                else:
                    b = "ERROR"
        else:
            b = ""
        self.entry.insert(0, b)

    def pi(self):
        self.entry.delete(0, END)
        self.entry.insert(0, m.pi)

    def two_pi(self):
        self.entry.delete(0, END)
        self.entry.insert(0, 2 * m.pi)

    def absolut(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            self.entry.insert(0, abs(float(a)))

    def euler(self):
        self.entry.delete(0, END)
        self.entry.insert(0, m.e)

    def log(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            if float(a) > 0:
                b = m.log(float(a))
                self.entry.insert(0, b)
            else:
                b = "ERROR"
                self.entry.insert(0, b)

    def log2(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            if float(a) > 0:
                b = m.log2(float(a))
                self.entry.insert(0, b)
            else:
                b = "ERROR"
                self.entry.insert(0, b)

    def log10(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            if float(a) > 0:
                b = m.log10(float(a))
                self.entry.insert(0, b)
            else:
                b = "ERROR"
                self.entry.insert(0, b)

    def exp(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, m.exp(float(a)))

    def rad(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, m.radians(float(a)))

    def x_power_2(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            b = float(a)**2
            self.entry.insert(0, b)

    def power10(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            b = 10**float(a)
            self.entry.insert(0, b)

    def power2_x(self):
        a = self.entry.get()
        self.entry.delete(0, END)
        if a != "" and a != ".":
            b = 2**float(a)
            self.entry.insert(0, b)

    def sinus(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, round(m.sin(float(a)), 15))

    def cosinus(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, round(m.cos(float(a)), 15))

    def tangens(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, round(m.tan(float(a)), 15))

    def sinush(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, round(m.sinh(float(a)), 14))

    def cosinush(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, round(m.cosh(float(a)), 14))

    def tangensh(self):
        a = self.entry.get()
        if a != "" and a != ".":
            self.entry.delete(0, END)
            self.entry.insert(0, round(m.tanh(float(a)), 14))


def wynik(n):
    w = ""
    i = 0
    while i < len(n):
        if n[i] == "x":
            w += "*"
        elif n[i] == "^":
            if n[i-1] == "0" and n[i+1] == "0":
                w = "ERROR"
                return w
            else:
                w += "**"
        elif n[i] == "m":
            w += "%"
            i += 2
        elif n[i] == "o" or n[i] == "d":
            continue
        else:
            w += n[i]
        i += 1
    return w


if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
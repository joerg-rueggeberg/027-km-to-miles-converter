from tkinter import *

window = Tk()
window.title("KM zu Meilen Umrechner")
# window.minsize(width=185, height=125)
window.config(padx=10, pady=10)


def convert():
    km = entry_km.get()
    mi = round(int(km) * 0.621371, 2)
    meilen_int.config(text=mi)


# Entry
entry_km = Entry(width=7)
entry_km.insert(END, string="0")
entry_km.grid(column=1, row=0)

# Labels
ausgang = Label(text="Ausgangswert:")
ausgang.config(padx=10, pady=10)
ausgang.grid(column=0, row=0)

kilometer = Label(text="Km")
kilometer.config(padx=10, pady=10)
kilometer.grid(column=2, row=0)

ergibt = Label(text="Ergibt:")
ergibt.config(padx=10, pady=10)
ergibt.grid(column=0, row=1)

meilen_int = Label(text="0")
meilen_int.config(padx=10, pady=10)
meilen_int.grid(column=1, row=1)

meilen = Label(text="Meilen")
meilen.config(padx=10, pady=10)
meilen.grid(column=2, row=1)

# Button
berechnen = Button(text="umrechnen", command=convert)
berechnen.config(padx=2, pady=2)
berechnen.grid(column=1, row=2)

window.mainloop()

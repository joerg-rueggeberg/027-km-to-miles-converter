from tkinter import *

window = Tk()
window.title("Jörg - Einheiten Umrechner")
window.minsize(width=350, height=125)
window.config(padx=10, pady=10)


def convert():
    ausgangseinheit_entry = entry_input.get()
    option_chosen = radio_option.get()
    if option_chosen == 1:
        neuer_wert = round(int(ausgangseinheit_entry) * 0.621371, 2)
        neuer_wert_int.config(text=neuer_wert)
    elif option_chosen == 2:
        neuer_wert = round(int(ausgangseinheit_entry) * 3.280839895, 2)
        neuer_wert_int.config(text=neuer_wert)
    elif option_chosen == 3:
        neuer_wert = round(int(ausgangseinheit_entry) * 2, 2)
        neuer_wert_int.config(text=neuer_wert)


def radio_options():
    option_chosen = radio_option.get()
    if option_chosen == 1:
        ausgangseinheit.config(text="Kilometer")
        zieleinheit.config(text="Meilen")
    elif option_chosen == 2:
        ausgangseinheit.config(text="Meter")
        zieleinheit.config(text="Fuß")
    elif option_chosen == 3:
        ausgangseinheit.config(text="Kilogramm")
        zieleinheit.config(text="Pfund")


# Radio
radio_option = IntVar()
radiobutton1 = Radiobutton(text="KM zu Meilen", value=1, variable=radio_option, command=radio_options)
radiobutton2 = Radiobutton(text="Meter zu Fuß", value=2, variable=radio_option, command=radio_options)
radiobutton3 = Radiobutton(text="KG zu Pfund", value=3, variable=radio_option, command=radio_options)
radiobutton1.grid(column=1, row=0, sticky="w")
radiobutton2.grid(column=1, row=1, sticky="w")
radiobutton3.grid(column=1, row=2, sticky="w")

# Entry
entry_input = Entry(width=7)
entry_input.insert(END, string="0")
entry_input.grid(column=1, row=3)

# Labels
was = Label(text="Wähle eine Funktion: ")
was.config(padx=10, pady=10)
was.grid(column=0, row=1)

ausgang = Label(text="Ausgangswert:")
ausgang.config(padx=10, pady=10)
ausgang.grid(column=0, row=3)

ausgangseinheit = Label(text="Kilometer")
ausgangseinheit.config(padx=10, pady=10)
ausgangseinheit.grid(column=2, row=3)

ergibt = Label(text="Ergebnis:")
ergibt.config(padx=10, pady=10)
ergibt.grid(column=0, row=4)

neuer_wert_int = Label(text="0")
neuer_wert_int.config(padx=10, pady=10)
neuer_wert_int.grid(column=1, row=4)

zieleinheit = Label(text="Meilen")
zieleinheit.config(padx=10, pady=10)
zieleinheit.grid(column=2, row=4)

# Button
berechnen = Button(text="umrechnen", command=convert)
berechnen.config(padx=2, pady=2)
berechnen.grid(column=1, row=5)

window.mainloop()

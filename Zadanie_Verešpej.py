import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk  # Na spracovanie a zobrazenie obrázka


# Funkcia na spustenie programu
def spusti_program():
    # Získanie kroku od užívateľa
    krok = simpledialog.askfloat("Parameter", "Zadaj krok (napr. 0.1, 0.5, 1):", minvalue=0.1, maxvalue=10)

    if krok is None:
        return  # Užívateľ stlačil "Cancel"

    # Generovanie náhodných čísel s nastaviteľným krokom
    nahodne_cisla = np.random.uniform(0, 100, 30)  # Generujeme 30 čísel v rozsahu 0-100
    zoradene_cisla = np.sort(nahodne_cisla)
    zaokruhlene_cisla = np.round(zoradene_cisla / krok) * krok  # Zaokrúhlenie na daný krok
    najvacsie_cislo = np.max(zaokruhlene_cisla)

    # Vypis výsledkov do konzoly
    print("Generovane cisla:", nahodne_cisla)
    print("Zoradene cisla:", zoradene_cisla)
    print("Zaokruhlene cisla (s krokom", krok, "):", zaokruhlene_cisla)
    print("Najvacsie cislo:", najvacsie_cislo)

    # Vykreslenie grafu
    plt.plot(zaokruhlene_cisla, marker='o')
    plt.title(f"Graf zaokruhlenych cisel (krok {krok})")
    plt.xlabel("Index")
    plt.ylabel("Hodnota")
    plt.grid(True)
    plt.show()


# Vytvorenie hlavného okna aplikácie
root = tk.Tk()
root.title("Generovanie čísel")

# Nastavenie veľkosti okna
root.geometry("600x500")

# Načítanie a nastavenie obrázka ako pozadie
try:
    # Načítanie obrázka (zmeňte "pozadie.png" na cestu k vášmu obrázku)
    obrazok = Image.open("pozadie.png")
    obrazok = obrazok.resize((600, 500))  # Prispôsobenie veľkosti obrázka
    img = ImageTk.PhotoImage(obrazok)

    # Zobrazenie obrázka na pozadí
    label_pozadie = tk.Label(root, image=img)
    label_pozadie.place(x=0, y=0, relwidth=1, relheight=1)  # Pokrytie celého okna
except FileNotFoundError:
    print("Obrázok 'pozadie.png' nebol nájdený. Uistite sa, že je v rovnakom priečinku ako tento skript.")

# Rámček pre hlavičku (vpravo hore) s čiernym pozadím
frame_hlavicka = tk.Frame(root, padx=10, pady=10, bg="black")  # Zmena pozadia rámu na čiernu
frame_hlavicka.pack(anchor="ne", padx=10, pady=5)

label_program = tk.Label(frame_hlavicka, text="Programovacie techniky", font=("Arial", 12, "bold"), fg="white",
                         bg="black")  # Biele písmo
label_program.pack(anchor="e")

label_meno = tk.Label(frame_hlavicka, text="Peter Verešpej", font=("Arial", 12), fg="white", bg="black")  # Biele písmo
label_meno.pack(anchor="e")

# Druhý rámček: zadanie úlohy s čiernym pozadím
frame_zadanie = tk.Frame(root, padx=10, pady=10, relief="groove", borderwidth=2, bg="black")  # Zmena pozadia na čiernu
frame_zadanie.pack(fill="x", padx=10, pady=5)
uvodny_text = (
    "Zadanie úlohy:\n"
    "Vygenerujte pole 30 náhodných hodnôt desatinných čísel od 0 do 100 s krokom 0.1,\n"
    "zoraďte ich od najmenšieho po najväčšie, zaokrúhlite každé číslo na celé číslo,\n"
    "vypíšte najvyššie číslo, vykreslite graf po zaokrúhlení."
)
label_zadanie = tk.Label(frame_zadanie, text=uvodny_text, justify="left", anchor="w", fg="white",
                         bg="black")  # Biele písmo
label_zadanie.pack()

# Tretí rámček: tlačidlo na spustenie programu s čiernym pozadím
frame_tlacitko = tk.Frame(root, padx=10, pady=10, relief="groove", borderwidth=2, bg="black")  # Zmena pozadia na čiernu
frame_tlacitko.pack(fill="x", padx=10, pady=5)
tlacitko = tk.Button(frame_tlacitko, text="Spusti program", command=spusti_program, fg="white",
                     bg="black")  # Biele písmo, čierne pozadie
tlacitko.pack()

# Spustenie hlavnej slučky
root.mainloop()

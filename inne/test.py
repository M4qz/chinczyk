import tkinter as tk
from tkinter import simpledialog

def choose_piece(pieces, color):
    # Utworzenie głównego okna Tkinter
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno

    # Funkcja wywoływana po kliknięciu przycisku
    def on_button_click(index):
        result.set(index)
        root.destroy()

    # Stworzenie nowego okna dialogowego
    dialog = tk.Toplevel(root)
    dialog.title("Wybór pionka")

    # Etykieta z pytaniem
    label = tk.Label(dialog, text="Którego pionka wybrać?")
    label.pack(pady=10)

    result = tk.IntVar()
    result.set(-1)  # Ustaw domyślną wartość

    # Dodanie przycisków dla każdego pionka w wybranym kolorze
    for index, piece in enumerate(pieces[color]):
        if piece is not None:
            button = tk.Button(dialog, text=f"{piece}", command=lambda i=index: on_button_click(i))
            button.pack(pady=5)

    # Pętla główna Tkinter
    dialog.mainloop()
    return result.get()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LGREEN = (144, 238, 144)
LBLUE = (173, 216, 230)
LYELLOW = (255, 252, 187)
LRED = (255, 192, 203)
GREY=(255,255,230)
CELL_SIZE = 50

# Przykładowe dane
pieces6 = {
    GREEN: [None, None, None, (5,6),(6,3)],
    RED: [None, None, (5,6),(6,3)],
    YELLOW: [(5,6),(6,3), None],
    BLUE: [None, (5,6),(6,3), None, None]
}

# Przykładowe użycie funkcji
color = GREEN  # Kolor pionków do wyboru
index = int(choose_piece(pieces6, color))
print(index)

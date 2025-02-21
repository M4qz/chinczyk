import sys
import pygame
from random import randrange
import tkinter as tk
from tkinter import messagebox

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (155, 103, 60)
CELL_SIZE = 50
BOARD_SIZE = 11

def draw_maze(screen, matrix, cell_size):
    tablica = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    tablica1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    light_grey = (211, 211, 211)
    dark_grey = (169, 169, 169)
    LRED = (255, 192, 203)
    LGREEN = (144, 238, 144)
    LBLUE = (173, 216, 230)
    LYELLOW = (255, 252, 187)


    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 1:
                color = BLACK
            elif matrix[y][x] == 2:
                color = LRED
            elif matrix[y][x] == 3:
                color = LGREEN
            elif matrix[y][x] == 44:
                color = BROWN
            elif matrix[y][x] == 4:
                color = LBLUE
            elif matrix[y][x] == 5:
                color = LYELLOW
            else:
                # tutaj jest robiony efekt szachownicy
                color = light_grey if (x + y) % 2 == 0 else dark_grey

            # prostokat na planszy
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

            # Wyrendeowanie liter szachownicy na dole ekranu
            if 6 <= matrix[y][x] <= 16:
                letter_index = matrix[y][x] - 6
                font = pygame.font.Font(None, cell_size)
                text = font.render(tablica[letter_index], True, BLACK)
                screen.blit(text, (x * cell_size + cell_size // 5, y * cell_size + cell_size // 5.5))

            # Wyrenderowanie liczb (1-11) na szachownicy po prawej czesci ekranu
            elif 17 <= matrix[y][x] <= 27:
                letter_index = 27 - matrix[y][x]
                font = pygame.font.Font(None, cell_size)
                text = font.render(tablica1[letter_index], True, BLACK)
                screen.blit(text, (x * cell_size + cell_size // 5, y * cell_size + cell_size // 5.5))

def draw_pieces_new(licznik_g, licznik_r, licznik_y, licznik_b,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, pieces, cell_size):
 tablica=[]
 for color, position in pieces.items():
     for pos in position:
        if pos and pos == (5, 4):
            index_to_remove = position.index((5, 4))
            position.remove((5, 4))
            matrix[4][5] = 44
            numer_green=1
            licznik_g.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 4 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 3) and   matrix[4][5] == 44:
            index_to_remove = position.index((5, 3))
            position.remove((5, 3))
            matrix[3][5] = 44
            numer_green=2
            licznik_g.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 3 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 2) and   matrix[4][5] == 44 and matrix[3][5] == 44:
            index_to_remove = position.index((5, 2))
            position.remove((5, 2))
            matrix[2][5] = 44
            numer_green=3
            licznik_g.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 2 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 1) and matrix[4][5] == 44 and matrix[3][5] == 44 and matrix[2][5] == 44:
            index_to_remove = position.index((5, 1))
            position.remove((5, 1))
            matrix[1][5] = 44
            numer_green=4
            licznik_g.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 1 * cell_size, cell_size, cell_size))
        elif pos and pos == (4, 5):
            index_to_remove = position.index((4, 5))
            position.remove((4,5))
            matrix[5][4] = 44
            numer_blue=1
            licznik_b.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (4 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (3, 5) and matrix[5][4] == 44:
            index_to_remove = position.index((3, 5))
            position.remove((3,5))
            matrix[5][3] = 44
            numer_blue=2
            licznik_b.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (3 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (2, 5) and matrix[5][4] == 44 and matrix[5][3] == 44:
            index_to_remove = position.index((2, 5))
            position.remove((2,5))
            matrix[5][2] = 44
            numer_blue=3
            licznik_b.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (2 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (1, 5) and matrix[5][4] == 44 and matrix[5][3] == 44 and matrix[5][2] == 44:
            index_to_remove = position.index((1, 5))
            position.remove((1,5))
            matrix[5][1] = 44
            numer_blue=4
            licznik_b.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (1 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 6):
            index_to_remove = position.index((5, 6))
            position.remove((5,6))
            matrix[6][5] = 44
            numer_yellow=1
            licznik_y.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 6 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 7) and matrix[6][5] == 44 :
            index_to_remove = position.index((5, 7))
            position.remove((5,7))
            matrix[7][5] = 44
            numer_yellow=2
            licznik_y.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 7 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 8) and matrix[6][5] == 44 and matrix[7][5] == 44:
            index_to_remove = position.index((5, 8))
            position.remove((5,8))
            matrix[8][5] = 44
            numer_yellow=3
            licznik_y.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 8 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 9) and matrix[6][5] == 44 and matrix[7][5] == 44 and matrix[8][5] == 44:
            index_to_remove = position.index((5, 9))
            position.remove((5,9))
            matrix[9][5] = 44
            numer_yellow=4
            licznik_y.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (5 * cell_size, 9 * cell_size, cell_size, cell_size))
        elif pos and pos == (6, 5):
            index_to_remove = position.index((6, 5))
            position.remove((6,5))
            matrix[5][6] = 44
            numer_red=1
            licznik_r.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (6 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (7, 5) and matrix[5][6] == 44:
            index_to_remove = position.index((7, 5))
            position.remove((7,5))
            matrix[5][7] = 44
            numer_red=2
            licznik_r.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (7 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (8, 5) and matrix[5][6] == 44 and matrix[5][7] == 44:
            index_to_remove = position.index((8, 5))
            position.remove((8,5))
            matrix[5][8] = 44
            numer_red=3
            licznik_r.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (8 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (9, 5) and matrix[5][6] == 44 and matrix[5][7] == 44 and matrix[5][8] == 44:
            index_to_remove = position.index((9,5))
            position.remove((9,5))
            matrix[5][9] = 44
            numer_red=4
            licznik_r.pop(int(index_to_remove))
            pygame.draw.rect(screen, BROWN, (9 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos:
            x, y = pos
            tablica.append((x, y))
            pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)

 set1=list(set(tablica))
 for i in range(len(set1)):
     licznik=tablica.count(set1[i])
     if licznik>1:
         x, y = set1[i]
         font = pygame.font.Font(None, cell_size)
         text = font.render(str(licznik), True, BLACK)
         screen.blit(text, (x * cell_size + cell_size // 3, y * cell_size + cell_size // 5.5))

 return licznik_g, licznik_r, licznik_y, licznik_b, numer_blue, numer_red, numer_green, numer_yellow


def rzutkostka():
    #return randrange(1, 7)
 return 6





def move_piece(pos, roll, path,granica,pieces,kolor,xd):
    if pos is None:
        return path[0],xd
    idx = path.index(pos)
    new_idx = (idx + roll) % len(path)
    if granica==True:
        xd = True if roll == 6 else False
        return pos,xd
    if path[new_idx] in path[-4:] and path[new_idx] in pieces[kolor]:
        xd = True if roll == 6 else False
        return pos,xd
    return path[new_idx],xd

def endgame(matrix, screen, font):
    winner = None
    if matrix[5][4] == 44 and matrix[5][3] == 44 and matrix[5][2] == 44 and matrix[5][1] == 44:
        winner = "Wygral niebieski"
    elif matrix[6][5] == 44 and matrix[7][5] == 44 and matrix[8][5] == 44 and matrix[9][5] == 44:
        winner = "Wygral żółty"
    elif matrix[5][6] == 44 and matrix[5][7] == 44 and matrix[5][8] == 44 and matrix[5][9] == 44:
        winner = "Wygral czerwony"
    elif matrix[4][5] == 44 and matrix[3][5] == 44 and matrix[2][5] == 44 and matrix[1][5] == 44:
        winner = "Wygral zielony"

    if winner:
        screen.fill(BLACK)
        winner_text = font.render(winner, True, WHITE)
        screen.blit(winner_text, (screen.get_width() // 2 - winner_text.get_width() // 2, screen.get_height() // 2 - winner_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)  #pokaz wynik calej gry przez 3 sekundy
        pygame.quit()
        sys.exit()

def number_of_players(screen, font):
    button_color = BLUE
    text_color = WHITE
    hover_color = RED


    button_2_rect = pygame.Rect(50, 150, 300, 60)
    button_3_rect = pygame.Rect(50, 250, 300, 60)
    button_4_rect = pygame.Rect(50, 350, 300, 60)


    button_font = pygame.font.Font(None, 22)
    legend_font = pygame.font.Font(None, 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_2_rect.collidepoint(event.pos):
                    return 2
                if button_3_rect.collidepoint(event.pos):
                    return 3
                if button_4_rect.collidepoint(event.pos):
                    return 4

        screen.fill(BLACK)
        prompt_text = font.render('Podaj liczbe graczy (2-4 graczy):', True, text_color)
        screen.blit(prompt_text, (50, 50))

        mouse_pos = pygame.mouse.get_pos()


        button_texts = [
            ('2 (Zielony i Czerwony)', button_2_rect),
            ('3 (Zielony, Czerwony, Żółty)', button_3_rect),
            ('4 (Wszystkie kolory)', button_4_rect)
        ]

        for text, rect in button_texts:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, hover_color, rect)
            else:
                pygame.draw.rect(screen, button_color, rect)


            button_text = button_font.render(text, True, text_color)


            text_rect = button_text.get_rect(center=rect.center)
            screen.blit(button_text, text_rect)

        opis = [
            "Legenda:",
            "2  oznacza 2 pionki na jednym polu",
            "3  oznacza 3 pionki na jednym polu",
            "4  oznacza 4 pionki na jednym polu", ]
        legend_texts = [
            "Sterowanie:",
            "W: Zielony",
            "D: Czerwony",
            "S: Żółty",
            "A: Niebieski"]

        y_offset = 150
        for text in legend_texts:
            legend_surface = legend_font.render(text, True, WHITE)
            screen.blit(legend_surface, (400, y_offset))
            y_offset += 30
        y_offset = 450
        i=0
        for text in opis:
            if i>0:
             pygame.draw.circle(screen, (255,255,255), (107,y_offset+10),14,1)
            legend_surface = legend_font.render(text, True, WHITE)
            screen.blit(legend_surface, (100, y_offset))
            y_offset += 40
            i+=1

        pygame.display.flip()


def count_none(pieces, color):
    # Sprawdza, czy kolor istnieje w słowniku
    if color in pieces:
        none_count = pieces[color].count(None)
        color_lenght= len(pieces[color])
        try:
            none_index = pieces[color].index(None)
        except ValueError:
            # Jeśli nie ma wartości None, ustawiamy none_index na None
            none_index = None
        return none_count, none_index,color_lenght
    else:
        return 0, None

def remove_duplicates_based_on_color(licznik_g,licznik_y,licznik_b,licznik_r,pieces, reference_color):
    reference_values = set(filter(lambda x: x is not None, pieces[reference_color])) #filtr przeszukiwania tupla pieces6 aby znalezc wartosci nie bedace None dla wskazanego koloru

    # iterujemy przez kolory inne niż wybrany kolor
    for color in pieces:
        if color != reference_color:
            for i in range(len(pieces[color])):
                if pieces[color][i] in reference_values:# jesli jakis kolor ma taka sama wartosc inna niz none to zmieniamy na none
                    pieces[color][i] = None
                    if color==GREEN:
                     licznik_g[i]=0
                    if color==YELLOW:
                     licznik_y[i]=0
                    if color==BLUE:
                     licznik_b[i]=0
                    if color==RED:
                     licznik_r[i]=0
    return pieces ,licznik_g,licznik_y,licznik_b,licznik_r

def pierwsza_funkcja(ilosc_none,path_w,roll,odpowiedz, pieces6, index,licznik_g,kolor):
    if (ilosc_none != 0 and roll == 6):
        if ilosc_none == len(pieces6[kolor]):
            pieces6[kolor][int(index)] = path_w[0]
            licznik_g[int(index)] += roll
            return odpowiedz, pieces6, index,licznik_g
        odpowiedz= ask_question()
        if odpowiedz == 1:
            pieces6[kolor][int(index)] = path_w[0]
            licznik_g[int(index)] += roll
    return odpowiedz, pieces6, index,licznik_g

def druga_funkcja(wybor,ilosc_none,color_lenght,roll,path_w,odpowiedz,pieces6, granicaA, numer_green,licznik_g,kolor,xd):
        if ilosc_none == color_lenght or odpowiedz == 1:
            return odpowiedz, pieces6, granicaA, numer_green,licznik_g,xd
        if licznik_g[int(wybor)] + roll < 50 and numer_green == 0:
            licznik_g[int(wybor)] += roll
        elif licznik_g[int(wybor)] + roll < 49 and numer_green == 1:
            licznik_g[int(wybor)] += roll
        elif licznik_g[int(wybor)] + roll < 48 and numer_green == 2:
            licznik_g[int(wybor)] += roll
        elif licznik_g[int(wybor)] + roll < 47 and numer_green == 3:
            licznik_g[int(wybor)] += roll
        else:
            granicaA = True
        pieces6[kolor][wybor],xd= move_piece(pieces6[kolor][wybor], roll, path_w, granicaA,pieces6,kolor,xd)
        granicaA = False
        return odpowiedz, pieces6, granicaA, numer_green,licznik_g,xd

def display_roll_result(result_window, font, kolor, last_roll, screen, clock):
    if last_roll is not None:
        result_window.fill(WHITE)
        roll_text1 = font.render(f'{kolor}', True, BLACK)
        roll_text2 = font.render(f'kostka : {last_roll}', True, BLACK)
        result_window.blit(roll_text1, (10, 10))
        result_window.blit(roll_text2, (10, 30))
        screen.blit(result_window, (10, 10))

    pygame.display.flip()
    clock.tick(30)

def ask_question():
    root = tk.Tk()
    root.withdraw()

    result = tk.IntVar()
    result.set(-1)

    answer = messagebox.askquestion("Pytanie", "Czy chcesz postawić pionek na planszy?")

    if answer == 'yes':
        result.set(1)
    else:
        result.set(0)

    return result.get()



def choose_piece(pieces, color):
    root = tk.Tk()
    root.withdraw()
    result = tk.IntVar(value=-1, master=root)

    def on_button_click(index):
        result.set(index)
        dialog.quit()
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Wybór pionka")
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() - dialog.winfo_reqwidth()) // 2
    y = (dialog.winfo_screenheight() - dialog.winfo_reqheight()) // 2
    dialog.geometry(f"+{x}+{y}")
    label = tk.Label(dialog, text="Którego pionka wybrać?")
    label.pack(pady=10)

    for index, piece in enumerate(pieces[color]):
        if piece is not None:
            #para koordynatów (x, y)
            x, y = piece[0] + 1, piece[1] + 1  # dopdanie do kordynatow 1 aby bylo od 1 do 11
            letter = chr(ord('A') + x - 1)# zamiana pierwszej wartości na literę alfabetu
            button_text = f"{letter}{y}"
            button = tk.Button(dialog, text=button_text, command=lambda i=index: on_button_click(i))
            button.pack(pady=5)


    dialog.mainloop()

    choice = result.get()
    root.destroy()
    return choice


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))  # rozmiar okna na 12x12 pól(plansza + oznaczenia)
    pygame.display.set_caption('Chińczyk')
    font = pygame.font.Font(None, 36)

    liczba_graczy = number_of_players(screen, font)
    matrix = [
        [0, 0, 0, 0, 1, 1, 3, 0, 0, 0, 0, 27],
        [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 26],
        [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 25],  # plansza
        [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 24],
        [4, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 23],
        [1, 4, 4, 4, 4, 1, 2, 2, 2, 2, 1, 22],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 2, 21],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 20],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 19],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 18],
        [0, 0, 0, 0, 5, 1, 1, 0, 0, 0, 0, 17],
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0]
    ]

    path_w = [(6,0), (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),
              (10,4), (10,5), (10,6), (9,6), (8,6), (7,6), (6,6), (6,7),#sciezka zielonego pionek
              (6,8), (6, 9), (6, 10), (5, 10), (4,10), (4,9), (4,8), (4,7),
              (4,6), (3, 6), (2, 6), (1,6), (0,6), (0, 5), (0,4), (1,4),
              (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(5,1),(5, 2),(5,3),(5,4)]
    path_d = [(10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7),#sciezka czerwonego pionka
              (6,8), (6,9), (6,10), (5,10), (4,10), (4,9), (4,8), (4,7),
              (4,6), (3,6), (2,6), (1,6), (0,6), (0,5), (0,4), (1,4),
              (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(6,0),
              (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),(10,4), (10,5),(9,5),(8,5),(7,5),(6,5)]
    path_s = [(4,10), (4,9), (4,8), (4,7),#sciezka zoltego pionka
              (4,6), (3,6), (2,6), (1,6), (0,6), (0,5), (0,4), (1,4),
              (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(6,0),
              (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),(10,4), (10,5),
              (10,6), (9,6), (8,6), (7,6), (6,6), (6,7),(6,8), (6,9), (6,10), (5,10),(5,9),(5,8),(5,7),(5,6)]
    path_a = [(0,4), (1,4),(2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(6,0),
              (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),(10,4), (10,5),
              (10,6), (9,6), (8,6), (7,6), (6,6), (6,7),(6,8), (6,9), (6,10),#sciezka niebieskiego pionka
              (5,10),(4,10), (4,9), (4,8), (4,7),(4,6), (3,6), (2,6), (1,6), (0,6), (0,5),(1,5),(2,5),(3,5),(4,5)]

    pieces6 = {
        GREEN:[None, None, None, None], # Adjusted positions # miejsce na kordy pionkow
        RED: [None, None, None, None],
        YELLOW: [None, None, None, None],
        BLUE: [None, None, None, None]
    }

    last_roll = None
    running = True

    clock = pygame.time.Clock()
    result_window = pygame.Surface((150, 50))
    result_window.fill(WHITE)

    player=0
    numer_blue=0
    numer_yellow=0
    numer_green=0
    numer_red=0
    granicaA=False #granica czy pionek zrobi za duzo krokow
    granicaB=False
    granicaC=False
    granicaD=False
    licznik_g = [0,0,0,0] #tablica licznikow pionkow
    licznik_r=[0,0,0,0]
    licznik_y=[0,0,0,0]
    licznik_b=[0,0,0,0]
    guzik=0
    ileszostek=0
    stop_round=False

    while running:
        odpowiedz = int(3)
        button_processed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not button_processed:
                if event.key == pygame.K_w:
                    guzik = 1
                    button_processed = True
                elif event.key == pygame.K_d:
                    guzik = 2
                    button_processed = True
                elif event.key == pygame.K_s:
                    guzik = 3
                    button_processed = True
                elif event.key == pygame.K_a:
                    guzik = 4
                    button_processed = True

        if guzik == 1 and player % liczba_graczy == 0:
            if stop_round:
                player += 1
                ileszostek = 0
                stop_round=False
                continue
            roll = rzutkostka()
            if roll == 6 and liczba_graczy != 3 and ileszostek < 1:
                player += 4
                ileszostek += 1
            elif liczba_graczy == 3 and roll == 6 and ileszostek <1:
                player += 3
                ileszostek += 1
            else:
                player += 1
                ileszostek = 0
            kolor = 'Zielona'
            last_roll = roll
            display_roll_result(result_window, font, kolor, last_roll, screen, clock)
            ilosc_none, index, color_lenght = count_none(pieces6, GREEN)
            odpowiedz, pieces6, index, licznik_g = pierwsza_funkcja(ilosc_none, path_w, roll, odpowiedz, pieces6, index,
                                                                    licznik_g, GREEN)
            if odpowiedz != 1 and ilosc_none != color_lenght:
                wybor = int(choose_piece(pieces6, GREEN))
                odpowiedz, pieces6, granicaA, numer_green, licznik_g,stop_round = druga_funkcja(wybor, ilosc_none, color_lenght,
                                                                                     roll, path_w, odpowiedz, pieces6,
                                                                                     granicaA, numer_green, licznik_g,
                                                                                     GREEN,stop_round)
                pieces6, licznik_g, licznik_y, licznik_b, licznik_r = remove_duplicates_based_on_color(licznik_g,
                                                                                                       licznik_y,
                                                                                                       licznik_b,
                                                                                                       licznik_r,
                                                                                                       pieces6, GREEN)

        if guzik == 2 and player % liczba_graczy == 1:
            if stop_round:
                player += 1
                ileszostek = 0
                stop_round=False
                continue
            roll = rzutkostka()
            if roll == 6 and liczba_graczy != 3 and ileszostek <1:
                player += 4
                ileszostek += 1
            elif liczba_graczy == 3 and roll == 6 and ileszostek < 1:
                player += 3
                ileszostek += 1
            else:
                player += 1
                ileszostek = 0
            kolor = 'Czerwona'
            last_roll = roll
            display_roll_result(result_window, font, kolor, last_roll, screen, clock)
            ilosc_none, index, color_lenght = count_none(pieces6, RED)
            odpowiedz, pieces6, index, licznik_r = pierwsza_funkcja(ilosc_none, path_d, roll, odpowiedz, pieces6, index,
                                                                    licznik_r, RED)
            if odpowiedz != 1 and ilosc_none != color_lenght:
                wybor = int(choose_piece(pieces6, RED))
                odpowiedz, pieces6, granicaB, numer_red, licznik_r,stop_round = druga_funkcja(wybor, ilosc_none, color_lenght,
                                                                                   roll, path_d, odpowiedz, pieces6,
                                                                                   granicaB, numer_red, licznik_r, RED,stop_round)
                pieces6, licznik_g, licznik_y, licznik_b, licznik_r = remove_duplicates_based_on_color(licznik_g,
                                                                                                       licznik_y,
                                                                                                       licznik_b,
                                                                                                       licznik_r,
                                                                                                       pieces6, RED)

        if guzik == 3 and player % liczba_graczy == 2:
            if stop_round:
                player += 1
                ileszostek = 0
                stop_round=False
                continue
            roll = rzutkostka()
            if roll == 6 and liczba_graczy != 3 and ileszostek < 1:
                player += 4
                ileszostek += 1
            elif liczba_graczy == 3 and roll == 6 and ileszostek < 1:
                player += 3
                ileszostek += 1
            else:
                player += 1
                ileszostek = 0
            kolor = 'Żółta'
            last_roll = roll
            display_roll_result(result_window, font, kolor, last_roll, screen, clock)
            ilosc_none, index, color_lenght = count_none(pieces6, YELLOW)
            odpowiedz, pieces6, index, licznik_y = pierwsza_funkcja(ilosc_none, path_s, roll, odpowiedz, pieces6, index,
                                                                    licznik_y, YELLOW)
            if odpowiedz != 1 and ilosc_none != color_lenght:
                wybor = int(choose_piece(pieces6, YELLOW))
                odpowiedz, pieces6, granicaC, numer_yellow, licznik_y,stop_round = druga_funkcja(wybor, ilosc_none, color_lenght,
                                                                                      roll, path_s, odpowiedz, pieces6,
                                                                                      granicaC, numer_yellow, licznik_y,
                                                                                      YELLOW,stop_round)
                pieces6, licznik_g, licznik_y, licznik_b, licznik_r = remove_duplicates_based_on_color(licznik_g,
                                                                                                       licznik_y,
                                                                                                       licznik_b,
                                                                                                       licznik_r,
                                                                                                       pieces6, YELLOW)

        if guzik == 4 and player % liczba_graczy == 3:
            if stop_round:
                player += 1
                ileszostek = 0
                stop_round=False
                continue
            roll = rzutkostka()
            if roll == 6 and liczba_graczy != 3  and ileszostek<1:
                player += 4
                ileszostek+=1
            elif liczba_graczy == 3 and roll == 6 and ileszostek<1:
                player += 3
                ileszostek += 1
            else:
                player += 1
                ileszostek = 0
            kolor = 'Niebieska'
            last_roll = roll
            display_roll_result(result_window, font, kolor, last_roll, screen, clock)
            ilosc_none, index, color_lenght = count_none(pieces6, BLUE)
            odpowiedz, pieces6, index, licznik_b = pierwsza_funkcja(ilosc_none, path_a, roll, odpowiedz, pieces6, index,
                                                                    licznik_b, BLUE)
            if odpowiedz != 1 and ilosc_none != color_lenght:
                wybor = int(choose_piece(pieces6, BLUE))
                odpowiedz, pieces6, granicaD, numer_blue, licznik_b,stop_round = druga_funkcja(wybor, ilosc_none, color_lenght,
                                                                                    roll, path_a, odpowiedz, pieces6,
                                                                                    granicaD, numer_blue, licznik_b,
                                                                                    BLUE,stop_round)
                pieces6, licznik_g, licznik_y, licznik_b, licznik_r = remove_duplicates_based_on_color(licznik_g,
                                                                                                       licznik_y,
                                                                                                       licznik_b,
                                                                                                       licznik_r,
                                                                                                       pieces6, BLUE)

        screen.fill(BLACK)
        draw_maze(screen, matrix, CELL_SIZE)
        for i in range (4):
         licznik_g, licznik_r, licznik_y, licznik_b, numer_blue, numer_red, numer_green, numer_yellow = draw_pieces_new(
            licznik_g, licznik_r, licznik_y, licznik_b, numer_blue, numer_red, numer_green, numer_yellow, matrix,
            screen, pieces6, CELL_SIZE)
        endgame(matrix, screen, font)

        if last_roll is not None:
            result_window = pygame.Surface((150, 70))
            result_window.fill(WHITE)
            roll_text1 = font.render(f'{kolor}', True, BLACK)
            roll_text2 = font.render(f'kostka : {last_roll}', True, BLACK)
            result_window.blit(roll_text1, (10, 10))
            result_window.blit(roll_text2, (10, 30))
            screen.blit(result_window, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
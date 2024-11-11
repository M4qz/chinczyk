import sys
import pygame
from random import randrange
from pionek import Pionek

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
BOARD_SIZE = 11

def draw_maze(screen, matrix, cell_size):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            color = WHITE
            if matrix[y][x] == 2:
                color = LRED
            elif matrix[y][x] == 3:
                color = LGREEN
            elif matrix[y][x] == 44:
               color = GREY
            elif matrix[y][x] == 4:
                color = LBLUE
            elif matrix[y][x] == 5:
                color = LYELLOW
            elif matrix[y][x] == 1:
                color = BLACK

            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

def draw_pieces(movesw, movesd, movess, movesa,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, pieces, cell_size):
    for color, pos in pieces.items():
        if pos and pos == (4, 5):  #warunek sprawdzający, czy pozycja nie jest koncem
            pieces[BLUE] = None
            matrix[5][4] = 44
            numer_blue=1
            movesa=0
            #print(movesa)
            pygame.draw.rect(screen, GREY, (4 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 6):
            pieces[YELLOW] = None
            matrix[6][5] = 44
            numer_yellow=1
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 6 * cell_size, cell_size, cell_size))
        elif pos and pos == (6, 5):
            pieces[RED] = None
            matrix[5][6] = 44
            numer_red=1
            movesd=0
            pygame.draw.rect(screen, GREY, (6 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 4):
            pieces[GREEN] = None
            matrix[4][5] = 44
            numer_green=1
            movesw=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 4 * cell_size, cell_size, cell_size))
      ###################################tutaj robie zaminy 2 fazy gry##################################################

        elif pos and pos == (3, 5) and matrix[5][4] == 44:
            pieces[BLUE] = None
            matrix[5][3] = 44
            numer_blue=2
            movesa=0
            pygame.draw.rect(screen, GREY, (3 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 7) and matrix[6][5] == 44 :
            pieces[YELLOW] = None
            matrix[7][5] = 44
            numer_yellow=2
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 7 * cell_size, cell_size, cell_size))
        elif pos and pos == (7, 5) and matrix[5][6] == 44:
            pieces[RED] = None
            matrix[5][7] = 44
            numer_red=2
            movesd=0
            pygame.draw.rect(screen, GREY, (7 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 3) and   matrix[4][5] == 44:
            pieces[GREEN] = None
            matrix[3][5] = 44
            numer_green=2
            movesw=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 3 * cell_size, cell_size, cell_size))


        ###################################tutaj robie zaminy 3 fazy gry################################################## kopiujemy wszystko 2 ostatnich dodajemu w endless loopie te
        # warunki ze counter mniejszy w kazdym polu o 1 oraz ze w tej funkcji kazde kolejne pole o 1 mniejsze w pathie oraz trzeba uwzglednic ze 2 osttnie pole gdy mamy do przodu z wartoscia 44

        elif pos and pos == (2, 5) and matrix[5][4] == 44 and matrix[5][3] == 44:
            pieces[BLUE] = None
            matrix[5][2] = 44
            numer_blue=3
            movesa=0
            pygame.draw.rect(screen, GREY, (2 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 8) and matrix[6][5] == 44 and matrix[7][5] == 44:
            pieces[YELLOW] = None
            matrix[8][5] = 44
            numer_yellow=3
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 8 * cell_size, cell_size, cell_size))
        elif pos and pos == (8, 5) and matrix[5][6] == 44 and matrix[5][7] == 44:
            pieces[RED] = None
            matrix[5][8] = 44
            numer_red=3
            movesd=0
            pygame.draw.rect(screen, GREY, (8 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 2) and   matrix[4][5] == 44 and   matrix[3][5] == 44:
            pieces[GREEN] = None
            matrix[2][5] = 44
            numer_green=3
            movesw=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 2 * cell_size, cell_size, cell_size))
#4 faza rozgrywki######################################

        elif pos and pos == (1, 5) and matrix[5][4] == 44 and matrix[5][3] == 44 and matrix[5][2] == 44:
            pieces[BLUE] = None
            matrix[5][1] = 44
            numer_blue=4
            movesa=0
            pygame.draw.rect(screen, GREY, (1 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 9) and matrix[6][5] == 44 and matrix[7][5] == 44 and matrix[8][5] == 44:
            pieces[YELLOW] = None
            matrix[9][5] = 44
            numer_yellow=4
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 9 * cell_size, cell_size, cell_size))
        elif pos and pos == (9, 5) and matrix[5][6] == 44 and matrix[5][7] == 44 and matrix[5][8] == 44:
            pieces[RED] = None
            matrix[5][9] = 44
            numer_red=4
            movesd=0
            pygame.draw.rect(screen, GREY, (9 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 1) and   matrix[4][5] == 44 and   matrix[3][5] == 44 and   matrix[2][5] == 44:
            pieces[GREEN] = None
            matrix[1][5] = 44
            numer_green=4
            movesw=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 1 * cell_size, cell_size, cell_size))
            ##############################################################################
        elif pos:
            #print(movesd,"movesw")
            #print(numer_red,"numer_green")
            x, y = pos
            pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)

    return movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow


def rzutkostka():
    return randrange(1, 7)

def move_piece(pos, roll, path,granica):
    if pos is None:
        return path[0]
    idx = path.index(pos)
    new_idx = (idx + roll) % len(path)
    if granica==True:
        return pos
    return path[new_idx]

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
        pygame.time.wait(3000)  # Display the message for 3 seconds
        pygame.quit()

def number_of_players(screen, font):
    # Kolory
    button_color = (0, 0, 255)
    text_color = (255, 255, 255)
    hover_color = (255, 0, 0)

    # Pozycje przycisków
    button_2_rect = pygame.Rect(50, 150, 200, 50)
    button_3_rect = pygame.Rect(50, 250, 200, 50)
    button_4_rect = pygame.Rect(50, 350, 200, 50)

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

        screen.fill((0, 0, 0))  # Czyszczenie ekranu
        prompt_text = font.render('Podaj liczbe graczy (2-4 graczy):', True, text_color)
        screen.blit(prompt_text, (50, 50))

        mouse_pos = pygame.mouse.get_pos()

        for rect, number in [(button_2_rect, '2'), (button_3_rect, '3'), (button_4_rect, '4')]:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, hover_color, rect)
            else:
                pygame.draw.rect(screen, button_color, rect)
            button_text = font.render(number, True, text_color)
            screen.blit(button_text, (rect.x + 75, rect.y + 10))

        pygame.display.flip()

def czyzero(pionki_g):
    for i in range(5):
           if pionki_g[i].get_pos() != (0, 0):
                return False
    return True

def color(player,liczba_graczy):
    if player%liczba_graczy==0:
        kolor='Zielona'
    elif player%liczba_graczy==1:
        kolor='Czerwona'
    elif player%liczba_graczy==2:
        kolor='Żółta'
    elif player%liczba_graczy==3:
        kolor='Niebieska'
    return kolor
def gameplay(roll,last_roll,event,granicaA, numer_green, movesw,player, liczba_graczy,pieces, path_w,przycisk,kolor):
    roll = roll if roll is not None else 0
    if event.key == przycisk and player%liczba_graczy==0 :#and x==1:
        kolor=color(player,liczba_graczy)
        player+=1
        #print(player,"player")
        roll = rzutkostka()
        last_roll = roll
        if roll == 6 or pieces[GREEN]:#any(piece is None for piece in GREEN): i jeszcze or
            print(pieces[GREEN])
            if movesw+roll<50 and numer_green==0:
                movesw+=roll

            elif movesw+roll<49 and numer_green==1:
                movesw+=roll

            elif movesw+roll<48 and numer_green==2:
                movesw+=roll
            elif movesw+roll<47 and numer_green==3:
                movesw+=roll

            else:
                granicaA=True
            pieces[GREEN] = move_piece(pieces.dictionary[GREEN], roll, path_w,granicaA)
            granicaA=False
    return movesw,player,last_roll,roll,kolor


# Główna funkcja gry
def main():
    pygame.init()
    screen = pygame.display.set_mode((550, 550))  # Adjust the window size as needed
    pygame.display.set_caption('Chińczyk')
    font = pygame.font.Font(None, 36)

    liczba_graczy = number_of_players(screen, font)
    #print(f'Liczba graczy: {liczba_graczy}')

    matrix = [
        [0, 0, 0, 0, 1, 1, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0],
        [4, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
        [1, 4, 4, 4, 4, 1, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 2],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 1, 1, 0, 0, 0, 0]
    ]

    # Path of the piece on the board for green
    path_w = [(6,0), (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),
              (10,4), (10,5), (10,6), (9,6), (8,6), (7,6), (6,6), (6,7),
              (6,8), (6, 9), (6, 10), (5, 10), (4,10), (4,9), (4,8), (4,7),
              (4,6), (3, 6), (2, 6), (1,6), (0,6), (0, 5), (0,4), (1,4),
              (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(5,1),(5, 2),(5,3),(5,4)]
    path_d = [(10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7),#red
              (6,8), (6,9), (6,10), (5,10), (4,10), (4,9), (4,8), (4,7),
              (4,6), (3,6), (2,6), (1,6), (0,6), (0,5), (0,4), (1,4),
              (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(6,0),
              (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),(10,4), (10,5),(9,5),(8,5),(7,5),(6,5)]
    path_s = [(4,10), (4,9), (4,8), (4,7),#yellow
              (4,6), (3,6), (2,6), (1,6), (0,6), (0,5), (0,4), (1,4),
              (2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(6,0),
              (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),(10,4), (10,5),
              (10,6), (9,6), (8,6), (7,6), (6,6), (6,7),(6,8), (6,9), (6,10), (5,10),(5,9),(5,8),(5,7),(5,6)]
    path_a = [(0,4), (1,4),(2,4), (3,4), (4,4), (4,3), (4,2), (4,1), (4,0), (5,0),(6,0),
              (6,1), (6,2), (6,3), (6,4), (7,4), (8,4), (9,4),(10,4), (10,5),
              (10,6), (9,6), (8,6), (7,6), (6,6), (6,7),(6,8), (6,9), (6,10),#blue
              (5,10),(4,10), (4,9), (4,8), (4,7),(4,6), (3,6), (2,6), (1,6), (0,6), (0,5),(1,5),(2,5),(3,5),(4,5)]

    '''
    # Initial positions of pieces; None means not yet on the board
    pieces = {
     GREEN: [None, None, None, None],
     RED: [None, None, None, None],
     YELLOW: [None, None, None, None],
     BLUE: [None, None, None, None]}
    '''
    pieces = {
     GREEN: None,
     RED: None,
     YELLOW: None,
     BLUE: None}

    pierwsza_runda=Pionek(pieces) #obiekt przechowujacy pieces czyli slownik z pionkami
    druga_runda=Pionek(pieces)
    trzecia_runda=Pionek(pieces)
    czwarta_runda=Pionek(pieces)
    roll= None
    last_roll = None

    running = True
    clock = pygame.time.Clock()

    # Create a separate window for displaying dice roll result
    result_window = pygame.Surface((150, 50))
    result_window.fill(WHITE)
    player=0
    movesw=0
    movesd=0
    movess=0
    movesa=0
    numer_blue=0
    numer_yellow=0
    numer_green=0
    numer_red=0
    granicaA=False
    granicaB=False
    granicaC=False
    granicaD=False
    kolor='Zielona'
    pionki_g=[0,0,0,0] ######wektor obiektow
    pionki_b=[0,0,0,0]
    pionki_y=[0,0,0,0]
    pionki_r=[0,0,0,0]
    ilosc_g=0
    ilosc_b=0
    ilosc_y=0
    ilosc_r=0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                movesw,player,last_roll,roll,kolor=gameplay(roll,last_roll,event,granicaA, numer_green, movesw,player, liczba_graczy,pieces, path_w,pygame.K_w,kolor)
                movesd,player,last_roll,roll,kolor=gameplay(roll,last_roll,event,granicaB, numer_red, movesd,player, liczba_graczy,pieces, path_d,pygame.K_d,kolor)
                movess,player,last_roll,roll,kolor=gameplay(roll,last_roll,event,granicaC, numer_yellow, movess,player, liczba_graczy,pieces, path_s,pygame.K_s,kolor)
                movesa,player,last_roll,roll,kolor=gameplay(roll,last_roll,event,granicaD, numer_blue, movesa,player, liczba_graczy,pieces, path_a,pygame.K_a,kolor)




        screen.fill(BLACK)
        draw_maze(screen, matrix, CELL_SIZE)
        movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow = draw_pieces(movesw, movesd, movess, movesa,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, pierwsza_runda.dictionary, CELL_SIZE)
        #movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow = draw_pieces(movesw, movesd, movess, movesa,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, druga_runda.dictionary, CELL_SIZE)
        #movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow = draw_pieces(movesw, movesd, movess, movesa,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, druga_runda.dictionary, CELL_SIZE)
        #movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow = draw_pieces(movesw, movesd, movess, movesa,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, druga_runda.dictionary, CELL_SIZE)
        endgame(matrix, screen, font)

        # Wyświetlanie wyniku rzutu kostką w osobnym oknie
        if last_roll is not None:
            result_window.fill(WHITE)
            roll_text1 = font.render(f'{kolor}', True, BLACK)
            roll_text2 = font.render(f'kostka : {last_roll}', True, BLACK)
            result_window.blit(roll_text1, (10, 10))
            result_window.blit(roll_text2, (10, 30))
            screen.blit(result_window, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()


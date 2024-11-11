import pygame
from random import randrange

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
        if pos and pos == (4, 5):  # Dodaj warunek sprawdzający, czy pozycja nie jest koncem
            pieces[BLUE] = None
            matrix[5][4] = 44
            numer_blue=1
            movesa=0
            print(movesa)
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
            numer_yellow=2
            movesa=0
            pygame.draw.rect(screen, GREY, (3 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 7) and matrix[6][5] == 44 :
            pieces[YELLOW] = None
            matrix[7][5] = 44
            numer_red=2
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 7 * cell_size, cell_size, cell_size))
        elif pos and pos == (7, 5) and matrix[5][6] == 44:
            pieces[RED] = None
            matrix[5][7] = 44
            numer_green=2
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
            numer_yellow=3
            movesa=0
            pygame.draw.rect(screen, GREY, (2 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 8) and matrix[6][5] == 44 and matrix[7][5] == 44:
            pieces[YELLOW] = None
            matrix[8][5] = 44
            numer_red=3
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 8 * cell_size, cell_size, cell_size))
        elif pos and pos == (8, 5) and matrix[5][6] == 44 and matrix[5][7] == 44:
            pieces[RED] = None
            matrix[5][8] = 44
            numer_green=3
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
            numer_yellow=4
            movesa=0
            pygame.draw.rect(screen, GREY, (1 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 9) and matrix[6][5] == 44 and matrix[7][5] == 44 and matrix[8][5] == 44:
            pieces[YELLOW] = None
            matrix[9][5] = 44
            numer_red=4
            movess=0
            pygame.draw.rect(screen, GREY, (5 * cell_size, 9 * cell_size, cell_size, cell_size))
        elif pos and pos == (9, 5) and matrix[5][6] == 44 and matrix[5][7] == 44 and matrix[5][8] == 44:
            pieces[RED] = None
            matrix[5][9] = 44
            numer_green=4
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
            print(movesd,"movesw")
            print(numer_red,"numer_green")
            x, y = pos
            pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)

    return movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow


def rzutkostka():
    return randrange(1, 7)

def tuple_to_ints(tup):
    return int(tup[0]), int(tup[1])

def move_piece(matrix,pos, roll, path,granica):
    if pos is None:
        return path[0]
    idx = path.index(pos)
    new_idx = (idx + roll) % len(path)
    #print(path[idx])
    #print(path[new_idx])
    #pattern = r"\((\d+),(\d+)\)"
    #match = re.match(pattern, path[idx])
    #num1 = int(match.group(1))
    #num2 = int(match.group(2))
    if granica==True:
        return pos
    '''
    x,y=tuple_to_ints(path[new_idx])
    if(path[new_idx]==path[-1]):
        matrix[x][y]=44
        print(matrix)
'''
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_SIZE * CELL_SIZE, BOARD_SIZE * CELL_SIZE))
    pygame.display.set_caption('Chińczyk')
    font = pygame.font.Font(None, 36)

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


    # Initial positions of pieces; None means not yet on the board
    pieces = {
        GREEN: None,
        RED: None,
        YELLOW: None,
        BLUE: None
    }

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player%4==0:
                    player+=1
                    print(player,"player")
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces[GREEN]:
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
                        pieces[GREEN] = move_piece(matrix,pieces[GREEN], roll, path_w,granicaA)
                        granicaA=False


                if event.key == pygame.K_d and player%4==1:
                    player+=1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces[RED]:
                        if movesd+roll<50 and numer_red==0:
                            movesd+=roll

                        elif movesd+roll<49 and numer_red==1:
                                movesd+=roll
                        elif movesd+roll<48 and numer_red==2:
                            movesd+=roll
                        elif movesd+roll<47 and numer_red==3:
                            movesd+=roll

                        else:
                            granicaB=True
                        pieces[RED] = move_piece(matrix,pieces[RED], roll, path_d,granicaB)
                        granicaB=False
                 
                if event.key == pygame.K_s and player%4==2:
                    player+=1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces[YELLOW]:
                        if movess+roll<50 and numer_yellow==0:
                            movess+=roll

                        elif movess+roll<49 and numer_yellow==1:
                            movess+=roll
                        elif movess+roll<48 and numer_yellow==2:
                            movess+=roll
                        elif movess+roll<47 and numer_yellow==3:
                            movess+=roll
                        else:
                            granicaC=True
                        pieces[YELLOW] = move_piece(matrix,pieces[YELLOW], roll, path_s,granicaC)
                        granicaC=False
                    
                if event.key == pygame.K_a and player%4==3:
                    player+=1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces[BLUE]:
                        if movesa+roll<50 and numer_blue==0:
                            movesa+=roll
                            print(movesa)
                            print("numer_blue",numer_blue)

                        elif movesa+roll<49 and numer_blue==1:
                            movesa+=roll
                            print("numer_blue",numer_blue)
                        elif movesa+roll<48 and numer_blue==2:
                            movesa+=roll
                        elif movesa+roll<47 and numer_blue==3:
                            movesa+=roll
                        else:
                            granicaD=True
                        pieces[BLUE] = move_piece(matrix,pieces[BLUE], roll, path_a,granicaD)
                        granicaD=False
                   

                
        screen.fill(BLACK)
        draw_maze(screen, matrix, CELL_SIZE)
        movesw, movesd, movess, movesa, numer_blue, numer_red, numer_green, numer_yellow = draw_pieces(movesw, movesd, movess, movesa,numer_blue,numer_red,numer_green,numer_yellow,matrix,screen, pieces, CELL_SIZE)
        endgame(matrix, screen, font)

        # Wyświetlanie wyniku rzutu kostką w osobnym oknie
        if last_roll is not None:
            result_window.fill(WHITE)
            roll_text = font.render(f'Kostka : {last_roll}', True, BLACK)
            result_window.blit(roll_text, (10, 10))
            screen.blit(result_window, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()


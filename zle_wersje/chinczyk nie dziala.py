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
            elif matrix[y][x] == 4:
                color = LBLUE
            elif matrix[y][x] == 5:
                color = LYELLOW
            elif matrix[y][x] == 1:
                color = BLACK

            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

def draw_pieces(matrix,screen, pieces, cell_size):
    for color, pos in pieces.items():
        if pos and pos == (4, 5):  # Dodaj warunek sprawdzający, czy pozycja nie jest koncem
            pieces[BLUE] = None
            matrix[5][4] = 44
            pygame.draw.rect(screen, GREY, (4 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 6):
            pieces[YELLOW] = None
            matrix[6][5] = 44
            pygame.draw.rect(screen, GREY, (5 * cell_size, 6 * cell_size, cell_size, cell_size))
        elif pos and pos == (6, 5):
            pieces[RED] = None
            matrix[5][6] = 44
            pygame.draw.rect(screen, GREY, (6 * cell_size, 5 * cell_size, cell_size, cell_size))
        elif pos and pos == (5, 4):
            pieces[GREEN] = None
            matrix[4][5] = 44
            pygame.draw.rect(screen, GREY, (5 * cell_size, 4 * cell_size, cell_size, cell_size))
        elif pos:
            x, y = pos
            pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)


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
    print(path[-1])
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
'''
def endgame(moves,player):
    if moves==49 and player%4==0:
        print("Wygral zielony")
        pygame.quit()
    if moves==49 and player%4==1:
        print("Wygral czerwony")
        pygame.quit()
    if moves==49 and player%4==2:
        print("Wygral zolty")
        pygame.quit()
    if moves==49 and player%4==3:
        print("Wygral niebieski")
        pygame.quit()
'''
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
                if event.key == pygame.K_w :#and player%4==0:
                    player+=1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces[GREEN]:
                        if movesw+roll<50:
                            movesw+=roll
                        else:
                            granicaA=True
                        pieces[GREEN] = move_piece(matrix,pieces[GREEN], roll, path_w,granicaA)
                        granicaA=False
                        '''
                   # endgame(movesw,player)
               
               if event.key == pygame.K_d and player%4==1:
                   player+=1
                   roll = rzutkostka()
                   last_roll = roll
                   if roll == 6 or pieces[RED]:
                       if movesd+roll<50:
                           movesd+=roll
                       else:
                           granicaB=True
                       pieces[RED] = move_piece(matrix,pieces[RED], roll, path_d,granicaB)
                       granicaB=False
                   # endgame(movesd,player)
               if event.key == pygame.K_s and player%4==2:
                   player+=1
                   roll = rzutkostka()
                   last_roll = roll
                   if roll == 6 or pieces[YELLOW]:
                       if movess+roll<50:
                           movess+=roll
                       else:
                           granicaC=True
                       pieces[YELLOW] = move_piece(matrix,pieces[YELLOW], roll, path_s,granicaC)
                       granicaC=False
                   # endgame(movess,player)
               if event.key == pygame.K_a and player%4==3:
                   player+=1
                   roll = rzutkostka()
                   last_roll = roll
                   if roll == 6 or pieces[BLUE]:
                       if movesa+roll<50:
                           movesa+=roll
                       else:
                           granicaD=True
                       pieces[BLUE] = move_piece(matrix,pieces[BLUE], roll, path_a,granicaD)
                       granicaD=False
                   #  endgame(movesa,player)
               '''

        screen.fill(BLACK)
        draw_maze(screen, matrix, CELL_SIZE)
        draw_pieces(matrix,screen, pieces, CELL_SIZE)




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
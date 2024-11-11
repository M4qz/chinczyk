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
GREY = (255, 255, 230)
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

def draw_pieces(moves, matrix, screen, pieces, cell_size):
    for color, pos in pieces.items():
        if pos:
            x, y = pos
            pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)

def rzutkostka():
    return randrange(1, 7)

def move_piece(pos, roll, path, granica):
    if pos is None:
        return path[0]
    idx = path.index(pos)
    new_idx = (idx + roll) % len(path)
    if granica:
        return pos
    return path[new_idx]

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
    player = 0
    movesw = 0
    movesd = 0
    movess = 0
    movesa = 0
    numer_blue = 0
    numer_yellow = 0
    numer_green = 0
    numer_red = 0
    blue_granica = False
    yellow_granica = False
    green_granica = False
    red_granica = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll = rzutkostka()
                    last_roll = roll
                    result_window.fill(WHITE)
                    roll_text = font.render(f'Roll: {roll}', True, BLACK)
                    result_window.blit(roll_text, (10, 10))
                    screen.blit(result_window, (BOARD_SIZE * CELL_SIZE // 2 - 75, BOARD_SIZE * CELL_SIZE // 2 - 25))
                    pygame.display.flip()

                    if player == 0:
                        if numer_green == 44:
                            green_granica = True
                        pieces[GREEN] = move_piece(pieces[GREEN], roll, path_w, green_granica)
                        movesw += 1
                        numer_green += roll
                    elif player == 1:
                        if numer_red == 41:
                            red_granica = True
                        pieces[RED] = move_piece(pieces[RED], roll, path_d, red_granica)
                        movesd += 1
                        numer_red += roll
                    elif player == 2:
                        if numer_yellow == 43:
                            yellow_granica = True
                        pieces[YELLOW] = move_piece(pieces[YELLOW], roll, path_s, yellow_granica)
                        movess += 1
                        numer_yellow += roll
                    elif player == 3:
                        if numer_blue == 43:
                            blue_granica = True
                        pieces[BLUE] = move_piece(pieces[BLUE], roll, path_a, blue_granica)
                        movesa += 1
                        numer_blue += roll

                    player = (player + 1) % 4

        screen.fill(WHITE)
        draw_maze(screen, matrix, CELL_SIZE)
        draw_pieces(movesw, matrix, screen, pieces, CELL_SIZE)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()

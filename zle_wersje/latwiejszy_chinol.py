import pygame
from random import randint

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
CELL_SIZE = 50
BOARD_SIZE = 11

class Piece:
    def __init__(self, color):
        self.color = color
        self.index = 0
        self.position = 0
        self.granica = False

    def move(self, roll, path):
        if self.position + roll < 50:
            self.position += roll
        else:
            self.granica = True
        self.index = move_piece(self.index, roll, path, self.granica)
        self.granica = False

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

def draw_pieces(screen, pieces, cell_size):
    for color, piece in pieces.items():
        if piece.position:
            x, y = piece.position
            pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)

def rzutkostka():
    return randint(1, 6)

def move_piece(piece, roll, path, granica):
    # Placeholder for move piece function
    return piece

def game_loop(screen, pieces, path_w, path_d, path_s, path_a, matrix, font):
    running = True
    player = 0
    last_roll = None
    movesw = 0
    movesd = 0
    movess = 0
    movesa = 0
    granicaA = False
    granicaB = False
    granicaC = False
    granicaD = False
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)
        draw_maze(screen, matrix, CELL_SIZE)
        draw_pieces(screen, pieces, CELL_SIZE)

        # Wyświetlanie wyniku rzutu kostką w osobnym oknie
        if last_roll is not None:
            result_window = pygame.Surface((150, 50))
            result_window.fill(WHITE)
            roll_text = font.render(f'Kostka : {last_roll}', True, BLACK)
            result_window.blit(roll_text, (10, 10))
            screen.blit(result_window, (10, 10))

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player % 4 == 0:
                    player += 1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces["GREEN"].index:
                        pieces["GREEN"].move(roll, path_w)
                    # endgame(pieces["GREEN"].position, player)

                if event.key == pygame.K_d and player % 4 == 1:
                    player += 1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces["RED"].index:
                        pieces["RED"].move(roll, path_d)
                    # endgame(pieces["RED"].position, player)

                if event.key == pygame.K_s and player % 4 == 2:
                    player += 1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces["YELLOW"].index:
                        pieces["YELLOW"].move(roll, path_s)
                    # endgame(pieces["YELLOW"].position, player)

                if event.key == pygame.K_a and player % 4 == 3:
                    player += 1
                    roll = rzutkostka()
                    last_roll = roll
                    if roll == 6 or pieces["BLUE"].index:
                        pieces["BLUE"].move(roll, path_a)
                    # endgame(pieces["BLUE"].position, player)

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
        [1, 4, 4, 4, 4, 0, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 2],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 1, 1, 0, 0, 0, 0]
    ]

    # Path of the piece on the board for each color
    path_w = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 4), (8, 4), (9, 4),
              (10, 4), (10, 5), (10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7),
              (6, 8), (6, 9), (6, 10), (5, 10), (4, 10), (4, 9), (4, 8), (4, 7),
              (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (1, 4),
              (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4)]
    path_d = [(10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7),
              (6, 8), (6, 9), (6, 10), (5, 10), (4, 10), (4, 9), (4, 8), (4, 7),
              (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (1, 4),
              (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0),
              (6, 1), (6, 2), (6, 3), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5)]
    path_s = [(4, 10), (4, 9), (4, 8), (4, 7),
              (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (1, 4),
              (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0),
              (6, 1), (6, 2), (6, 3), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (10, 5),
              (10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6)]
    path_a = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0),
              (6, 1), (6, 2), (6, 3), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (10, 5),
              (10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
              (5, 10), (4, 10), (4, 9), (4, 8), (4, 7), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]

    pieces = {
        "GREEN": Piece(GREEN),
        "RED": Piece(RED),
        "YELLOW": Piece(YELLOW),
        "BLUE": Piece(BLUE)
    }

    game_loop(screen, pieces, path_w, path_d, path_s, path_a, matrix, font)
    pygame.quit()

if __name__ == "__main__":
    main()

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

def draw_pieces(pieces, matrix, screen, cell_size):
    for color, positions in pieces.items():
        for pos in positions:
            if pos:
                x, y = pos
                pygame.draw.circle(screen, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 3)

def rzutkostka():
    return randrange(1, 7)

def move_piece(pos, roll, path):
    if pos is None:
        return path[0]
    idx = path.index(pos)
    new_idx = (idx + roll) % len(path)
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((550, 550))  # Adjust the window size as needed
    pygame.display.set_caption('Chińczyk')
    font = pygame.font.Font(None, 36)

    liczba_graczy = number_of_players(screen, font)

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
    path_w = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 4), (8, 4), (9, 4),
              (10, 4), (10, 5), (10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7),
              (6, 8), (6, 9), (6, 10), (5, 10), (4, 10), (4, 9), (4, 8), (4, 7),
              (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (1, 4),
              (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0),
              (5, 1), (5, 2), (5, 3), (5, 4)]

    path_r = [(10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0),
              (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5),
              (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 10),
              (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 5),
              (9, 5), (8, 5), (7, 5), (6, 5)]

    path_b = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5),
              (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 10),
              (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 5),
              (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0),
              (5, 1), (5, 2), (5, 3), (5, 4)]

    path_y = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 10),
              (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 5),
              (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0),
              (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5),
              (1, 5), (2, 5), (3, 5), (4, 5)]

    pieces = {RED: [None, None, None, None], GREEN: [None, None, None, None], BLUE: [None, None, None, None], YELLOW: [None, None, None, None]}
    paths = {RED: path_r, GREEN: path_w, BLUE: path_b, YELLOW: path_y}

    turn = 0
    colors = list(pieces.keys())[:liczba_graczy]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_maze(screen, matrix, CELL_SIZE)
        draw_pieces(pieces, matrix, screen, CELL_SIZE)
        pygame.display.flip()

        current_color = colors[turn]
        roll = rzutkostka()

        available_pieces = [i for i, pos in enumerate(pieces[current_color]) if pos is not None]
        if len(available_pieces) < 4 and roll == 6:
            for i in range(4):
                if pieces[current_color][i] is None:
                    pieces[current_color][i] = paths[current_color][0]
                    break
        elif available_pieces:
            piece_to_move = available_pieces[0]
            pieces[current_color][piece_to_move] = move_piece(pieces[current_color][piece_to_move], roll, paths[current_color])

        endgame(matrix, screen, font)

        turn = (turn + 1) % liczba_graczy
        pygame.time.wait(1000)

if __name__ == '__main__':
    main()

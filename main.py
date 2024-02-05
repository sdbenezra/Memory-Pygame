import random

import pygame

pygame.init()

# game variables and constants
WIDTH = 450
HEIGHT = 600
rows = 4
cols = 4
TOP_MENU_HEIGHT = 100
white = (255, 255, 255)
black = (0, 0, 0)
selected = (213, 106, 235)
green = (0, 255, 0)
gray = (127, 129, 128)
fps = 60
timer = pygame.time.Clock()
correct = [[0 for col in range(cols)] for row in range(rows)]
options_list = []
spaces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0
game_over = False

# create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Memory Game')
title_font = pygame.font.Font('freesansbold.ttf', 56)
sub_title_font = pygame.font.Font('freesansbold.ttf', 36)
body_font = pygame.font.Font('freesansbold.ttf', 26)


def generate_board():
    global options_list
    global spaces
    global used
    for item in range(rows * cols // 2):
        options_list.append(item)
    for item in range(rows * cols):
        piece = options_list[random.randint(0, len(options_list)-1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)


def draw_backgrounds():
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, TOP_MENU_HEIGHT])
    title_text = title_font.render('Memory Game', True, white)
    width, height = title_font.size('Memory Game')
    # centering title text
    xoffset = (WIDTH - width) // 2
    yoffset = (TOP_MENU_HEIGHT - height) // 2
    coords = [xoffset, yoffset]
    screen.blit(title_text, coords)
    board_space = pygame.draw.rect(screen, gray, [0, 100, WIDTH, HEIGHT - 200], 0)
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT - 100, WIDTH, 100], 0)
    restart_button = pygame.draw.rect(screen, gray, [10, HEIGHT - 90, 200, 80], 0, 5)
    restart_text = sub_title_font.render('Restart', True, white)
    screen.blit(restart_text, (45, 530))
    score_text = body_font.render(f'Current Turns: {score}', True, white)
    screen.blit(score_text, (225, 520))
    best_text = body_font.render(f'Previous Best: {best_score}', True, white)
    screen.blit(best_text, (225, 560))
    return restart_button


def draw_board():
    global rows
    global cols
    global correct
    board_list = []
    # Fill board by column (single dimension array displayed in two dimension grid)
    for col in range(cols):
        for row in range(rows):
            piece = pygame.draw.rect(screen, white, [col * 85 + 60, row * 90 + 120, 70, 70], 0, 4)
            board_list.append(piece)
            '''piece_text = body_font.render(f'{spaces[i * rows + j]}', True, gray)
            screen.blit(piece_text, (i * 75 + 18, j * 65 + 120))'''

    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, green, [c * 85 + 58, r * 90 + 118, 74, 74], 3, 4)
                piece_text = body_font.render(f'{spaces[c * rows + r]}', True, black)
                screen.blit(piece_text, (c * 85 + 85, r * 90 + 140))
    return board_list


def check_guesses(first, second):
    global spaces
    global correct
    global score
    global matches
    if spaces[first] == spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 = first % rows
        row2 = second % rows
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
            print(correct)
            print(f'score: {score}')
            print(f'matches: {matches}')
    else:
        score += 1


running = True

# event handler
while running:
    timer.tick(fps)
    screen.fill(white)
    if new_board:
        generate_board()
        print(spaces)
        new_board = False

    restart = draw_backgrounds()
    board = draw_board()

    if first_guess and second_guess:
        check_guesses(first_guess_num, second_guess_num)
        pygame.time.delay(1000)
        first_guess = False
        second_guess = False

    # game event handlers
    for event in pygame.event.get():
        # to quit from game
        if event.type == pygame.QUIT:
            running = False
        # mouse click handlers
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if not game_over:
                    if button.collidepoint(event.pos) and not first_guess:
                        first_guess = True
                        first_guess_num = i
                        print(f'first guess {i}')
                    if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
                        print(f'second guess {i}')
            if restart.collidepoint(event.pos):
                options_list = []
                used = []
                spaces = []
                new_board = True
                score = 0
                matches = 0
                first_guess = False
                second_guess = False
                correct = [[0 for col in range(cols)] for row in range(rows)]
                game_over = False

    if matches == rows * cols // 2:
        game_over = True
        winner = pygame.draw.rect(screen, gray, [10, HEIGHT - 330, WIDTH - 20, 80], 0, 5)
        winner_text = sub_title_font.render(f'You Won in {score} moves!', True, white)
        screen.blit(winner_text, (30, HEIGHT - 310))
        if best_score > score or best_score == 0:
            best_score = score

    if first_guess:
        piece_text = body_font.render(f'{spaces[first_guess_num]}', True, selected)
        location = (first_guess_num // rows * 85 + 85, (first_guess_num % rows) * 90 + 140)
        screen.blit(piece_text, location)

    if second_guess:
        piece_text = body_font.render(f'{spaces[second_guess_num]}', True, selected)
        location = (second_guess_num // rows * 85 + 85, (second_guess_num % rows) * 90 + 140)
        screen.blit(piece_text, location)

    pygame.display.flip()
pygame.QUIT

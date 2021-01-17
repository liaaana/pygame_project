import pygame
import sys
import random
from math import sin, cos, pi
from PIL import Image



def load_image(name, colorkey=None):
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def show_text(t, pos, size, font='fonts/MajorMonoDisplay-Regular.ttf', color=(0, 0, 0)):
    font = pygame.font.Font(font, size)
    text = font.render(f'{t}', 1, color)
    screen.blit(text, (pos))


def draw_img(name, x, y, w, h):
    img = pygame.transform.scale(load_image(name), (w, h))
    screen.blit(img, (x, y))


def start_screen():
    pygame.display.set_caption('Start')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    bg = Background()
    button = Button(WIDTH // 2 - 90, HEIGHT // 2 + 150, 180, 60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    sound2.play()
                    run = False
        screen.fill(BLACK)
        bg.draw_space(WHITE, True)
        button.draw('start', (WIDTH // 2 - 90 + 17, HEIGHT // 2 + 150 + 10), 40)
        pygame.display.flip()
        clock.tick(FPS)


def second_screen():
    pygame.display.set_caption('Rules')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    bg = Background()
    button = Button(WIDTH // 2 - 90, HEIGHT // 2 + 150, 180, 60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    sound2.play()
                    run = False
        screen.fill(BLACK)
        bg.draw_space()
        draw_img('all_img/btn_1.png', 250, 150, 240, 160)
        draw_img('all_img/btn_2.png', 900, 150, 240, 160)
        show_text('Player1', (310, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player2', (960, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        button.draw('OK', (WIDTH // 2 - 90 + 60, HEIGHT // 2 + 150 + 13), 30, 'fonts/Orbitron-VariableFont_wght.ttf')
        pygame.display.flip()
        clock.tick(FPS)


def third_screen():
    pygame.display.set_caption('Games')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    bg = Background()
    button = Button(WIDTH // 2 - 90, HEIGHT // 2 + 150, 180, 60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    sound2.play()
                    run = False
        screen.fill(BLACK)
        bg.draw_space()
        draw_img('all_img/game_icon1.png', 400, 180, 140, 140)
        draw_img('all_img/game_icon2.png', 625, 180, 140, 140)
        draw_img('all_img/game_icon3.png', 850, 180, 140, 140)
        show_text('Ping pong', (400, 330), 25, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Connect four', (625, 330), 25, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Timer', (850, 330), 25, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        button.draw('GO', (WIDTH // 2 - 90 + 60, HEIGHT // 2 + 150 + 13), 30, 'fonts/Orbitron-VariableFont_wght.ttf')
        pygame.display.flip()
        clock.tick(FPS)


def game1():
    class Ball(pygame.sprite.Sprite):
        def __init__(self, group, x, y, w, h, name):
            super().__init__(group)
            image = Image.open(name)
            image = image.resize((w, h))
            image.save(name)
            self.img_name = name
            self.image = load_image(name)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(x, y, w, h)
            self.add_speed = 0.01
            self.speed_x = 4 * random.choice([-1, 1])
            self.speed_y = 4 * random.choice([-1, 1])
            self.ball_time = 0
            self.now = 0
            self.go = 0

        def update(self, *args):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.speed_y = -self.speed_y
            if self.rect.colliderect(player1.get_rect()) and self.speed_x > 0:
                sound1.play()
                if abs(self.rect.right - player1.get_rect().left) < 10:
                    self.speed_x = -self.speed_x
                elif abs(self.rect.bottom - player1.get_rect().top) < 10 and self.speed_y > 0:
                    self.speed_y = -self.speed_y
                elif abs(self.rect.bottom - player1.get_rect().top) < 10 and self.speed_y < 0:
                    self.speed_y = -self.speed_y

            if self.rect.colliderect(player2.get_rect()) and self.speed_x < 0:
                sound1.play()
                if abs(self.rect.left - player2.get_rect().right) < 10:
                    self.speed_x = -self.speed_x
                elif abs(self.rect.bottom - player2.get_rect().top) < 10 and self.speed_y > 0:
                    self.speed_y = -self.speed_y
                elif abs(self.rect.bottom - player2.get_rect().top) < 10 and self.speed_y < 0:
                    self.speed_y = -self.speed_y

            if self.rect.left <= 0:
                self.speed_x = 0
                self.speed_y = 0
                self.rect.center = (WIDTH // 2, HEIGHT // 2)
                player2.set_score(player2.get_score() + 1)
                self.ball_time = pygame.time.get_ticks()
                self.go = 1

            if self.rect.right >= WIDTH:
                self.speed_x = 0
                self.speed_y = 0
                self.rect.center = (WIDTH // 2, HEIGHT // 2)
                player1.set_score(player1.get_score() + 1)
                self.ball_time = pygame.time.get_ticks()
                self.go = 1

            for event in args:
                if event.type == MYEVENTTYPE and not self.go:
                    if self.speed_x > 0:
                        self.speed_x += self.add_speed
                    else:
                        self.speed_x -= self.add_speed
                    if self.speed_y > 0:
                        self.speed_y += self.add_speed
                    else:
                        self.speed_y -= self.add_speed

        def restart(self):
            self.now = pygame.time.get_ticks()
            if self.now - self.ball_time < 1000:
                self.speed_x = 0
                self.speed_y = 0
                self.rect.center = (WIDTH // 2, HEIGHT // 2)
            else:
                self.speed_x = 4 * random.choice([-1, 1])
                self.speed_y = 4 * random.choice([-1, 1])
                self.go = 0
                self.ball_time = 0
                self.now = 0

        def get_go(self):
            return self.go

    class PingPLayer(pygame.sprite.Sprite):
        def __init__(self, group, x, y, w, h, name):
            super().__init__(group)
            image = Image.open(name)
            image = image.resize((w, h))
            image.save(name)
            self.img_name = name
            self.image = load_image(name)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(x, y, w, h)
            self.speed = 7
            self.score = 0

        def update(self, *args):
            for event in args:
                pre = self.rect.y
                if pygame.key.get_pressed()[pygame.K_w] and self.img_name[-5] == '4':
                    self.rect.y -= self.speed
                if pygame.key.get_pressed()[pygame.K_s] and self.img_name[-5] == '4':
                    self.rect.y += self.speed
                if pygame.key.get_pressed()[pygame.K_UP] and self.img_name[-5] == '3':
                    self.rect.y -= self.speed
                if pygame.key.get_pressed()[pygame.K_DOWN] and self.img_name[-5] == '3':
                    self.rect.y += self.speed
                if not (0 <= self.rect.y <= HEIGHT - 72):
                    self.rect.y = pre
            self.show_score()

        def show_score(self):
            font_size = 24
            font = pygame.font.Font(None, font_size)
            font_color = WHITE
            text = font.render(f'{self.score}', 1, font_color)
            if self.img_name[-5] == '3':
                pos = (WIDTH // 2 - 70, HEIGHT // 2 - 7)
            else:
                pos = (WIDTH // 2 + 70, HEIGHT // 2 - 7)
            screen.blit(text, pos)

        def set_score(self, n):
            self.score = n

        def get_score(self):
            return self.score

        def get_rect(self):
            return self.rect

    pygame.display.set_caption('Game1')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    players = pygame.sprite.Group()
    balls = pygame.sprite.Group()

    player1 = PingPLayer(players, WIDTH - 20, HEIGHT / 2 - 45, 20, 90, "all_img/images2/p3.png")
    player2 = PingPLayer(players, 0, HEIGHT / 2 - 45, 20, 90, "all_img/images2/p4.png")
    ball = Ball(balls, WIDTH / 2 - 15, HEIGHT / 2 - 15, 20, 20, 'all_img/images2/ball.png')
    bg = Background()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if player1.get_score() == 3:
                WINNER.append(1)
                return
            if player2.get_score() == 3:
                WINNER.append(2)
                return
            if ball.get_go():
                ball.restart()
        screen.fill(BLACK)
        bg.draw_space(pygame.Color((100, 100, 100)))
        pygame.draw.aaline(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

        players.draw(screen)
        balls.draw(screen)

        players.update(event)
        balls.update(event)

        pygame.display.flip()
        clock.tick(FPS)


def wait_screen():
    pygame.display.set_caption('Break')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    bg = Background()
    button = Button(WIDTH // 2 - 90, HEIGHT // 2 + 150, 180, 60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    sound2.play()
                    run = False
        screen.fill(BLACK)
        bg.draw_space()
        show_text(f'{WINNER.count(1)}', (320, 100), 100, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text(f'{WINNER.count(2)}', (970, 100), 100, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player1', (300, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player2', (955, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        button.draw('GO', (WIDTH // 2 - 90 + 60, HEIGHT // 2 + 150 + 13), 30, 'fonts/Orbitron-VariableFont_wght.ttf')
        pygame.display.flip()
        clock.tick(FPS)


def game2():
    pygame.display.set_caption('Game2')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    class Board():
        def __init__(self):
            self.board = [[0 for _ in range(COLUMNS)] for __ in range(ROWS)]
            self.turn = 0

        def draw(self):
            for c in range(COLUMNS):
                for r in range(ROWS):
                    draw_img('all_img/images1/block1.png', c * BOX + (WIDTH - board_w) // 2, r * BOX + BOX, BOX, BOX)
                    if self.board[ROWS - r - 1][c] == 0:
                        pygame.draw.circle(screen, BLACK, (
                            int(c * BOX + BOX / 2 + (WIDTH - board_w) // 2), int(r * BOX + BOX / 2 + BOX)),
                                           RADIUS)
                    if self.board[ROWS - r - 1][c] == 1:
                        draw_img('all_img/images1/f1.png', c * BOX + (WIDTH - board_w) // 2 + BOX // 6,
                                 r * BOX + BOX + BOX // 6,
                                 RADIUS * 2, RADIUS * 2)
                    if self.board[ROWS - r - 1][c] == 2:
                        draw_img('all_img/images1/f2.png', c * BOX + (WIDTH - board_w) // 2 + BOX // 6,
                                 r * BOX + BOX + BOX // 6,
                                 RADIUS * 2, RADIUS * 2)

        def add(self, r, c, pl):
            sound1.play()
            self.board[r][c] = pl

        def is_free(self, c):
            return self.board[ROWS - 1][c] == 0

        def next(self, col):
            for r in range(ROWS):
                if self.board[r][col] == 0:
                    return r

        def win(self, pl):
            for c in range(COLUMNS - 3):
                for r in range(ROWS):
                    if self.board[r][c] == pl and self.board[r][c + 1] == pl and self.board[r][c + 2] == pl \
                            and self.board[r][c + 3] == pl:
                        return True

            for c in range(COLUMNS):
                for r in range(ROWS - 3):
                    if self.board[r][c] == pl and self.board[r + 1][c] == pl and self.board[r + 2][c] == pl and \
                            self.board[r + 3][c] == pl:
                        return True

            for c in range(COLUMNS - 3):
                for r in range(ROWS - 3):
                    if self.board[r][c] == pl and self.board[r + 1][c + 1] == pl and self.board[r + 2][c + 2] == pl and \
                            self.board[r + 3][c + 3] == pl:
                        return True

            for c in range(COLUMNS - 3):
                for r in range(3, ROWS):
                    if self.board[r][c] == pl and self.board[r - 1][c + 1] == pl and self.board[r - 2][c + 2] == pl and \
                            self.board[r - 3][
                                c + 3] == pl:
                        return True

        def upd(self, *args):
            screen.fill(BLACK)
            bg.draw_space()
            board.draw()
            for event in args:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, BOX))
                    if self.turn == 0:
                        draw_img('all_img/images1/f1.png', event.pos[0], BOX // 6,
                                 RADIUS * 2, RADIUS * 2)
                    if self.turn == 1:
                        draw_img('all_img/images1/f2.png', event.pos[0], BOX // 6,
                                 RADIUS * 2, RADIUS * 2)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn == 0:
                        x, y = event.pos
                        col = int((x - (WIDTH - board_w) // 2) / BOX)
                        if self.is_free(col):
                            row = self.next(col)
                            self.add(row, col, 1)
                    else:
                        x, y = event.pos
                        col = int((x - (WIDTH - board_w) // 2) / BOX)
                        if self.is_free(col):
                            row = self.next(col)
                            self.add(row, col, 2)
                    self.turn = int(not self.turn)
    run = True
    BOX = 100
    ROWS = 6
    COLUMNS = 7
    RADIUS = int(BOX / 2 - 15)
    board_w = COLUMNS * BOX
    board = Board()
    bg = Background()
    screen.fill(BLACK)
    bg.draw_space()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if board.win(1):
                if len(WINNER) == 1:
                    WINNER.append(1)
                return
            elif board.win(2):
                if len(WINNER) == 1:
                    WINNER.append(2)
                return
            board.upd(event)
        pygame.display.flip()
        clock.tick(FPS)


def game3():
    pygame.display.set_caption('Game3')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))

    class ButtonUpd():
        def __init__(self, x, y, w, h):
            self.btn = (x, y, w, h)

        def draw(self, t, pos, size, font='fonts/MajorMonoDisplay-Regular.ttf'):
            pygame.draw.rect(screen, WHITE, self.btn)
            show_text(t, pos, size, font)

        def is_clicked(self, event, player):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and player == 2:
                    sound1.play()
                    return True
            else:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and player == 1:
                    sound1.play()
                    return True
            else:
                return False

    class MyClock():
        def __init__(self, time):
            self.my_time = time
            self.time_now = pygame.time.get_ticks()
            self.drawing = 1
            self.block_rect1 = pygame.Rect(WIDTH // 2 - 380, -60, 180, 60)
            self.block_rect2 = pygame.Rect(WIDTH // 2 + 180, -60, 180, 60)
            self.time_p1 = 0
            self.time_p2 = 0
            self.res = 0

        def upd(self):
            if not self.res:
                if (pygame.time.get_ticks() - self.time_now) < 4000 or self.block_rect1.y < HEIGHT // 4:
                    self.block_rect1.y += 1
                    self.block_rect2.y += 1
                if (pygame.time.get_ticks() - self.time_now) >= 4000:
                    self.drawing = 0
                pygame.draw.rect(screen, WHITE, self.block_rect1)
                pygame.draw.rect(screen, WHITE, self.block_rect2)
                pygame.display.update()

        def draw(self):
            if self.drawing:
                show_text(f'{(pygame.time.get_ticks() - self.time_now) / 1000}', (WIDTH // 2 - 360, HEIGHT // 4), 30,
                          'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
                show_text(f'{(pygame.time.get_ticks() - self.time_now) / 1000}', (WIDTH // 2 + 200, HEIGHT // 4), 30,
                          'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
            if self.res:
                show_text(f'{self.time_p1 / 1000}', (WIDTH // 2 - 360, HEIGHT // 4), 30,
                          'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
                show_text(f'{self.time_p2 / 1000}', (WIDTH // 2 + 200, HEIGHT // 4), 30,
                          'fonts/Orbitron-VariableFont_wght.ttf', WHITE)

        def set_res(self, p, n):
            if p == 1:
                self.time_p1 = n - self.time_now
            if p == 2:
                self.time_p2 = n - self.time_now
            if self.time_p2 != 0 and self.time_p1 != 0:
                self.res = 1
                self.drawing = 0

        def get_res(self):
            return self.time_p1, self.time_p2

    go = 0
    game_time = random.randint(7, 20)
    start = pygame.time.get_ticks()
    bg = Background()
    btn1 = ButtonUpd(WIDTH // 2 - 380, HEIGHT // 2 + 150, 180, 60)
    btn2 = ButtonUpd(WIDTH // 2 + 180, HEIGHT // 2 + 150, 180, 60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if go:
                if btn1.is_clicked(event, 1):
                    p.set_res(1, pygame.time.get_ticks())
                if btn2.is_clicked(event, 2):
                    p.set_res(2, pygame.time.get_ticks())
        if go:
            global res3
            if p.get_res()[0] != 0 and p.get_res()[1] != 0:
                res3 = [p.get_res()[0], p.get_res()[1], game_time * 1000]
                if abs(p.get_res()[0] - game_time * 1000) < abs(p.get_res()[1] - game_time * 1000):
                    show_text(f'{p.get_res()[0] / 1000}', (WIDTH // 2 - 360, HEIGHT // 4), 30,
                              'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
                    show_text(f'{p.get_res()[1] / 1000}', (WIDTH // 2 + 200, HEIGHT // 4), 30,
                              'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
                    if len(WINNER) == 2:
                        WINNER.append(1)
                        return
                elif abs(p.get_res()[0] - game_time * 1000) > abs(p.get_res()[1] - game_time * 1000):
                    show_text(f'{p.get_res()[0] / 1000}', (WIDTH // 2 + 200, HEIGHT // 4), 30,
                              'fonts/Orbitron-VariableFont_wght.ttf', BLACK)
                    show_text(f'{p.get_res()[1] / 1000}', (WIDTH // 2 + 200, HEIGHT // 4), 30,
                              'fonts/Orbitron-VariableFont_wght.ttf', BLACK)
                    if len(WINNER) == 2:
                        WINNER.append(2)
                        return
                else:
                    if len(WINNER) == 2:
                        WINNER.append('1 and 2')
                        return
        if pygame.time.get_ticks() - start > 2000 and go == 0:
            p = MyClock(game_time)
            go = 1
        screen.fill(BLACK)
        bg.draw_space()
        btn2.draw(f'{game_time} sec  -> ', (WIDTH // 2 + 180 + 50, HEIGHT // 2 + 150 + 20), 20,
                  'fonts/Orbitron-VariableFont_wght.ttf')
        btn1.draw(f'{game_time} sec  D', (WIDTH // 2 - 380 + 50, HEIGHT // 2 + 150 + 20), 20,
                  'fonts/Orbitron-VariableFont_wght.ttf')
        if go and p.get_res():
            p.draw()
            p.upd()
        else:
            show_text(f'{game_time} sec', (500, 100), 100, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        pygame.display.flip()
        clock.tick(FPS)


def res_screen():
    pygame.display.set_caption('Result')
    pygame.display.set_icon(load_image('all_img/icon1.bmp'))
    bg = Background()
    button = Button(WIDTH // 2 - 90, HEIGHT // 2 + 150, 180, 60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    run = False
        screen.fill(BLACK)
        bg.draw_space()
        show_text(f'{res3[0] / 1000}', (WIDTH // 2 - 380, HEIGHT // 4), 30,
                  'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text(f'{res3[1] / 1000}', (WIDTH // 2 + 280, HEIGHT // 4), 30,
                  'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text(f'{abs(res3[2] - res3[0]) / 1000}', (WIDTH // 2 - 330, HEIGHT // 4 + 50), 15,
                  'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text(f'{abs(res3[2] - res3[1]) / 1000}', (WIDTH // 2 + 330, HEIGHT // 4 + 50), 15,
                  'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player1', (300, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player2', (955, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        button.draw(f'Game 3 WINNER: {WINNER[-1]}', (WIDTH // 2 - 85, HEIGHT // 2 + 150 + 16), 15,
                    'fonts/Orbitron-VariableFont_wght.ttf')
        pygame.display.flip()
        clock.tick(FPS)


def finish_screen():
    bg = Background()
    button = Button(WIDTH // 2 - 90, HEIGHT // 2 + 150, 180, 60)

    class Particle(pygame.sprite.Sprite):

        fire = [load_image("all_img/circle.png")]
        for scale in (5, 7, 8, 10, 20):
            fire.append(pygame.transform.scale(fire[0], (scale, scale)))

        def __init__(self, pos, dx, dy):
            super().__init__(all_sprites)
            self.image = random.choice(self.fire)
            self.rect = self.image.get_rect()
            self.velocity = [dx, dy]
            self.rect.x, self.rect.y = pos
            self.gravity = 0.3

        def update(self):
            self.velocity[1] += self.gravity
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            if not self.rect.colliderect(pygame.Rect(0, 0, WIDTH, HEIGHT)):
                self.kill()

    def create_particles(position):
        particle_count = 20
        numbers = range(-5, 6)
        for _ in range(particle_count):
            Particle(position, random.choice(numbers), random.choice(numbers))

    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True
    create_particles((100, 100))
    sound1.play()
    create_particles((900, 200))
    sound1.play()
    create_particles((WIDTH // 2, 500))
    sound1.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound1.play()
                create_particles(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()
        screen.fill(BLACK)
        bg.draw_space()
        show_text(f'{WINNER.count(1)}', (320, 100), 100, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text(f'{WINNER.count(2)}', (970, 100), 100, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player1', (300, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        show_text('Player2', (955, 330), 30, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        if ''.join(list(map(str,WINNER))).count('1') > ''.join(map(str,WINNER)).count('2'):
            show_text('WINNER!!!', (300, 400), 40, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        elif ''.join(list(map(str,WINNER))).count('1') < ''.join(map(str,WINNER)).count('2'):
            show_text('WINNER!!!', (955, 400), 40, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        elif ''.join(list(map(str,WINNER))).count('1') == ''.join(map(str,WINNER)).count('2'):
            show_text('WINNER!!!', (695, 400), 40, 'fonts/Orbitron-VariableFont_wght.ttf', WHITE)
        button.draw('FINISH', (WIDTH // 2 - 90 + 30, HEIGHT // 2 + 150 + 13), 30,
                    'fonts/Orbitron-VariableFont_wght.ttf')
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


class Background():
    def __init__(self):
        self.bg = [(random.random() * WIDTH, random.random() * HEIGHT, random.randint(1, 2), random.randint(1, 2)) for _
                   in range(300)]

    def draw_space(self, color=pygame.Color('white'), fon=False):
        self.upd()
        for i in range(len(self.bg)):
            pygame.draw.circle(screen, color, (int(self.bg[i][0]), int(self.bg[i][1])), int(self.bg[i][2]))
        if fon:
            fon = pygame.transform.scale(load_image('all_img/name.png'), (650, 100))
            screen.blit(fon, (WIDTH // 2 - 650 // 2, HEIGHT // 2 - 200 // 2))

    def upd(self):
        for i in range(len(self.bg)):
            self.bg[i] = (
                (self.bg[i][0] + (self.bg[i][3] / 2)) % WIDTH, (self.bg[i][1] + (self.bg[i][3] / 2)) % HEIGHT,
                self.bg[i][2],
                self.bg[i][3])


class Button():
    def __init__(self, x, y, w, h):
        self.btn = (x, y, w, h)

    def draw(self, t, pos, size, font='fonts/MajorMonoDisplay-Regular.ttf'):
        pygame.draw.rect(screen, WHITE, self.btn)
        show_text(t, pos, size, font)

    def is_clicked(self, pos):
        if self.btn[0] <= pos[0] <= self.btn[0] + self.btn[2] and self.btn[1] <= pos[1] <= self.btn[1] + self.btn[3]:
            return True
        else:
            return False


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 240, 0)
PURPLE = (170, 90, 243)
FPS = 60
MYEVENTTYPE = pygame.USEREVENT + 1
WINNER = []
res3 = []
pygame.init()
size = WIDTH, HEIGHT = 1366, 706

screen = pygame.display.set_mode((int(WIDTH), int(HEIGHT)))
pygame.time.set_timer(MYEVENTTYPE, 10000)
clock = pygame.time.Clock()

if __name__ == '__main__':
    pygame.mixer.music.load('music/m2.mp3')
    pygame.mixer.music.play(-1)
    sound1 = pygame.mixer.Sound('music/btn.mp3')
    sound2 = pygame.mixer.Sound('music/btn2.mp3')
    start_screen()
    second_screen()
    third_screen()
    game1()
    wait_screen()
    game2()
    wait_screen()
    game3()
    res_screen()
    finish_screen()

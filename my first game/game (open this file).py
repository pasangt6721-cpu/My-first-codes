import pygame
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pasa Game")
icon = pygame.image.load('gg.jpg')
pygame.display.set_icon(icon)

# Load assets
background = pygame.image.load('backk.jpg')
ship_img = pygame.image.load('ship1.png')
bullet_img = pygame.image.load('bbb.png')
monster_img = pygame.image.load('monst.png')

mixer.music.load('background.wav')
mixer.music.play(-1)
bullet_sound = mixer.Sound('lase.wav')
explosion_sound = mixer.Sound('explosion.wav')

# Fonts
score_font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
menu_font = pygame.font.Font('freesansbold.ttf', 40)

# Game state
clock = pygame.time.Clock()
game_state = "menu"  # menu, playing, game_over, highscore
menu_index = 0
high_score = 0

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_img
        self.rect = self.image.get_rect(center=(400, 500))
        self.speed = 4.5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(self.rect.x, 736))  # clamp to screen

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.velocity = pygame.math.Vector2(0, -8)
        self.active = False

    def fire(self, x, y):
        self.rect.midbottom = (x + 32, y)  # center bullet on ship
        self.active = True
        bullet_sound.play()

    def update(self):
        if self.active:
            self.rect.move_ip(self.velocity)
            if self.rect.y < 0:
                self.active = False

    def draw(self, surface):
        if self.active:
            surface.blit(self.image, self.rect)

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = monster_img
        self.rect = self.image.get_rect(x=random.randint(0, 735), y=random.randint(50, 400))
        self.velocity = pygame.math.Vector2(random.choice([-1, 1]), 0)
        self.speed = 1.0

    def update(self):
        self.rect.x += self.velocity.x * self.speed
        if self.rect.x <= 0 or self.rect.x >= 736:
            self.velocity.x *= -1
            self.rect.y += 30

# Helper functions
def draw_text(text, font, x, y, selected=False):
    color = (255, 255, 255) if not selected else (255, 215, 0)
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def draw_score(score):
    score_render = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_render, (10, 10))

def draw_game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    restart_text = score_font.render("Press R to Restart | Press M for Menu", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    screen.blit(restart_text, (150, 320))

def draw_menu(selected_index):
    screen.fill((0, 0, 0))
    draw_text("PASA GAME", over_font, 240, 100)
    options = ["Play Game", "High Score", "Quit"]
    for i, option in enumerate(options):
        draw_text(option, menu_font, 300, 250 + i * 60, selected=(i == selected_index))
    draw_text(f"High Score: {high_score}", score_font, 10, 560)
    pygame.display.update()

def draw_highscore_screen():
    screen.fill((0, 0, 0))
    draw_text(f"High Score: {high_score}", over_font, 250, 250)
    draw_text("Press B to go back", score_font, 250, 320)
    pygame.display.update()

def create_monsters(num):
    return pygame.sprite.Group(*(Monster() for _ in range(num)))

# Game objects
player = Ship()
bullet = Bullet()
monsters = create_monsters(4)
score = 0
game_over = False

running = True
while running:
    clock.tick(60)
    if game_state == "menu":
        draw_menu(menu_index)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menu_index = (menu_index + 1) % 3
                elif event.key == pygame.K_UP:
                    menu_index = (menu_index - 1) % 3
                elif event.key == pygame.K_RETURN:
                    if menu_index == 0:
                        game_state = "playing"
                        player = Ship()
                        bullet = Bullet()
                        monsters = create_monsters(4)
                        score = 0
                        game_over = False
                    elif menu_index == 1:
                        game_state = "highscore"
                    elif menu_index == 2:
                        running = False

    elif game_state == "highscore":
        draw_highscore_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                game_state = "menu"

    elif game_state == "playing":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not game_over and event.key == pygame.K_SPACE and not bullet.active:
                    bullet.fire(player.rect.x, player.rect.y)
                elif game_over:
                    if event.key == pygame.K_r:
                        player = Ship()
                        bullet = Bullet()
                        monsters = create_monsters(4)
                        score = 0
                        game_over = False
                    elif event.key == pygame.K_m:
                        game_state = "menu"

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        if not game_over:
            player.update()
            bullet.update()
            monsters.update()

            # Collision detection
            for monster in monsters:
                if monster.rect.y > 350:
                    game_over = True
                if bullet.active and monster.rect.colliderect(bullet.rect):
                    explosion_sound.play()
                    bullet.active = False
                    score += 1
                    if score > high_score:
                        high_score = score
                    monster.rect.x = random.randint(0, 735)
                    monster.rect.y = random.randint(50, 200)

            monsters.draw(screen)
            bullet.draw(screen)
            screen.blit(player.image, player.rect)
            draw_score(score)
        else:
            draw_game_over()

        pygame.display.update()

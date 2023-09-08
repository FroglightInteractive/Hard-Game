import pygame
import random
from pygame import mixer

# Initialize Pygame
pygame.init()

# Initialize Mixer
mixer.init()
mixer.music.load("Hard Game Soundtrack/HardGameSoundtrack.mp3")
mixer.music.set_volume(0.1)


# Constants
WIDTH, HEIGHT = 400, 600
BACKGROUND_COLOR = ("gray")
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hard Game")
pygame_icon = pygame.image.load('assets/icon.ico')
pygame.display.set_icon(pygame_icon)


# Colors
GOLD = (255 , 215, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = ("green")
PURPLE = ("purple")
ORANGE = ("orange")

# Character (basket) properties
basket_width = 50
basket_height = 50
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 5

# Falling object properties
object_width = 20
object_height = 20
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Rare object properties
rare_width = 20
rare_height = 20
rare_x = None  #random.randint(0, WIDTH - rare_width)
rare_y = 0
rare_speed = 10

# Rare enemy properties
renemy_width = 50
renemy_height = 50
renemy_x = None
renemy_y = 0
renemy_speed = 20

# Extra Rare object properties
xrare_width = 20
xrare_height = 20
xrare_x = None
xrare_y = 0
xrare_speed = 15

# Enemy properties
enemy_width = 40
enemy_height = 40
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = 0
enemy_speed = 15

# Score
score = 0
font = pygame.font.Font(None, 36)

# Main game loop

clock = pygame.time.Clock()
running = True
gameloop = True
paused = False
gameOver = False
mixer.music.play()
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                gameloop = False

            keys = pygame.key.get_pressed()

            # Quit
            if keys[pygame.K_ESCAPE]:
                running = False
                gameloop = False

            # Pause
            if not gameOver:
                if keys[pygame.K_LSHIFT]:
                    pause_text = font.render("Game Paused", True, (0, 0, 0))
                    screen.blit(pause_text, (125, 300))
                    gameloop = False
                    paused = True
                if keys[pygame.K_SPACE]:
                    gameloop = True
                    paused = False

        # Restart
        if keys[pygame.K_r]:
            paused = False
            gameloop = True
            basket_x = (WIDTH - basket_width) // 2
            basket_y = HEIGHT - basket_height - 10
            score = 0
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_y = 0
            object_x = random.randint(0, WIDTH - object_width)
            object_y = 0
        if gameloop:
            if score >= -14 & score <= 99:

                if keys[pygame.K_a]:
                    basket_x -= basket_speed
                if keys[pygame.K_d]:
                    basket_x += basket_speed
                if keys[pygame.K_LEFT]:
                    basket_x -= basket_speed
                if keys[pygame.K_RIGHT]:
                    basket_x += basket_speed

                # Update falling object position
                object_y += object_speed

                # Update enemy position
                enemy_y += enemy_speed
                
                # Update renemy position
                if renemy_x is None:
                    if random.randint(1, 50) == 5:
                        renemy_x = random.randint(0, WIDTH - renemy_width)
                        renemy_y = 0
                else:
                    renemy_y += renemy_speed

                # Update rare position
                if rare_x is None:
                    if random.randint(1, 100) == 5:
                        rare_x = random.randint(0, WIDTH - rare_width)
                        rare_y = 0
                else:
                    rare_y += rare_speed
                    
                # Update xrare position
                if xrare_x is None:
                    if random.randint(1, 500) == 5:
                        xrare_x = random.randint(0, WIDTH - xrare_width)
                        xrare_y = 0
                else:
                    xrare_y += xrare_speed

                # Check for collisions
                
                # renemy
                if (
                        renemy_x is not None
                        and renemy_y + renemy_height >= basket_y
                        and basket_x <= renemy_x <= basket_x + basket_width
                ):
                    # renemy caught
                    score -= 10
                    renemy_x = None

                if renemy_y >= HEIGHT:
                    # renemy missed
                    renemy_x = None
                
                # xrare
                if (
                        xrare_x is not None
                        and xrare_y + xrare_height >= basket_y
                        and basket_x <= xrare_x <= basket_x + basket_width
                ):
                    # xrare caught
                    score += 10
                    xrare_x = None

                if xrare_y >= HEIGHT:
                    # xrare missed
                    xrare_x = None

                # Rare
                if (
                        rare_x is not None
                        and rare_y + rare_height >= basket_y
                        and basket_x <= rare_x <= basket_x + basket_width
                ):
                    # rare caught
                    score += 5
                    rare_x = None

                if rare_y >= HEIGHT:
                    # rare missed
                    rare_x = None

                # Object
                if (
                        object_y + object_height >= basket_y
                        and basket_x <= object_x <= basket_x + basket_width
                ):
                    # Object caught
                    score += 1
                    object_x = random.randint(0, WIDTH - object_width)
                    object_y = 0

                if object_y >= HEIGHT:
                    # Object missed
                    object_x = random.randint(0, WIDTH - object_width)
                    object_y = 0

                # Enemy
                if (
                        enemy_y + enemy_height >= basket_y
                        and basket_x <= enemy_x <= basket_x + basket_width
                ):
                    # Enemy Hit
                    score -= 5
                    enemy_x = random.randint(0, WIDTH - enemy_width)
                    enemy_y = 0

                if enemy_y >= HEIGHT:
                    # Enemy missed
                    enemy_x = random.randint(0, WIDTH - enemy_width)
                    enemy_y = 0
                # Clear the screen
                screen.fill(BACKGROUND_COLOR)
                # Draw the basket
                pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

                # Draw the RENEMY:
                if renemy_x is not None:
                    pygame.draw.rect(screen, ORANGE, (renemy_x, renemy_y, renemy_width, renemy_height))

                # Draw the XRARE object
                if xrare_x is not None:
                    pygame.draw.rect(screen, PURPLE, (xrare_x, xrare_y, xrare_width, xrare_height))

                # Draw the RARE object
                if rare_x is not None:
                    pygame.draw.rect(screen, GREEN, (rare_x, rare_y, rare_width, rare_height))

                # Draw the falling object
                pygame.draw.rect(screen, GOLD, (object_x, object_y, object_width, object_height))

                # Draw the enemy
                pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

                # Draw the score
                score_text = font.render(f"Score: {score}", True, (0, 0, 0))
                screen.blit(score_text, (10, 10))

            # Game Over
            if score <= -15:
                gameOver = True
                gameloop = False
                game_over = font.render("Game Over", True, (0, 0, 0))
                screen.blit(game_over, (125, 300))
                game_over_score = font.render(f"Score Was: {score}", True, (0, 0, 0))
                screen.blit(game_over_score, (100, 350))

            # Win
            if score >= 100:
                gameOver = True
                gameloop = False
                you_win = font.render("You Win!", True, (0, 0, 0))
                screen.blit(you_win, (125, 300))
                you_win_score = font.render(f"Score Was: {score}", True, (0, 0, 0))
                screen.blit(you_win_score, (100, 350))

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        clock.tick(FPS)

# Quit Pygame
pygame.quit()
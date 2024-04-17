# Final Project, Albert Laguerre, v0.0
import sys, random, pygame

resolution = 0  # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD!"))

pygame.display.set_caption('Basketball Game -- EASY')
pygame.display.set_caption('Basketball Game -- HARD')

if difficulty == 1:
    pygame.display.set_caption('Basketball Game -- EASY')
else:
    pygame.display.set_caption('Basketball Game -- HARD')
screen = pygame.display.set_mode((x, y))
# CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

# Set up the screen
screen_width = 800
screen_height = 600
screen = 0
pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#Fonts
font = pygame.font.SysFont(None, 50)

# Player
player_size = 50
player_color = red
player_x = screen_height // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# Computer Player
computer_color = blue
computer_size = 50
computer_x = screen_width // 2 - computer_size // 2
computer_y = 10
computer_speed = 3

# Ball
ball_radius = 15
ball_color = black
ball_x = screen_width // 2
ball_y = player_y - ball_radius
ball_speed = 5
ball_direction_x = 0
ball_direction_y = 0

# Score
player_score = 0
computer_score = 0

# Function to display score
def display_score():
    player_text = font.render(f"Player: {player_score}0", True, red)
    computer_text = font.render(f"Computer: {computer_score}", True, blue)
    screen.blit(player_text, (10, 10))
    screen.blit(computer_text, (screen_width - computer_text.get_width() - 10, 10))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Player Movement
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and player_x > 0:
    player_x -= player_speed
if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
    player_x += player_speed

# Computer Movement
if ball_y < screen_height // 2 and ball_direction_y < 0:
    if computer_x + computer_size // 2 < ball_x:
        computer_x += computer_speed
    elif computer_x + computer_size // 2 > ball_x:
        computer_x -= computer_speed

# Ball Movement
ball_x += ball_direction_x
ball_y += ball_direction_y

# Collision Detection with player
if ball_y + ball_radius >= player_y and player_x < ball_x < player_x + player_size:
    ball_direction_y = -ball_speed
    player_score += 1

# Collision Dectection with computer
if ball_y - ball_radius <= computer_y + computer_size and computer_x < ball_x < computer_x + computer_size:
    ball_direction_y = ball_speed
    computer_score += 1

# Ball out of bounds
if ball_y < 0 or ball_y > screen_height:
    ball_x = random.randint(ball_radius, screen_width - ball_radius)
    ball_y = player_y - ball_radius
    ball_direction_x = 0
    ball_direction_y = 0

# Update Screen
screen.fill(white)
pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
pygame.draw.rect(screen, computer_color, (computer_x, computer_y, computer_size, computer_size))
pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)


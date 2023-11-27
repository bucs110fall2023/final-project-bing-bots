import pygame
import sys
import random
import time
#import your controller

def main():
    #Create an instance on your controller object
    #Call your mainloop
    global timer
    global score
    global start_time

    start_time = pygame.time.get_ticks()

    while timer > 0:
        clock.tick(60)
        handle_events()
        update_game()
        draw_game()
        # if timer == pygame.USEREVENT: 
        #     timer -= 1

    # Show the final score
    screen.fill(BACKGROUND_COLOR)
    final_score_text = font.render(f'Congratulations, you finished the game with a score of {score}', True, TEXT_COLOR)
    screen.blit(final_score_text, (WIDTH // 2 - 300, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = "azure3"
MOLE_COLOR = "coral1"
HOLE_COLOR = "cadetblue4"
TEXT_COLOR = "black"
MOLE_RADIUS = 30
HOLE_SIZE = 60
TIMER_FONT_SIZE = 36
GAME_DURATION = 30
HOLE_POSITIONS = [(100, 100), (400, 100), (700, 100),
                  (100, 300), (400, 300), (700, 300),
                  (100, 500), (400, 500), (700, 500)]

# Set up display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")
clock = pygame.time.Clock()
# pygame.time.set_timer(pygame.USEREVENT, GAME_DURATION)


# Mole class
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.Color(MOLE_COLOR), (MOLE_RADIUS, MOLE_RADIUS), MOLE_RADIUS)
        self.image.fill(MOLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(HOLE_POSITIONS)
        self.hidden = True

    def show(self):
        self.hidden = False

    def hide(self):
        self.hidden = True
        self.rect.center = random.choice(HOLE_POSITIONS)

# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole.rect.colliderect(pygame.Rect(event.pos[0] - MOLE_RADIUS, event.pos[1] - MOLE_RADIUS, MOLE_RADIUS * 2, MOLE_RADIUS * 2)) and not mole.hidden:
                mole.hide()
                increase_score()

# Function to update game state
# def update_game():
#     global timer
#     global score
#     current_time = pygame.time.get_ticks()
#     if timer > 0:
#         # Randomly show/hide the mole
#         if random.random() < 0.02:
#             if mole.hidden:
#                 mole.show()
#             else:
#                 mole.hide()
#         if current_time % 1000 == 0:
#             # Update timer
#             timer -= 1
def update_game():
    global timer
    global score

    current_time = pygame.time.get_ticks()

    if timer > 0 and current_time - start_time >= 1000:
        # Randomly show/hide the mole
        if random.random() < 0.02:
            if mole.hidden:
                mole.show()
            else:
                mole.hide()

        # Update timer
        timer = GAME_DURATION - ((current_time - start_time) // 1000)

# Function to draw the game
def draw_game():
    screen.fill(BACKGROUND_COLOR)
    # Draw holes
    for pos in HOLE_POSITIONS:
        pygame.draw.circle(screen, HOLE_COLOR, pos, HOLE_SIZE)
    all_sprites.draw(screen)
    # Draw timer and score
    timer_text = font.render(f'Time: {timer}', True, TEXT_COLOR)
    score_text = font.render(f'Score: {score}', True, TEXT_COLOR)
    screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 50))
    pygame.display.flip()

# Function to increase the score
def increase_score():
    global score
    score += 1
    
# Set up timer and score
font = pygame.font.Font(None, TIMER_FONT_SIZE)
timer = GAME_DURATION
score = 0

# Create mole
mole = Mole()
all_sprites = pygame.sprite.Group(mole)

# Run the game loop
if __name__ == '__main__':
    main()

# End of the game
pygame.quit()
sys.exit()

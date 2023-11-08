import pygame
import sys
import random
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    global timer
    global score

    while timer > 0:
        handle_events()
        update_game()
        draw_game()
        clock.tick(60)

    # Show the final score
    screen.fill(BACKGROUND_COLOR)
    final_score_text = font.render(f'Congratulations, you finished the game with a score of {score}', True, TEXT_COLOR)
    screen.blit(final_score_text, (WIDTH // 2 - 280, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = "azure3"
MOLE_COLOR = "coral1"
HOLE_COLOR = "cadetblue4"
TEXT_COLOR = "black"
MOLE_RADIUS = 30
HOLE_SIZE = 60
TIMER_FONT_SIZE = 36
GAME_DURATION = 5
HOLE_POSITIONS = [(100, 100), (400, 100), (700, 100),
                  (100, 300), (400, 300), (700, 300),
                  (100, 500), (400, 500), (700, 500)]

# Set up display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")
clock = pygame.time.Clock()

# Mole class
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2))
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
            if mole.rect.collidepoint(event.pos) and not mole.hidden:
                mole.hide()
                increase_score()

# Function to update game state
def update_game():
    global timer
    global score

    if timer > 0:
        # Randomly show/hide the mole
        if random.random() < 0.02:
            if mole.hidden:
                mole.show()
            else:
                mole.hide()

        # Update timer
        if pygame.time.get_ticks() % 1000 == 0:
            timer -= 1

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

# Main game loop
def main():
    global timer
    global score

    while timer > 0:
        handle_events()
        update_game()
        draw_game()
        clock.tick(60)

    # Show the final score
    screen.fill(BACKGROUND_COLOR)
    final_score_text = font.render(f'Congratulations, you finished the game with a score of {score}', True, TEXT_COLOR)
    screen.blit(final_score_text, (WIDTH // 2 - 280, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting

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

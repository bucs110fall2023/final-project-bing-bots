# import pygame
# import sys
# import random

# # Constants
# WIDTH, HEIGHT = 800, 600
# BACKGROUND_COLOR = "azure3"
# MOLE_COLOR = "coral1"
# HOLE_COLOR = "cadetblue4"
# TEXT_COLOR = "black"
# BOX_COLOR = "lightsteelblue2"
# MOLE_RADIUS = 30
# HOLE_SIZE = 60
# TIMER_FONT_SIZE = 36
# GAME_DURATION = 30
# HOLE_POSITIONS = [(100, 100), (400, 100), (700, 100),
#                   (100, 300), (400, 300), (700, 300),
#                   (100, 500), (400, 500), (700, 500)]

# # Set up display
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Whack-a-Mole")
# clock = pygame.time.Clock()

# # Mole class
# class Mole(pygame.sprite.Sprite):
#     def __init__(self):
#         """Initialize the Mole sprite."""
#         super().__init__()
#         self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2))
#         self.image.fill(MOLE_COLOR)
#         self.rect = self.image.get_rect()
#         self.rect.center = random.choice(HOLE_POSITIONS)
#         self.hidden = True
#         self.last_toggle_time = 0

#     def show(self):
#         """Display the mole."""
#         self.hidden = False

#     def hide(self):
#         """Hide the mole and reset its position."""
#         self.hidden = True
#         self.rect.center = random.choice(HOLE_POSITIONS)

#     def can_toggle(self):
#         """Check if enough time has passed to toggle the mole's visibility."""
#         return pygame.time.get_ticks() - self.last_toggle_time >= 1000

# # Function to handle events
# def handle_events():
#     """Handle pygame events, such as quitting the game or clicking the mouse."""
#     global game_started
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if not game_started:
#                 start_game()
#             elif not mole.hidden and mole.rect.collidepoint(event.pos):
#                 mole.hide()
#                 increase_score()

# def update_game():
#     """Update the game state, including mole visibility and the game timer."""
#     global timer
#     global score
#     mole.update()

#     current_time = pygame.time.get_ticks()

#     if timer > 0 and current_time - start_time >= 1000:
#         # Randomly show/hide the mole
#         if random.random() < 0.02 and mole.can_toggle():
#             if mole.hidden:
#                 mole.show()
#             else:
#                 mole.hide()

#         # Update timer
#         timer = GAME_DURATION - ((current_time - start_time) // 1000)

# # Function to draw the game
# def draw_game():
#     """Draw the game elements on the screen, including holes, mole, timer, and score."""
#     screen.fill(BACKGROUND_COLOR)
#     # Draw holes
#     for pos in HOLE_POSITIONS:
#         pygame.draw.circle(screen, HOLE_COLOR, pos, HOLE_SIZE)
#     all_sprites.draw(screen)
#     # Draw timer and score
#     timer_text = font.render(f'Time: {timer}', True, TEXT_COLOR)
#     score_text = font.render(f'Score: {score}', True, TEXT_COLOR)
#     screen.blit(timer_text, (10, 10))
#     screen.blit(score_text, (10, 50))
#     pygame.display.flip()

# # Function to increase the score
# def increase_score():
#     """Increase the player's score."""
#     global score
#     score += 1

# # Function to display the final score
# def show_final_score():
#     """Display the final score on the screen."""
#     screen.fill(BACKGROUND_COLOR)
#     box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
#     pygame.draw.rect(screen, BOX_COLOR, box_rect)
#     final_score_text = font.render(f'Congratulations, you finished the game with a score of {score}', True, TEXT_COLOR)
#     text_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     screen.blit(final_score_text, text_rect)
#     pygame.display.flip()
#     pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting

# # Function to start the game
# def start_game():
#     """Start the game by initializing necessary variables."""
#     global timer
#     global score
#     global start_time
#     global game_started

#     timer = GAME_DURATION
#     score = 0
#     start_time = pygame.time.get_ticks()
#     game_started = True

# # Main game loop function
# def main_game_loop():
#     """Run the main game loop until the timer reaches zero."""
#     global timer
#     global score
#     global start_time
#     global game_started

#     start_time = pygame.time.get_ticks()
#     game_started = False

#     while True:
#         clock.tick(60)
#         handle_events()

#         if game_started:
#             update_game()
#             draw_game()
#         else:
#             draw_start_screen()
#         if timer <= 0:
#             show_final_score()
#             break


# # Function to draw the start screen
# def draw_start_screen():
#     """Draw the start screen with a 'Click to Play' message."""
#     screen.fill(BACKGROUND_COLOR)
#     box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
#     pygame.draw.rect(screen, BOX_COLOR, box_rect)
#     start_text = font.render("Click to Play", True, TEXT_COLOR)
#     text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     screen.blit(start_text, text_rect)
#     pygame.display.flip()

# # Set up timer and score
# font = pygame.font.Font(None, TIMER_FONT_SIZE)
# timer = GAME_DURATION
# score = 0
# start_time = 0
# game_started = False

# # Create mole
# mole = Mole()
# all_sprites = pygame.sprite.Group(mole)

# # Run the main game loop
# if __name__ == '__main__':
#     main_game_loop()

#     pygame.quit()
#     sys.exit()



# ####

import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = "azure3"
MOLE_COLOR = "coral1"
HOLE_COLOR = "cadetblue4"
TEXT_COLOR = "black"
BOX_COLOR = "lightsteelblue2"
PADDING = 20  # Padding for the final score box
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

# Mole class
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize the Mole sprite."""
        super().__init__()
        self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, MOLE_COLOR, (MOLE_RADIUS, MOLE_RADIUS), MOLE_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(HOLE_POSITIONS)
        self.hidden = True
        self.last_toggle_time = 0

    def show(self):
        """Display the mole."""
        self.hidden = False

    def hide(self):
        """Hide the mole and reset its position."""
        self.hidden = True
        self.rect.center = random.choice(HOLE_POSITIONS)

    def can_toggle(self):
        """Check if enough time has passed to toggle the mole's visibility."""
        return pygame.time.get_ticks() - self.last_toggle_time >= 1000


# Function to handle events
def handle_events():
    """Handle pygame events, such as quitting the game or clicking the mouse."""
    global game_started
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                start_game()
            elif not mole.hidden and mole.rect.collidepoint(event.pos):
                mole.hide()
                increase_score()

def update_game():
    """Update the game state, including mole visibility and the game timer."""
    global timer
    global score
    mole.update()

    current_time = pygame.time.get_ticks()

    if timer > 0 and current_time - start_time >= 1000:
        # Randomly show/hide the mole
        if random.random() < 0.02 and mole.can_toggle():
            if mole.hidden:
                mole.show()
            else:
                mole.hide()

        # Update timer
        timer = GAME_DURATION - ((current_time - start_time) // 1000)

# Function to draw the game
def draw_game():
    """Draw the game elements on the screen, including holes, mole, timer, and score."""
    screen.fill(BACKGROUND_COLOR)
    # Draw holes
    for pos in HOLE_POSITIONS:
        pygame.draw.circle(screen, HOLE_COLOR, pos, HOLE_SIZE)
    all_sprites.draw(screen)

    # Draw the mole as a circle
    if not mole.hidden:
        pygame.draw.circle(screen, MOLE_COLOR, mole.rect.center, MOLE_RADIUS)

    # Draw timer and score
    timer_text = font.render(f'Time: {timer}', True, TEXT_COLOR)
    score_text = font.render(f'Score: {score}', True, TEXT_COLOR)
    screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 50))
    pygame.display.flip()

# Function to increase the score
def increase_score():
    """Increase the player's score."""
    global score
    score += 1

# Function to display the final score
def show_final_score():
    """Display the final score on the screen."""
    screen.fill(BACKGROUND_COLOR)
    box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(screen, BOX_COLOR, box_rect)
    final_score_text = font.render(f'Congratulations, you finished the game with a score of {score}', True, TEXT_COLOR)
    text_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(final_score_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting

# Function to start the game
def start_game():
    """Start the game by initializing necessary variables."""
    global timer
    global score
    global start_time
    global game_started

    timer = GAME_DURATION
    score = 0
    start_time = pygame.time.get_ticks()
    game_started = True

# Main game loop function
def main_game_loop():
    """Run the main game loop until the timer reaches zero."""
    global timer
    global score
    global start_time
    global game_started

    start_time = pygame.time.get_ticks()
    game_started = False

    while True:
        clock.tick(60)
        handle_events()

        if game_started:
            update_game()
            draw_game()
        else:
            draw_start_screen()
        if timer <= 0:
            show_final_score()
            break


# Function to draw the start screen
def draw_start_screen():
    """Draw the start screen with a 'Click to Play' message."""
    screen.fill(BACKGROUND_COLOR)
    box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(screen, BOX_COLOR, box_rect)
    start_text = font.render("Click to Play", True, TEXT_COLOR)
    text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(start_text, text_rect)
    pygame.display.flip()

# Set up timer and score
font = pygame.font.Font(None, TIMER_FONT_SIZE)
timer = GAME_DURATION
score = 0
start_time = 0
game_started = False

# Create mole
mole = Mole()
all_sprites = pygame.sprite.Group(mole)

# Run the main game loop
if __name__ == '__main__':
    main_game_loop()

    pygame.quit()
    sys.exit()

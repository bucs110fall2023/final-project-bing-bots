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
# PADDING = 20  # Padding for the final score box
# MOLE_RADIUS = 30
# HOLE_SIZE = 60
# TIMER_FONT_SIZE = 36
# GAME_DURATION = 30  # in seconds
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
#         super().__init__()
#         self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2), pygame.SRCALPHA)
#         pygame.draw.circle(self.image, MOLE_COLOR, (MOLE_RADIUS, MOLE_RADIUS), MOLE_RADIUS)
#         self.rect = self.image.get_rect()
#         self.rect.center = random.choice(HOLE_POSITIONS)
#         self.hidden = True
#         self.last_toggle_time = 0

#     def show(self):
#         self.hidden = False

#     def hide(self):
#         self.hidden = True
#         self.rect.center = random.choice(HOLE_POSITIONS)

# # Function to check if a point is inside the mole
# def point_inside_mole(point, mole):
#     distance_squared = (point[0] - mole.rect.center[0]) ** 2 + (point[1] - mole.rect.center[1]) ** 2
#     return distance_squared <= MOLE_RADIUS ** 2

# # Function to handle events
# def handle_events(mole):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if point_inside_mole(event.pos, mole):
#                 mole.hide()
#                 increase_score()

# # Function to increase the score
# def increase_score():
#     global score
#     score += 1

# # Function to draw the start screen
# def draw_start_screen(font):
#     """Draw the start screen with a 'Click to Play' message."""
#     screen.fill(BACKGROUND_COLOR)
#     box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
#     pygame.draw.rect(screen, BOX_COLOR, box_rect)
#     start_text = font.render("Click to Play", True, TEXT_COLOR)
#     text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     screen.blit(start_text, text_rect)
#     pygame.display.flip()

# # Function to display the final score
# def show_final_score(font):
#     screen.fill(BACKGROUND_COLOR)
#     box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
#     pygame.draw.rect(screen, BOX_COLOR, box_rect)
#     final_score_text = font.render(f'Congratulations, you finished the game with a score of {score}', True, TEXT_COLOR)
#     text_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     screen.blit(final_score_text, text_rect)
#     pygame.display.flip()
#     pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting

# # Main game loop
# def main():
#     mole = Mole()
#     all_sprites = pygame.sprite.Group(mole)

#     global score
#     score = 0
#     font = pygame.font.Font(None, TIMER_FONT_SIZE)

#     start_time = pygame.time.get_ticks()
#     game_started = False  # Variable to track whether the game has started

#     while True:
#         clock.tick(60)

#         if not game_started:
#             draw_start_screen(font)
#             for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     game_started = True
#             pygame.display.flip()
#             continue  # Skip the rest of the loop until the game starts

#         handle_events(mole)

#         # Update game
#         current_time = pygame.time.get_ticks()
#         elapsed_time = (current_time - start_time) // 1000
#         remaining_time = max(GAME_DURATION - elapsed_time, 0)

#         if elapsed_time % 1 == 0:  # Toggle mole every 2 seconds
#             if random.random() < 0.02 and mole.hidden:
#                 mole.show()
#             elif not mole.hidden:
#                 mole.hide()
#             timer = GAME_DURATION - ((current_time - start_time) // 1000)

#         """Draw the game elements on the screen, including holes, mole, timer, and score."""
#         screen.fill(BACKGROUND_COLOR)
#         # Draw holes
#         for pos in HOLE_POSITIONS:
#             pygame.draw.circle(screen, HOLE_COLOR, pos, HOLE_SIZE)
#         all_sprites.draw(screen)

#         # Draw the mole as a circle
#         if not mole.hidden:
#             pygame.draw.circle(screen, MOLE_COLOR, mole.rect.center, MOLE_RADIUS)

#         # Draw timer and score
#         timer_text = font.render(f'Time: {timer}', True, TEXT_COLOR)
#         score_text = font.render(f'Score: {score}', True, TEXT_COLOR)
#         screen.blit(timer_text, (10, 10))
#         screen.blit(score_text, (10, 50))
#         pygame.display.flip()

#         # Check if the game has ended
#         if elapsed_time >= GAME_DURATION:
#             show_final_score(font)
#             pygame.quit()
#             sys.exit()

# if __name__ == "__main__":
#     main()

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
GAME_DURATION = 30  # in seconds
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
        self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, MOLE_COLOR, (MOLE_RADIUS, MOLE_RADIUS), MOLE_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(HOLE_POSITIONS)
        self.hidden = True
        self.last_toggle_time = 0

    def show(self):
        self.hidden = False

    def hide(self):
        self.hidden = True
        self.rect.center = random.choice(HOLE_POSITIONS)

# WhackAMoleGame class
class WhackAMoleGame:
    def __init__(self):
        self.mole = Mole()
        self.all_sprites = pygame.sprite.Group(self.mole)

        self.score = 0
        self.font = pygame.font.Font(None, TIMER_FONT_SIZE)

        self.start_time = pygame.time.get_ticks()
        self.game_started = False

    def point_inside_mole(self, point):
        distance_squared = (point[0] - self.mole.rect.center[0]) ** 2 + (point[1] - self.mole.rect.center[1]) ** 2
        return distance_squared <= MOLE_RADIUS ** 2

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.point_inside_mole(event.pos):
                    self.mole.hide()
                    self.increase_score()

    def increase_score(self):
        self.score += 1

    def draw_start_screen(self):
        screen.fill(BACKGROUND_COLOR)
        box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
        pygame.draw.rect(screen, BOX_COLOR, box_rect)
        start_text = self.font.render("Click to Play", True, TEXT_COLOR)
        text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(start_text, text_rect)
        pygame.display.flip()

    def show_final_score(self):
        screen.fill(BACKGROUND_COLOR)
        box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
        # pygame.draw.rect(screen, BOX_COLOR, box_rect)
        final_score_text = self.font.render(f'Congratulations, you finished the game with a score of {self.score}', True, TEXT_COLOR)
        text_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(final_score_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting

    def run(self):
        while True:
            clock.tick(60)

            if not self.game_started:
                self.draw_start_screen()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_started = True
                pygame.display.flip()
                continue

            self.handle_events()

            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) // 1000
            remaining_time = max(GAME_DURATION - elapsed_time, 0)

            if elapsed_time % 1 == 0:
                if random.random() < 0.02 and self.mole.hidden:
                    self.mole.show()
                elif not self.mole.hidden:
                    self.mole.hide()
                timer = GAME_DURATION - ((current_time - self.start_time) // 1000)

            screen.fill(BACKGROUND_COLOR)
            for pos in HOLE_POSITIONS:
                pygame.draw.circle(screen, HOLE_COLOR, pos, HOLE_SIZE)
            self.all_sprites.draw(screen)

            if not self.mole.hidden:
                pygame.draw.circle(screen, MOLE_COLOR, self.mole.rect.center, MOLE_RADIUS)

            timer_text = self.font.render(f'Time: {timer}', True, TEXT_COLOR)
            score_text = self.font.render(f'Score: {self.score}', True, TEXT_COLOR)
            screen.blit(timer_text, (10, 10))
            screen.blit(score_text, (10, 50))
            pygame.display.flip()

            if elapsed_time >= GAME_DURATION:
                self.show_final_score()
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    game = WhackAMoleGame()
    game.run()

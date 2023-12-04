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

# Mole class
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initializes the Mole object
        Arguments:
            self
        Return:
            none
        """
        super().__init__()
        self.image = pygame.Surface((MOLE_RADIUS * 2, MOLE_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, MOLE_COLOR, (MOLE_RADIUS, MOLE_RADIUS), MOLE_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = random.choice(HOLE_POSITIONS)
        self.hidden = True
        self.last_toggle_time = 0

    def show(self):
        """
        Sets the self.hidden value to False
        Arguments:
            self
        Return:
            none
        """
        self.hidden = False

    def hide(self):
        """
        Sets the self.hidden value to True and sets the center of the rect of the object to a random value from the list of hole positions.
        Arguments:
            self
        Return:
            none
        """
        self.hidden = True
        self.rect.center = random.choice(HOLE_POSITIONS)

# WhackAMoleGame class
class WhackAMoleGame:
    def __init__(self):
        """
        Initializes the WhackAMoleGame object
        Arguments:
            self
        Return:
            none
        """
        self.mole = Mole()
        self.all_sprites = pygame.sprite.Group(self.mole)

        self.score = 0
        self.font = pygame.font.Font(None, TIMER_FONT_SIZE)

        self.start_time = pygame.time.get_ticks()
        self.game_started = False

    def point_inside_mole(self, point):
        """
        Identifies whether or not the point that the player presses down on is inside the radius of the mole using the math module.
        Arguments:
            self
            point
        Return:
            a conditional statement that the distance_squared is <= the mole_radius squared
        """
        distance_squared = (point[0] - self.mole.rect.center[0]) ** 2 + (point[1] - self.mole.rect.center[1]) ** 2
        return distance_squared <= MOLE_RADIUS ** 2

    def handle_events(self):
        """
        Handles the events of the program
        Arguments:
            self
        Return:
            none
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.point_inside_mole(event.pos):
                    self.mole.hide()
                    self.increase_score()

    def increase_score(self):
        """
        Increases the score in the score tracker by 1 when called
        Arguments:
            self
        Return:
            none
        """
        self.score += 1

    def draw_start_screen(self):
        """
        Draws the "click to play" starter screen of the program
        Arguments:
            self
        Return:
            none
        """
        screen.fill(BACKGROUND_COLOR)
        box_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
        pygame.draw.rect(screen, BOX_COLOR, box_rect)
        start_text = self.font.render("Click to Play", True, TEXT_COLOR)
        text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(start_text, text_rect)
        pygame.display.flip()

    def show_final_score(self):
        """
        Draws the final score page where the final score of the player is shown and the player is congratulated.
        Arguments:
            self
        Return:
            none
        """
        screen.fill(BACKGROUND_COLOR)
        final_score_text = self.font.render(f'Congratulations, you finished the game with a score of {self.score}', True, TEXT_COLOR)
        text_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(final_score_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Display the final score for 3 seconds before quitting

    def run(self):
        """
        The main loop function where the actual program is being run.
        Arguments:
            self
        Return:
            none
        """
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
    # Set up display
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Whack-a-Mole")
    clock = pygame.time.Clock()
    game = WhackAMoleGame()
    game.run()
import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("the butten game")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse cursor's position
    mouse_pos = pygame.mouse.get_pos()

    # Get mouse button states
    mouse_button_1, mouse_button_2, mouse_button_3 = pygame.mouse.get_pressed()

    # Clear the screen
    screen.fill((245, 199, 140))
    
    pygame.draw.circle(screen, (161, 21, 8), (screen.get_width() / 2, screen.get_height() / 2), 50)
    pygame.draw.circle(screen, (211, 31, 18), (screen.get_width() / 2, screen.get_height() / 2 -8), 50)
    
    
    # Render
    pygame.display.flip()

pygame.quit()
sys.exit()



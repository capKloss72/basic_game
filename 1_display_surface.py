import pygame

pygame.init()

# Create a display surface and set caption
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption("Hello World")

# Main game loop
running = True

while running:
    # Loop through a list of event objects that have occurred
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


# End of game
pygame.quit()
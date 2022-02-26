import pygame

pygame.init()

# Create a display surface and set caption
WINDOW_WIDTH = 600
WINDOW_HIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption("Drawing Objects")

# Define colours as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (255, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Give a background colour to the display_surface
display_surface.fill(BLUE)

# Draw various shapes on display_surface
# Line(surface, colour, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)

# Circle(surface, colour, center, radius, thickness...0 for fill)
pygame.draw.circle(display_surface, YELLOW, (300, 300), 150, 10)
pygame.draw.circle(display_surface, WHITE, (300, 300), 140, 10)

# Rectangle(surface, colour, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 100, 100))

running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display_surface
    pygame.display.update()

pygame.quit()

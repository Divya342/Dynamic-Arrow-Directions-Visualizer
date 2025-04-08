import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arrow Directions")

# Colors
SKY_BLUE = (135, 206, 250)
MIDNIGHT_BLUE = (25, 25, 112)
ARROW_COLORS = {
    "UP": (0, 0, 255),
    "DOWN": (255, 0, 0),
    "LEFT": (0, 255, 0),
    "RIGHT": (255, 255, 0)
}

# Gradient background function
def draw_gradient():
    for i in range(SCREEN_HEIGHT):
        color = (
            SKY_BLUE[0] + (MIDNIGHT_BLUE[0] - SKY_BLUE[0]) * i // SCREEN_HEIGHT,
            SKY_BLUE[1] + (MIDNIGHT_BLUE[1] - SKY_BLUE[1]) * i // SCREEN_HEIGHT,
            SKY_BLUE[2] + (MIDNIGHT_BLUE[2] - SKY_BLUE[2]) * i // SCREEN_HEIGHT,
        )
        pygame.draw.line(screen, color, (0, i), (SCREEN_WIDTH, i))

# Draw arrows
def draw_arrow(x, y, direction, color):
    if direction == "UP":
        points = [(x, y - 50), (x - 30, y + 30), (x + 30, y + 30)]
    elif direction == "DOWN":
        points = [(x, y + 50), (x - 30, y - 30), (x + 30, y - 30)]
    elif direction == "LEFT":
        points = [(x - 50, y), (x + 30, y - 30), (x + 30, y + 30)]
    elif direction == "RIGHT":
        points = [(x + 50, y), (x - 30, y - 30), (x - 30, y + 30)]
    pygame.draw.polygon(screen, color, points)

# Main function
def main():
    clock = pygame.time.Clock()
    start_time = time.time()

    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        draw_gradient()  # Draw gradient background

        # Draw arrows
        draw_arrow(400, 200, "UP", ARROW_COLORS["UP"])
        draw_arrow(400, 600, "DOWN", ARROW_COLORS["DOWN"])
        draw_arrow(200, 400, "LEFT", ARROW_COLORS["LEFT"])
        draw_arrow(600, 400, "RIGHT", ARROW_COLORS["RIGHT"])

        pygame.display.flip()  # Update the display

        # Exit after 30 seconds
        if time.time() - start_time >= 30:
            running = False

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

# Run the program
if __name__ == "__main__":
    main()

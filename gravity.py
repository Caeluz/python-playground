import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
ball_radius = 20
ball_color = (255, 0, 0)
gravity = 0.5  # Acceleration due to gravity
bounce_factor = -0.7  # Factor to reduce velocity when the ball bounces
initial_velocity = -10
bounce_count_threshold = 5  # Set a threshold for the number of bounces
stop_bouncing = False  # Flag to stop the ball from bouncing

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Create the ball
ball_x = width // 2
ball_y = height // 2
ball_velocity = initial_velocity
bounce_count = 0  # Initialize the bounce count

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_y += ball_velocity
    time.sleep(0.02)
    ball_velocity += gravity
    # print(ball_velocity)

    # Bounce when hitting the ground
    if ball_y >= height - ball_radius:
        ball_y = height - ball_radius
        ball_velocity *= bounce_factor

        # Increment the bounce count
        bounce_count += 1
        print(bounce_count)

        # Stop bouncing after a certain number of bounces
        if bounce_count >= bounce_count_threshold:
            ball_velocity = 0
            stop_bouncing = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Exit the loop if the ball has stopped bouncing
    if stop_bouncing:
        break

# Quit Pygame (will be reached after breaking out of the loop)
pygame.quit()
import pygame
from snakeObjects import Apple, Snake


# Function to draw the background here
def draw_background():
    pygame.draw.rect(screen, black, [0, 0, 620, 620])
    pygame.draw.rect(screen, white, [10, 10, 600, 600])


# main
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode([620, 620])

# Set title of screen
pygame.display.set_caption("Snake Game")

# Set up all the variables needed
done = False
snakeAlive = False
frame = 0

# Set up all the objects that we need (and additional variables that are needed with an object)
snake = Snake()
apple = Apple(appleType="add")
next_direction = None

print(snake)  # Some 'debug' information for you here (prints a defined string for us)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while not done:  # Loop until the user clicks the close button.
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:  # User wants to
            if event.key == pygame.K_SPACE:
                snakeAlive = not snakeAlive
            if event.key == pygame.K_r and not snakeAlive:
                snake = Snake()
                apple = Apple(appleType="add")

        if event.type == pygame.KEYDOWN and snakeAlive:  # If user wants to perform a directional change to the snake
            if event.key == pygame.K_UP and snake.direction != "down":
                next_direction = "up"
            if event.key == pygame.K_DOWN and snake.direction != "up":
                next_direction = "down"
            if event.key == pygame.K_LEFT and snake.direction != "right":
                next_direction = "left"
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                next_direction = "right"

    # Move our snake if it isn't dead and depending on the frame we are on
    if frame % 10 == 0 and snakeAlive:
        # Move the snake in the direction it is facing or intending to face
        if next_direction is not None:
            snake.direction = next_direction
            next_direction = None
        isSnakeAlive = snake.move()

        if snake.location() == apple.location():  # Check if the snake is going to eat the apple
            occupiedSpace = snake.occupation()

            # Do an action to the snake based on what type of apple it ate
            if apple.type == "add":
                coords = snake.location()
                snake.body.addnode(coords[0], coords[1])
            elif apple.type == "remove":
                snake.body.removelast()
            else:  # The last remaining type, that it will be reversed
                snake.direction = snake.body.reverse(snake.direction)

            # Spawn a new apple at a location that the snake does not occupy
            apple = Apple([(x, y) for x in range(19) for y in range(19) if (x, y) not in occupiedSpace])

        else:  # If the snake is not going to eat the apple, check if it will still be alive
            snakeAlive = isSnakeAlive and not snake.collided()

    # Draw all our objects here in order: background -> apple -> leaf on top -> snake
    draw_background()
    leaf, leafCoords = apple.draw(screen)
    screen.blit(leaf, leafCoords)
    snake.draw(screen)

    clock.tick(60)  # Limit to 60 frames per second
    pygame.display.update()  # Go ahead and update the screen with what we've drawn.
    frame = (frame + 1) % 10  # Increment frame

# If you forget this line, the program will 'hang' on exit.
pygame.quit()

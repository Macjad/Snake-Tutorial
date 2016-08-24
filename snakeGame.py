import pygame, random
import snakeObjects

#Functions
def draw_background():
    pygame.draw.rect(screen, black, [0, 0, 620, 620])
    pygame.draw.rect(screen, white, [10, 10, 600, 600])


# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Initialize pygame
pygame.init()

screen=pygame.display.set_mode([620,620])

# Set title of screen
pygame.display.set_caption("Snake Game")

# Loop until the user clicks the close button.
done = False
dead = True
frame = 0
apple = 0
grid = [[0 for y in range( 20)] for x in range(20)]

#Snake object
snake = snakeObjects.Snake()
apple = snakeObjects.Apple()
next_direction = None
print(snake)

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dead = not dead
            if event.key == pygame.K_r and dead:
                snake.randomSpawn()
                apple = snakeObjects.Apple()

        if event.type == pygame.KEYDOWN and not dead: # If user wants to perform an action
            if event.key == pygame.K_UP and snake.direction != "down":
                next_direction = "up"
            if event.key == pygame.K_DOWN and snake.direction != "up":
                next_direction = "down"
            if event.key == pygame.K_LEFT and snake.direction != "right":
                next_direction = "left"
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                next_direction = "right"

    #Move our snake if it isn't dead and depending on our frame
    if frame%10 == 0 and not dead:
        if next_direction is not None:
            snake.direction = next_direction
            next_direction = None
        dead = snake.move()

        if snake.location() == apple.location():
            apple = snakeObjects.Apple(snake.occupation())

    # Draw all our objects here
    draw_background()
    snake.draw(screen)
    apple.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    #Increment frame
    frame = (frame + 1) % 10

# If you forget this line, the program will 'hang' on exit.
pygame.quit ()
import pygame
import random

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#The Snake class is our class to represent everything about the snake
class Snake:
    #Initialise our snake
    def __init__(self):
        self.randomSpawn()
        self.body = LinkedBody()

    def randomSpawn(self):
        self.x = random.randint(2,17)
        self.y = random.randint(2,17)
        self.direction = random.choice(["left", "right", "up", "down"])
        self.body = LinkedBody()

    def location(self):
        return (self.x, self.y)

    def move(self):
        dx, dy = 0, 0
        if self.direction == "left":
            dx = -1
        elif self.direction == "right":
            dx = 1
        elif self.direction == "up":
            dy = -1
        elif self.direction == "down":
            dy = 1

        if 0 <= self.x + dx <= 19 and 0 <= self.y + dy <= 19:
            self.body.move(self.x, self.y)
            self.x += dx
            self.y += dy
            return True
        return False

    def collision(self):
        return len(self.occupation()) == len(set(self.occupation()))

    def occupation(self):
        return [(self.x, self.y)] + self.body.occupation()

    def draw(self, screen):
        self.body.draw(screen)
        pygame.draw.rect(screen, green, [self.x*30+10, self.y*30+10, 30, 30])
        if self.direction == "left":
            pygame.draw.ellipse(screen, white, [self.x*30+12, self.y*30+14, 10, 10])
            pygame.draw.ellipse(screen, white, [self.x*30+12, self.y*30+26, 10, 10])
            pygame.draw.ellipse(screen, black, [self.x*30+13, self.y*30+17, 4, 4])
            pygame.draw.ellipse(screen, black, [self.x*30+13, self.y*30+29, 4, 4])
        elif self.direction == "right":
            pygame.draw.ellipse(screen, white, [self.x*30+28, self.y*30+14, 10, 10])
            pygame.draw.ellipse(screen, white, [self.x*30+28, self.y*30+26, 10, 10])
            pygame.draw.ellipse(screen, black, [self.x*30+33, self.y*30+17, 4, 4])
            pygame.draw.ellipse(screen, black, [self.x*30+33, self.y*30+29, 4, 4])
        elif self.direction == "up":
            pygame.draw.ellipse(screen, white, [self.x*30+14, self.y*30+12, 10, 10])
            pygame.draw.ellipse(screen, white, [self.x*30+26, self.y*30+12, 10, 10])
            pygame.draw.ellipse(screen, black, [self.x*30+17, self.y*30+13, 4, 4])
            pygame.draw.ellipse(screen, black, [self.x*30+29, self.y*30+13, 4, 4])
        elif self.direction == "down":
            pygame.draw.ellipse(screen, white, [self.x*30+14, self.y*30+28, 10, 10])
            pygame.draw.ellipse(screen, white, [self.x*30+26, self.y*30+28, 10, 10])
            pygame.draw.ellipse(screen, black, [self.x*30+17, self.y*30+33, 4, 4])
            pygame.draw.ellipse(screen, black, [self.x*30+29, self.y*30+33, 4, 4])
        
    #If you wish to print out the snake
    def __str__(self):
        return "<Snake location:({},{}) direction: {}>".format(self.x, self.y, self.direction)

        
#Linked_body class is the body of our snake, which will be represented as a linked list
class LinkedBody():
    #Initialise the overall shell of the body
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    
    #Return a boolean on whether there are any nodes
    def isEmpty(self):
        return self.length == 0

    def addNode(self, x, y): #For them to implement
        pass

    def draw(self, screen): #For them to implement
        pass

    def move(self, x, y): #For them to implement
        pass

    def occupation(self):
        return []


class BodyNode():
    #Initialise a node for the linked list
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
    
    #Draw the node
    def draw(self, screen):
        pygame.draw.rect(screen, green, [self.x*30+10, self.y*30+10, 30, 30])

    def __str__(self):
        return "<Node location: ({},{})>".format(self.x, self.y)


class Apple():
    def __init__(self, snakeLocation=None):
        if not snakeLocation:
            self.x = random.randint(0,19)
            self.y = random.randint(0,19)
        else:
            location = random.choice(snakeLocation)

            self.x = location[0]
            self.y = location[1]

    def location(self):
        return (self.x, self.y)

    def draw(self, screen):
        pygame.draw.ellipse(screen, red, [self.x*30+10, self.y*30+10, 30, 30])
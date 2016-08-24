import pygame
import random

green = (0, 255, 0)
red = (255, 0, 0)

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
            self.x += dx
            self.y += dy
            return False
        return True

    def occupation(self):
        return [(self.x, self.y)]

    def draw(self, screen):
        pygame.draw.ellipse(screen, green, [self.x*30+10, self.y*30+10, 30, 30])
        self.body.draw(screen)
        
    #If you wish to print out the snake
    def __str__(self):
        return "<Snake x: {}  y: {} Direction: {}>".format(self.x, self.y, self.direction)

        
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

    def addNode(self, x, y):
        pass

    def draw(self, screen):
        pass
        
        
class BodyNode():
    #Initialise a node for the linked list
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
    
    #Draw the node
    def draw_node(self, screen):
        pygame.draw.rect(screen, green, [self.x*30+10, self.y*30+10, 30, 30])


class Apple():
    def __init__(self, snakeLocation=None):
        if not snakeLocation:
            self.x = random.randint(0,19)
            self.y = random.randint(0,19)
        else:
            potentialLocation = (random.randint(0,19), random.randint(0,19))
            while potentialLocation in snakeLocation:
                potentialLocation = (random.randint(0,19), random.randint(0,19))

            self.x = potentialLocation[0]
            self.y = potentialLocation[1]

    def location(self):
        return (self.x, self.y)

    def draw(self, screen):
        pygame.draw.ellipse(screen, red, [self.x*30+10, self.y*30+10, 30, 30])
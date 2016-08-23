import pygame
import random

#The Snake class is our class to represent everything about the snake
class Snake:
    #Initialise our snake
    def __init__(self):
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        self.body = "nothing"
        
    #If you wish to print out the snake
    def __str__(self):
        return "Snek"
        
    #An unambiguous representation of the snake
    def __repr__(self):
        return "<Snake>"
        
#Linked_body class is the body of our snake, which will be represented as a linked list
class Linked_body():
    #Initialise the overall shell of the body
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    
    #Return a boolean on whether there are any nodes
    def isEmpty(self):
        return self.length == 0
        
        
class Body_node():
    #Initialise a node for the linked list
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
    
    #Draw the node
    def draw_node(self):
        pass
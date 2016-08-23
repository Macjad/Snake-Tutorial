import pygame

#Functions
def draw_background():


# Main program here
#Initialisation of variables and classes
#Initialise pygame
pygame.init()

#Set the pygame window so it is 800x800
window = pygame.display.set_mode([800,800]) 

pygame.display.set_caption("Snake")

done = False
start = False

clock = pygame.time.Clock()

#Program loop
while not done:
    draw_background()
    
    #Limit the game to 5 frames a second (1000ms/200)
    clock.tick(200)
    
    #Display what we are going to draw on the frame
    pygame.display.flip()
#End while loop here

#Don't hang the program on exit
pygame.quit()
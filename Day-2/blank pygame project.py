import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

# Create variables and stuff here if needed

running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add more events here, if needed

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely black
    screen.fill(black)

    #Game logic/drawing code goes here
    
    #update the entire display
    pygame.display.update()


pygame.quit()

import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 911x364 sized screen
screen = pygame.display.set_mode([512, 1024])
 
# This sets the name of the window
pygame.display.set_caption('CMSC 150 is cool')
 
clock = pygame.time.Clock()
  
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
background_image = pygame.image.load("heroofstorm.jpg")
player_image = pygame.image.load("hoswser.jpg")
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    x = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        

 
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
    screen.blit(player_image, [x, y])
 
    pygame.display.flip()
 
    clock.tick(60)

        
pygame.quit()

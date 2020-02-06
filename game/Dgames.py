
import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initializing the Pygame modules to get everything started.
pygame.init()
lose = False
win = False

# Setting the screen width and a height.
screen_width = 1490
screen_height = 780
size=screen_width,screen_height=1490, 780

# This creates the screen and gives it the width and height specified as a 2 item sequence.
screen = pygame.display.set_mode((screen_width,
                                  screen_height))

# This creates the player and gives the image found in my folder
bg= pygame.image.load("bgf.PNG")
bg=pygame.transform.scale(bg , size)
player = pygame.image.load("aliens.PNG")
prize = pygame.image.load("prize_sub.PNG")
enemy = pygame.image.load("missile.PNG")
enemy2 = pygame.image.load("missle_2.PNG")
enemy3 = pygame.image.load("missle_3.PNG")

# Getting the width and height of the images in order to do boundary detection
image_height = player.get_height()
image_width = player.get_width()
prize_height = player.get_height()
prize_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and enemy as variables so it can be changed
playerXPosition = 100
playerYPosition = 300

# Make the enemies start off at random position within the screen
enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)
enemy2XPosition = random.randint(200, screen_width - enemy2_width)
enemy2YPosition = screen_height
enemy3XPosition = random.randint(200, 700)
enemy3YPosition = 0
prizeX= random.randint(200, 700)
prizeY= random.randint(100, 300)

# Checks if the up or down key is pressed.
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# Game logic that needs to run over and over again.
# Screen has to updated as the game is running
# This in turn represents real time game play.

# This is a looping structure that will loop the indented code until one tells it to stop
# Clears the screen.
# Draws the player image to the screen at the position specfied initially
# will updates the screen with the flip() command
while 1:
    screen.fill(0)
    screen.blit(bg, (0,0))
    screen.blit(player, (playerXPosition,
                         playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeX, prizeY))

    pygame.display.flip()



    for event in pygame.event.get():             # This loops through events in the game.

        if event.type == pygame.QUIT:            # This event checks if the user quits the program, then if so it exits the program.
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:         # This event checks if the user press a key down.



            if event.key == pygame.K_UP:         # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            elif event.key == pygame.K_DOWN:
                keyDown = True
            elif event.key == pygame.K_LEFT:     # pygame.K_UP represents a keyboard key constant.
                keyLeft = True
            elif event.key == pygame.K_RIGHT:
                keyRight = True



        if event.type == pygame.KEYUP:          # This event checks if the key is up(i.e. not pressed by the user).

            if event.key == pygame.K_UP:        # Test if the key released is the one we want.
                keyUp = False
            elif event.key == pygame.K_DOWN:
                keyDown = False
            elif event.key == pygame.K_LEFT:
                keyLeft = False
            elif event.key == pygame.K_RIGHT:
                keyRight = False

    # checks key pressed values and move player accordingly.

    if keyUp == True:
        if playerYPosition > 0:                             # This makes sure that the user does not move the player above the window.
            playerYPosition -= 10
    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 10

    if keyLeft == True:
        if playerXPosition > 0:                             # This makes sure that the user does not move the player pass the outer most right side of the window in the x axis.
            playerXPosition -= 10
    if keyRight == True:
        if playerXPosition < screen_width - image_width:   # This makes sure that the user does not move the player pass the outer most left side of the window in the x axis.
            playerXPosition += 10

    # Checking for collisions of any enemy with the player.
    #Bounding boxes around the images of the player and enemy.
    # Bounding box for the player
    playerBox = pygame.Rect(player.get_rect())

    # Updates the playerBox position to the player's position,
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemies
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeY
    prizeBox.left = prizeX

    # Testing collisions of the boxes
    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit()
        exit(0)

    # Displays losing status to the user if collision occurs
    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    # If the user collects the gift prize a winning message is displayed
    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)


    # Make enemy approach the playerat a certain constant increment
    enemyXPosition -= 3
    enemy2YPosition -= 6
    enemy3YPosition += 9



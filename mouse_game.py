import pygame 

#pygame setup stuff
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('move the balls')
clock = pygame.time.Clock()
running = True 

dt = 0 
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2,)


while running:
    #pool for events 
    #pygame.quit() event closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pick the screen color 
    screen.fill("silver")

    #render our game here
    pygame.draw.circle(screen, "#033660", player_pos, 40)

    #move our circle 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt 

    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt 

    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt 

    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt 


    #use the mouse!
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        #print(pos)
        #move the circle
        player_pos.x = pos[0]
        player_pos.y = pos[1]

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)

    #flip the display to output our screen 
    pygame.display.flip()

    

    #set the clock stuff / delta time in seconds since the last frame
    # used for framerate independent physics
    dt = clock.tick(60) / 1000
        










pygame.quit()
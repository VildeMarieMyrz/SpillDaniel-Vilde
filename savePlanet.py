import pygame, pickle, sys

def save(planet, screen, screen_width, screen_height):
    font = pygame.font.Font(None,64)
    txt = ""
    box = pygame.Rect(screen_width/4,screen_height/4,screen_width/2,screen_height/2)
    box_color = pygame.Color("lightskyblue3")
    outline_color = (0,0,0)

    running = True
    while running:

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    chunks = [planet.positive_chunks, planet.negative_chunks]
                    pickle.dump(chunks, open("planets/"+txt+".planet","wb"))

                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    txt += event.unicode

        # Display
            # Box
        pygame.draw.rect(screen,box_color,box)
        #pygame.draw.rect(screen,outline_color,box,5)

            # Text
        screen.blit(font.render("What do you wish to name this planet?",True,(255,255,255)), (box.x + 45, box.y + 60))
        screen.blit(font.render(txt,True,(255,255,255)), (screen_width/2 - 200,screen_height/2))

        pygame.display.update()
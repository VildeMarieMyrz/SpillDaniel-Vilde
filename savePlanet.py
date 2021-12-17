import pygame, pickle, sys

def save(planet):
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption('Save Planet?')
    background_colour = (0, 0, 0)
    font = pygame.font.Font(None,32)
    txt = ""

    running = True
    while running:

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    chunks = [planet.positive_chunks, planet.negative_chunks]
                    pickle.dump(chunks, open("planets/"+txt+".planet","wb"))

                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                else:
                    txt += event.unicode

        # Display
            # Background
        screen.fill(background_colour)
        screen.blit(font.render(txt,True,(255,255,255)), (0,0))

        pygame.display.update()
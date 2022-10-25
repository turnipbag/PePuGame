import pygame, sys, random

player_list = ["Tapani", "Mikko"]
color_list = ["red", "green"]

player_info = list(zip(player_list, color_list))

clock = pygame.time.Clock()

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Test game")

players= []
texts = []
spot = 1
for player in player_info:
    name = player[0]
    color = player[1]

    turtle_surf = pygame.Surface((20,20))
    turtle_rect = turtle_surf.get_rect(center = (20, 20 + 40 * spot))

    font = pygame.font.SysFont("Times New Roman", 15)
    text_surf = font.render(name,False,color)
    text_rect = text_surf.get_rect(center = (25, 10 + 30 * spot))

    spot += 1

    players.append((turtle_surf,turtle_rect))
    texts.append((text_surf,text_rect))

finish_surf = pygame.Surface((40,720))
finish_rect = finish_surf.get_rect(center = (1200, 360))


speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    finish_surf.fill(("white"))

    display_surface.fill("black")
    display_surface.blit(finish_surf, finish_rect)

    #draw each player separately
    for player, color in zip(players,color_list):
        player[0].fill(color)
        display_surface.blit(player[0], player[1])
    for text in texts:
        display_surface.blit(text[0], text[1])

    """
    if not turtle_rect.colliderect(finish_rect):
        turtle_rect.x += 5
        text_rect.x += 5
    """
    clock.tick(60)


    

    pygame.display.update()
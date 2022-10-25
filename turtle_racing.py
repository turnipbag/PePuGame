import pygame, sys

clock = pygame.time.Clock()

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Test game")

turtle_surf = pygame.Surface((20,20))
turtle_rect = turtle_surf.get_rect(center = (10,360))

finish_surf = pygame.Surface((40,720))
finish_rect = finish_surf.get_rect(center = (1200, 360))

font = pygame.font.SysFont("Times New Roman", 15)
text_surf = font.render("TAPANI", False,(232, 193, 86))
text_rect = text_surf.get_rect(center = (10,340))

speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    turtle_surf.fill((232, 193, 86))
    finish_surf.fill(("white"))

    display_surface.fill("black")
    display_surface.blit(finish_surf, finish_rect)
    display_surface.blit(turtle_surf, turtle_rect)
    display_surface.blit(text_surf, text_rect)

    
    if not turtle_rect.colliderect(finish_rect):
        turtle_rect.x += 5
        text_rect.x += 5

    clock.tick(60)


    

    pygame.display.update()
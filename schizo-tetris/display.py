import pygame

pygame.init()
clock = pygame.time.Clock()
size = width, height = 540, 580
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SCHIZO TETRIS')
game_exists = True

# trial change
while game_exists:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exists = False
    pygame.draw.rect(screen, (0, 0, 0), [150, 10, 50, 20])
    pygame.display.flip()


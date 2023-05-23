import pygame
import math


def start():

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def tick(screen):
    
    mode = 0
    roots = []
    moving = False

    while True:

        screen.fill((0, 0, 0))
        show_roots(roots, screen)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            break
        elif key[pygame.K_q]:
            mode = 0
        elif key[pygame.K_a]:
            mode = 1
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                moving = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mode == 0:
                    roots.append(pygame.Rect((*pos, 10, 10)))
                elif  mode == 1:
                    moving = True
            elif event.type == pygame.MOUSEMOTION and moving:
                move_root(roots, pos, event.rel)
                

        pygame.display.update()

    pygame.quit()

def show_roots(roots, screen):
    for root in roots:
        pygame.draw.rect(screen, (255, 255, 255), root)

def move_root(roots: list[pygame.Rect], pos, rel):
    
    for root in roots:
        if math.dist(root.center, pos) <= 20:
            root.move_ip(rel)

if __name__ == '__main__':

    screen = start()

    tick(screen)

        
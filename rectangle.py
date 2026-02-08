import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("purple")
class rectangle():
    def __init__(self,w,h,x,y,c):
        self.h = h
        self.w = w
        self.x = x
        self.y = y
        self.c = c
    def draw(self):
        pygame.draw.rect(screen,self.c,(self.x,self.y,self.w,self.h))

r1 = rectangle(20,60,0,0,"black")
r1.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
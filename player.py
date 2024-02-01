import pygame as pg
import math

class PLAYER:
    def __init__(self, jw, wh):
        self.surf = pg.image.load('Sprite.png').convert_alpha()
        self.size = self.surf.get_size()
        self.pos = [jw/2 - self.size[0]/2, wh/2 - self.size[1]/2]
        self.vel = 5
        self.angle = 0

    def move(self):
        k = pg.key.get_pressed()
        vel_x = (k[pg.K_a] - k[pg.K_d]) * self.vel
        vel_y = (k[pg.K_w] - k[pg.K_s]) * self.vel

        mag = math.sqrt(vel_x**2 + vel_y**2)

        if mag != 0:
            vel_x, vel_y = vel_x / mag * self.vel, vel_y / mag * self.vel
        
        self.pos[0] -= vel_x
        self.pos[1] -= vel_y


    def rotate_img(self, tela):
        surf_copy = pg.transform.rotate(self.surf, self.angle)
        pos = (self.pos[0] - int(surf_copy.get_width()/2), self.pos[1] - int(surf_copy.get_height()/2))
        tela.blit(surf_copy, pos)
    
    def line(self, tela, mouse):
        pg.draw.line(tela, (255, 255, 255), self.pos, mouse)
        dx = mouse[0] - (self.pos[0] - 16)
        dy = mouse[1] - (self.pos[1] - 16)
        tangente = math.atan2(dx, dy)
        self.angle = int(math.degrees(tangente))

    def update(self, tela, mouse):
        self.move()
        self.line(tela, mouse)
        self.rotate_img(tela)



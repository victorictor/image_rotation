import pygame as pg
from sys import exit
from player import PLAYER
pg.init()

tela = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

pl = PLAYER(800, 600)
while True:
    tela.fill('gray20')

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            exit()
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_SPACE:
                pass

    mouse = pg.mouse.get_pos()
    pl.update(tela, mouse)
    pg.display.flip()
    clock.tick(60)
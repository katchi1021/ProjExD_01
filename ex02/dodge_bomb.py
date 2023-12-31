import sys
import pygame as pg
from random import randint

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    fps = 50
    vx = vy = 5
    key_lst = {pg.K_UP:(0, -5), pg.K_DOWN:(0, 5), pg.K_LEFT:(-5, 0), pg.K_RIGHT:(5, 0)}
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    bomb_sfc = pg.Surface((40, 40))
    bomb_sfc.set_colorkey((0,0,0))
    bomb = pg.draw.circle(bomb_sfc, (255,0,0), (20,20), 10)
    bomb.center = (randint(0,1600), randint(0,800))
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()


        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bomb_sfc, bomb)
        pg.display.update()
        bomb.move_ip((vx,vy))
        tmr += 1
        clock.tick(fps)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
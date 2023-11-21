import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    rev_bg = pg.transform.flip(bg_img, True, False)
    bgs = [bg_img, rev_bg]
    # img_rct = bg_img.get_rect()
    # img_rct.center = 800, 600
    kokaton = pg.image.load("ex01/fig/3.png")
    kokaton = pg.transform.flip(kokaton, True, False)
    kokatons = [pg.transform.rotozoom(kokaton, i*0.3, 1) for i in range(50)]
    kokatons += [pg.transform.rotozoom(i, -0.3, 1) for i in reversed(kokatons)]
    tmr = 0
    cnt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bgs[cnt], (-tmr,0))
        screen.blit(bgs[~cnt], (1600-tmr,0))
        screen.blit(kokatons[tmr%100], [300, 200])
        pg.display.update()
        # img_rct.move_ip(1, 0)
        tmr += 1
        if tmr >= 1600:
            tmr = 0
            cnt = ~cnt
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
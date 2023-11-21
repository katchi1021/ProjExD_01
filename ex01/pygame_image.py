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
    kokatons = [pg.transform.rotozoom(kokaton, i*0.1, 1) for i in range(100)]
    kokatons += [pg.transform.rotozoom(i, -0.1, 1) for i in reversed(kokatons)]
    tmr = 0
    dxy = [-0.2, 1]
    pxy = [300, 200]
    bg_cnt = 0
    cnt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                pxy[0] = x
                pxy[1] = y

        screen.blit(bgs[bg_cnt], (-tmr,0))
        screen.blit(bgs[~bg_cnt], (1600-tmr,0))
        screen.blit(kokatons[tmr%200], pxy)
        pg.display.update()
        # img_rct.move_ip(1, 0)
        pxy[0] += dxy[0]
        tmr += 1
        if tmr >= 1600:
            tmr = 0
            bg_cnt = ~bg_cnt
        if pxy[0] >= 700:
            dxy[0] = -0.2
        elif pxy[0] <= 200:
            dxy[0] = 1
    
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kokaton = pg.image.load("ex01/fig/3.png")
    kokaton = pg.transform.flip(kokaton, True, False)
    kokatons = [pg.transform.rotozoom(kokaton, i, 1) for i in range(10)]
    kokatons += [pg.transform.rotozoom(i, -1, 1) for i in reversed(kokatons)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(bg_img, [1600, 0])
        screen.blit(kokatons[tmr//10%20], [300, 200])
        pg.display.update()
        bg_img.scroll(tmr%1600,0)

        tmr += 1        
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
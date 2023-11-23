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
    #工科とん大量生成
    kokatons = [pg.transform.rotozoom(kokaton, i*0.2, 1) for i in range(50)]
    kokatons += [pg.transform.rotozoom(i, -0.2, 1) for i in reversed(kokatons)]
    tmr = 0
    dxy = [1, 1]
    pxy = [300, 200]
    bg_cnt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            #click event取得
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                pxy[0] = x
                pxy[1] = y
            elif event.type == "":
                pass
        #背景の置き換え
        screen.blit(bgs[bg_cnt], (-tmr,0))
        screen.blit(bgs[~bg_cnt], (1600-tmr,0))
        screen.blit(kokatons[tmr%100], pxy)
        #画面のアップデート
        pg.display.update()
        # img_rct.move_ip(1, 0)
        pxy[0] += dxy[0]
        pxy[1] += dxy[1]
        tmr += 1
        #背景のx表が1600以上移動したとき
        if tmr >= 1600:
            #タイマー初期化
            tmr = 0
            #背景画像を反転
            bg_cnt = ~bg_cnt
        if pxy[0] >= 700 or pxy[0] <= 200:
            dxy[0] *= -1
        if pxy[1] >= 500 or pxy[1] <= 100:
            dxy[1] *= -1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
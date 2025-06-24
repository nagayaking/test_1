import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
GROUND_HEIGHT = SCREEN_HEIGHT * 4 //5
LEFT_LINE = 40
RIGHT_LINE = SCREEN_WIDTH - 48
STAGE_WIDTH = 128 * 3
STAGE_HEIGHT = 128 * 1
scroll_x = 0
scroll_y = 0


check = [(0,0),(0,7),(7,0),(7,7)]

def get_tile(tile_x, tile_y):
    return pyxel.tilemaps[0].pget(tile_x, tile_y)

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title="game")
        pyxel.load("me.pyxres")
        self.player_x = 0
        self.player_dx = 0
        self.player_y = GROUND_HEIGHT - 8
        self.player_dy = 0
        self.jump = 0
        self.right = True
        self.is_flying = False
        pyxel.run(self.update,self.draw)



    def update(self):
        global scroll_x,scroll_y

        # 左方向へのスクロール
        if self.player_x < scroll_x + LEFT_LINE:
            scroll_x = self.player_x - LEFT_LINE
            if scroll_x < 0:
                scroll_x = 0

        # 右方向へのスクロール
        if scroll_x + RIGHT_LINE < self.player_x:
            scroll_x = self.player_x - RIGHT_LINE
            if SCREEN_WIDTH - pyxel.width < scroll_x:
                scroll_x = STAGE_WIDTH - pyxel.width

        print(self.player_x, scroll_x, pyxel.width)

        def chkwall(self,cx,cy):
            c = 0
            if pyxel.height < cy:
                c = c + 1               # 画面下に落ちたところで止める
            for cpx,cpy in check:
                xi = (cx + cpx)//8
                yi = (cy + cpy)//8
                if (5,0) == pyxel.tilemap(0).pget(xi,yi):
                    c = c + 1

            print(c)
            return c

        if self.jump == 0:
            if chkwall(self,self.player_x,self.player_y+1) == 0:
                self.jump = 2  # 床が無ければ落下
            if pyxel.btnp(pyxel.KEY_W):
                self.player_dy = 8
                self.jump = 1   # ジャンプ開始
        else:
            self.player_dy = self.player_dy - 1
            if self.player_dy < 0:
                self.jump = 2    # 頂点で落下開始

        ud = pyxel.sgn(self.player_dy)
        loop = abs(self.player_dy)
        while 0 < loop :
            if chkwall(self,self.player_x, self.player_y - ud) != 0:
                self.player_dy = 0
                if self.jump == 1:
                    self.jump = 2   # 壁にぶつかって落下
                elif self.jump == 2:
                    self.jump = 0   # 着地　落下終了
                break
            self.player_y = self.player_y - ud
            loop = loop -1


        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_A) and self.player_x > 0:
            self.player_x -= 1
            self.player_dx = -1
            self.right = False
        elif pyxel.btn(pyxel.KEY_D) and self.player_x + 8 < SCREEN_WIDTH:
            self.player_x += 1
            self.player_dx = 1
            self.right = True
    

        # 終了
        if pyxel.btnp(pyxel.KEY_ESCAPE) or self.player_y >= SCREEN_HEIGHT:
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_GRAY)
        pyxel.camera()
        pyxel.bltm(0,0, 0, scroll_x, scroll_y, pyxel.width,pyxel.height, 0)

        pyxel.camera(scroll_x,scroll_y)

        #キャラの向き
        if self.right:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 16, 8, 8, pyxel.COLOR_GRAY)
        else:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 16, -8, 8, pyxel.COLOR_GRAY)

App()
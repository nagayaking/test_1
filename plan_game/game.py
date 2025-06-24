import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
GROUND_HEIGHT = SCREEN_HEIGHT * 4 //5
FLYING_TIME = 0
GRAVITATIONA_ACCELERATION = 0.1

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
        self.flying_timer = FLYING_TIME
        self.accelerate = GRAVITATIONA_ACCELERATION
        self.right = True
        self.is_flying = False
        pyxel.run(self.update,self.draw)


    def chkwall(self,cx,cy):
        c = 0
        if cx < 0 or pyxel.width -8 < cx:
            c = c + 1
        if pyxel.height < cy:
            c = c + 1                  # 画面下に落ちたところで止める
        for cpx,cpy in check:
            xi = (cx + cpx)//8
            yi = (cy + cpy)//8
            if (1,0) == pyxel.tilemap(0).pget(xi,yi):
                c = c + 1
        return c
            


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()



        # 落下
        if self.player_y + 8 < GROUND_HEIGHT and not self.is_flying:
            self.player_y += 2

        # ジャンプ
        if pyxel.btn(pyxel.KEY_W) and GROUND_HEIGHT - self.player_y == 8:
            self.is_flying = True
        if self.is_flying:
            self.flying_timer += 1
            self.player_y -= 4
            if self.flying_timer == 10:
                self.is_flying = False
                self.flying_timer = FLYING_TIME
                


        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_A) and self.player_x > 0:
            self.player_x -= 1
            self.player_dx = -1
            self.right = False
        elif pyxel.btn(pyxel.KEY_D) and self.player_x + 8 < SCREEN_WIDTH:
            self.player_x += 1
            self.player_dx = 1
            self.right = True

    def draw(self):
        pyxel.cls(pyxel.COLOR_GRAY)
        pyxel.bltm(0, 0, 0, self.player_x, 0, 160, 120, pyxel.COLOR_BLACK)

        #キャラの向き
        if self.right:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 16, 8, 8, pyxel.COLOR_GRAY)
        else:
            pyxel.blt(self.player_x, self.player_y, 0, 0, 16, -8, 8, pyxel.COLOR_GRAY)

App()
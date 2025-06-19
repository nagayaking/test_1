import pyxel

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
GROUND_HEIGHT = SCREEN_HEIGHT * 4 //5
FLYING_TIME = 60

class Gravity:
    def __init__(self):
        self.accelerate = 0.1
        self.velocity = 0

    def update_gravity(self,y):
        self.velocity += self.accelerate
        y += self.velocity
        return y

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title="game")
        pyxel.load("me.pyxres")
        self.player_x = 0
        self.player_y = GROUND_HEIGHT - 16
        self.flying_timer = FLYING_TIME
        self.is_flying = False
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # 落下
        if self.player_y + 16 < GROUND_HEIGHT and not self.is_flying:
            self.player_y += 2

        # ジャンプ
        if pyxel.btn(pyxel.KEY_W) and GROUND_HEIGHT - self.player_y == 16:
            self.is_flying = True
        if self.is_flying:
            self.flying_timer -= 1
            self.player_y -= 1
            if self.flying_timer == 0:
                self.flying_timer = FLYING_TIME
                self.is_flying = False


        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_A) and self.player_x > 0:
            self.player_x -= 2
        elif pyxel.btn(pyxel.KEY_D) and self.player_x + 16 < SCREEN_WIDTH:
            self.player_x += 2

    def draw(self):
        pyxel.cls(pyxel.COLOR_GRAY)
        pyxel.blt(self.player_x, self.player_y, 0, 8, 0, 16, 16, pyxel.COLOR_GRAY)
        pyxel.rect(0, GROUND_HEIGHT, SCREEN_WIDTH, 10, pyxel.COLOR_GREEN)

App()
import random
import pygame
# 帧数刷新
FRAME_PER_SEC = 60
SCREEM_RECT = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name) # 图片引入
        self.rect = self.image.get_rect() #设置尺寸
        self.speed = speed
    def update(self, *args):
        self.rect.y += self.speed

class Backgroud(GameSprite):

    """GAME  BG"""
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height



    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEM_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEM_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEM_RECT.height:
            print("飞出屏幕")
            self.kill()
    def __del__(self):
        print("%s 销毁" % self.rect)


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEM_RECT.centerx
        self.rect.bottom = SCREEM_RECT.bottom - 120
        # 子弹精灵组
        self.bullets = pygame.sprite.Group()
    def update(self):
       self.rect.x += self.speed

       # 控制hero 不能离开屏幕
       if self.rect.x < 0:
           self.rect.x = 0
       elif self.rect.right > SCREEM_RECT.right:
           self.rect.right = SCREEM_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i *20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)




class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
    def __del__(self):
        print("子弹已经销毁")


from Plane_sprites import *
import pygame


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEM_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    def __create_sprites(self): #创建精灵方法和精灵组
        bg1 = Backgroud()
        bg2 = Backgroud(True)
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_Groud = pygame.sprite.Group()

    def start_game(self):
       # print("游戏开始。。。")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_spriites()
            pygame.display.update()



    def __event_handler(self): #事件监听方法
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #print("敌机出场")
                enemy = Enemy()
                self.enemy_Groud.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
                # 判断用户按下按钮
                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_RIGHT]:
                    self.hero.speed = 3
                elif keys_pressed[pygame.K_LEFT]:
                    self.hero.speed = -3
                else:
                    self.hero.speed = 0
    def __update_spriites(self): # 精灵组H更新和绘制
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_Groud.update()
        self.enemy_Groud.draw(self.screen)
        self.hero.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __check_collide(self): # 碰撞检测
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_Groud, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_Groud, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()
    @staticmethod
    def __game_over(): # 游戏结束方法
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__': # 判断是否在本主入口运行
    game = PlaneGame()
    game.start_game()
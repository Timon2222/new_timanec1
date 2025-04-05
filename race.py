from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Гонки')
background = transform.scale(image.load('background.jpg'), (700, 500))



clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y,  player_width, player_height, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (player_width, player_height))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):

        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 660: 
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update_car1(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >=  500:
            self.direction = 'down'
            self.rect.y = -60
            self.rect.x = randint(0, 635)
            lost = lost + 1
    def update_car2(self):
            self.rect.y += self.speed
            global lost
            if self.rect.y >=  500:
                self.direction = 'down'
                self.rect.y = -60
                self.rect.x = randint(0, 635)
                lost = lost + 1
    def update_car3(self):
            self.rect.y += self.speed
            global lost
            if self.rect.y >=  500:
                self.direction = 'down'
                self.rect.y = -60
                self.rect.x = randint(0, 635)
                lost = lost + 1
    def update_car4(self):
            self.rect.y += self.speed
            global lost
            if self.rect.y >=  500:
                self.direction = 'down'
                self.rect.y = -60
                self.rect.x = randint(0, 635)
                lost = lost + 1




car1 = Enemy('car1.jpg', 400, 400, 60, 80, 10)
car2 = Enemy('car2.png', 400, 400, 60, 80, 10)
car3 = Enemy('car3.png', 400, 400, 60, 80, 10)
car4 = Enemy('car3.png', 400, 400, 60, 80, 10)
racer = Player('car4.png', 400, 400, 60, 80, 10)



while game:
    if finish != True:
        window.blit(background,(0, 0))
        racer.update()
        racer.reset()
        car1.update_car1()
        car1.reset()
        car2.update_car2()
        car2.reset()
        car3.update_car3()
        car3.reset()
        car4.update_car4()
        car4.reset()
    for e in event.get():
            if e.type == QUIT:
                game = False

clock.tick(FPS)
display.update()
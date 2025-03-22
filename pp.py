from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 455: 
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 455: 
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, player_image,  player_x, player_y,  player_width, player_height, player_speed):
        super().__init__(player_image,  player_x, player_y,  player_width, player_height, player_speed)
        self.speed_x = self.speed
        self.speed_y =  self.speed
    def update(self):
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 650 or ball.rect.x <0:
            speed_x *= -1
        if ball.colliderect(platform.rect):
            speed_y *= -1
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
Ball = Ball('Ball.png')
racket1 = Player("Raketka.png", 600, 200, 80, 100, 10)
racket2 = Player("Raketka2.png", 20, 200, 80, 100, 10)
game = True
finish = False

while game:
    if finish != True:
        window.blit(background,(0, 0))
        Ball.update()
        Ball.draw(window)
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False
         
    clock.tick(FPS)
    display.update()
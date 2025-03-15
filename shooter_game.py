#Создай собственный Шутер
from random import randint
from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Космос')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

game = True
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
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)        

        pass
lost = 0
count = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >=  500:
            self.direction = 'down'
            self.rect.y = -60
            self.rect.x = randint(0, 635)
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <=  -10:
            self.kill()
bullets = sprite.Group()

 
monsters = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(80, 635), -80, 70, 50, randint(1,5))
    monsters.add(monster)


player = Player('rocket.png', 400, 400, 60, 80, 10)

font.init()
font2 = font.SysFont('Arial', 36)
text = font2.render('YOU LOSE!', 1, (255, 0, 0))
finish = False
score = 0
text2 = font2.render('YOU WIN!', 1, (255, 0, 0))
while game:
    if finish != True:
        window.blit(background,(0, 0))
        text_lose = font2.render('Улетело чуваков:' + str(lost), 1, (255, 255, 255))
        text_count = font2.render('Подсчет сбитых чуваков:' + str(score), 1, (255, 255, 255))
        window.blit(text_lose,(0, 10))
        window.blit(text_count,(0,35))
        bullets.update()
        bullets.draw(window)
        player.update()
        player.reset()
        monsters.update()
        monsters.draw(window)
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        if score >= 10:
            finish = True
            window.blit(text2,(300,200))
        for monster in sprites_list:
            score += 1
            monster = Enemy('ufo.png', randint(80,635), -80, 70, 50, randint(1,5))
            monsters.add(monster)
        if sprite.spritecollide(player, monsters, False):
            finish = True
            window.blit(text,(300,200))
        if lost >= 10:
            finish = True
            window.blit(text,(300,200))
    for e in event.get():
        if e.type == QUIT:
            game = False
        
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    clock.tick(FPS)
    display.update()
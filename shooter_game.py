from pygame import *
from random import *
font.init()

window = display.set_mode((700,500))
display.set_caption("Артем лох")
background = transform.scale(image.load("fon.png"), (700, 500))



number = 0
lost = 0

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def showhero(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

    def upravlenie(self):
        keys = key.get_pressed()
        if keys [K_LEFT]: 
            self.rect.x -= self.speed
        if keys [K_RIGHT]:
            self.rect.x += self.speed 

    
    def update(self):
        global number
        self.rect.y += self.speed
        if self.rect.y > 505:
            self.rect.y = randint(-40, -20)
            self.rect.x = randint(40, 650)
            number += 1

    def fire(self):
        bullet = Bullet ("bomb-transformed.png", self.rect.centerx - 4 , self.rect.y, 40, 40, 15)
        bullets.add(bullet)


class Bullet (GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 5:
            self.kill()


player = GameSprite('bird-transformed.png', 5, 420, 60, 60, 10)
monsters = sprite.Group()
for i in range(10):
    monster = GameSprite('pig-transformed.png', randint(40, 650), randint(-40, -20), 60, 60, randint(1, 2)) 
    monsters.add(monster)

font1 = font.Font(None, 36)
font2 = font.Font(None, 36)


bullets = sprite.Group()
 

mixer.init()
mixer.music.load("bb.ogg")
mixer.music.play()

clock = time.Clock()
FPS = 60

speed = 10

end = False

game = True
while game:
    if end != True:
        window.blit(background,(0,0))
        text_lose = font1.render("Пропущено: "  + str(number), 1, (255, 255, 255))
        text_lose1 = font1.render("Сбито: "  + str(lost), 1, (255, 255, 255))
        window.blit(text_lose,(10,10))
        window.blit(text_lose1,(10,40))
        
        player.showhero()
        monsters.draw(window)
        player.upravlenie()
        monsters.update()
        bullets.update()
        bullets.draw(window)
    
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys [K_SPACE]:
            player.fire()

    if sprite.groupcollide(monsters, bullets, True, True):
            lost = lost + 1
            monster = GameSprite('pig-transformed.png', randint(40, 650), randint(-40, -20), 60, 60, randint(1, 2)) 
            monsters.add(monster)
    
    
    if number > 20:
        text_loste = font1.render("LOSE", 1, (255, 255, 255))
        window.blit(text_loste, (250, 200))
        end = True
    
    elif lost > 10:
        text_win = font1.render("WIN", 1, (255, 255, 255))
        window.blit(text_win, (250 ,200))
        end = True


    clock.tick(FPS)
    display.update()
        

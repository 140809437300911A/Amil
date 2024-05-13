from pygame import*
class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 490:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed



   #метод "выстрел" (используем место игрока, чтобы создать там пулю)
  
back = (99,111,2)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60

game = True
finish = False


font.init()
font = font.SysFont('Arial', 40)
lose1 = font.render('Player 1 lose', True,(255, 255, 255))
lose2 = font.render('Player 2 lose', True,(255, 255, 255))
raket1 = Player('png-transparent-sporting-goods-tennis-racket-accessory-rakieta-tenisowa-tennis-racket-sport-sporting-goods-sports-equipment.png', 10, 10, 60, 100, 10)
raket2 = Player('png-transparent-sporting-goods-tennis-racket-accessory-rakieta-tenisowa-tennis-racket-sport-sporting-goods-sports-equipment.png',520, 10, 60, 100, 10)
score_text = font.render('Счёт', True, (255, 255, 255))
score_1_text = font.render('0', True, (255, 255, 255))
score_2_text = font.render('0', True, (255, 255, 255))


ball = GameSprite('galaxy.jpg', 200,200,30,30,30)

speed_x = 5
speed_y = 5

score_1 = 0
score_2 = 0


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        window.blit(score_text, (200,10))
        ball.rect.x +=speed_x
        ball.rect.y +=speed_y


        if sprite.collide_rect(ball, raket1): 
            speed_x = speed_x * -1
            score_1 +=1
            score_1_text = font.render(str(score_1), True, (255, 255, 255))
            

        if sprite.collide_rect(raket2, ball):
            speed_x = speed_x * -1
            score_2 +=1
            score_2_text = font.render(str(score_2), True, (255,255,255))

        if ball.rect.y<0 or ball.rect.y > 500 - 50:
            speed_y = speed_y * -1
        
        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(200, 200))
            game_over = True
        if ball.rect.x > 600:
            finish = True 
            window.blit(lose2,(200, 200))
            game_over = True
        window.blit(score_1_text, (20,10))
        window.blit(score_2_text, (400,10))



        raket1.update_l()
        raket2.update_r()
        raket1.reset()
        raket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)




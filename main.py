import pygame as pg


class Square:
    def __init__(self, pos, m, v, w):
            self.pos = pos
            self.mass = m
            self.velocity = v
            self.width = w

    def bounce(self):
        self.velocity *= -1

    def move(self):
        self.pos += self.velocity

    def newV(self, square):
        v1 = self.velocity
        self.velocity = (self.velocity*(self.mass - square.mass) + 2*square.mass*square.velocity)/(self.mass+square.mass)
        square.velocity =  (square.velocity*(square.mass - self.mass) + 2*self.mass*v1)/(self.mass+square.mass)


screens = (1000, 400)
screen = pg.display.set_mode(screens)
sq1 = Square(1000, 10000, -100, 80)
sq2 = Square(900, 1, 0, 40)

pi = 0

while 1:
    screen.fill((0, 0, 0))
    sqr1 = pg.draw.rect(screen, (255, 255, 0), pg.Rect(sq1.pos, 200, sq1.width, sq1.width))
    sqr2 = pg.draw.rect(screen, (255, 255, 0), pg.Rect(sq2.pos, 240, sq2.width, sq2.width))
    pg.display.flip()
    pg.time.delay(1000)
    sq1.move()
    sq2.move()
    if sq1.pos <= 0:
        sq1.bounce()

    if sq2.pos <= 0:
        sq2.bounce()
        pi += 1
    if sq2.pos+sq2.width >= sq1.pos:
        sq2.newV(sq1)
        pi += 1
    print(pi)

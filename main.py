#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame, random, time
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480
 
# Clases
# ---------------------------------------------------------------------
 
class Yoda(pygame.sprite.Sprite):
        def __init__(self, x):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/yoda.png",True)
                self.rect = self.image.get_rect()
                self.rect.centerx = x
                self.rect.centery = HEIGHT / 2
                self.speed = 0.4
 
        def mover(self, time, keys):
                if self.rect.top >= 0:
                        if keys[K_UP]:
                                self.rect.centery -= self.speed * time
                if self.rect.bottom <= HEIGHT:
                        if keys[K_DOWN]:
                                self.rect.centery += self.speed * time
                if self.rect.left >= 0:
                        if keys[K_LEFT]:
                                self.rect.centerx -= self.speed * time
                if self.rect.right <= WIDTH:
                        if keys[K_RIGHT]:
                                self.rect.centerx += self.speed * time

                                
class Laser(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/rayoLaser.png")
                self.rect = self.image.get_rect()
                self.rect.centerx = 625
                self.rect.centery = random.randint(50,430)
                self.speed = 0.3       # Variar dificultad

        def mover(self, time):       
                self.rect.centerx -= self.speed * time


# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
                try: image = pygame.image.load(filename)
                except pygame.error, message:
                                raise SystemExit, message
                image = image.convert()
                if transparent:
                                color = image.get_at((0,0))
                                image.set_colorkey(color, RLEACCEL)
                return image

def texto(texto, posx, posy, color=(255, 255, 255)):
        fuente = pygame.font.Font('images/DroidSans.ttf', 25)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
# ---------------------------------------------------------------------
 
def main():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Yoda")
        pun=0
 
        background_image = load_image('images/fondo.jpg')
        yoda_jug = Yoda(30)
        laser = Laser()
 
        clock = pygame.time.Clock()

        pygame.mixer.music.load('sound/starWars.mid')
        pygame.mixer.music.play(-1,0.0)
 
        while True:
                time = clock.tick(60)
                keys = pygame.key.get_pressed()
                for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                                pygame.mixer.music.stop()
                                sys.exit(0)
                yoda_jug.mover(time, keys)      
                laser.mover(time)
                puntuacion, puntuacion_rect = texto(str(pun), WIDTH-WIDTH/4, 40)
                screen.blit(background_image, (0, 0))
                screen.blit(yoda_jug.image, yoda_jug.rect)
                screen.blit(laser.image, laser.rect)
                screen.blit(puntuacion, puntuacion_rect)
                if pygame.sprite.collide_rect(yoda_jug, laser):              
                        laser = Laser()
                        pun+=50
                if laser.rect.left <= 0:
                        over = pygame.image.load("images/gameover.jpg")
                        screen.blit(over,(0,0))
                        screen.blit(puntuacion, puntuacion_rect)
                        pygame.display.update()
                pygame.display.flip()
        return 0
 
if __name__ == '__main__':
        pygame.init()
        main()

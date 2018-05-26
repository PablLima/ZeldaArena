# #! /usr/bin/env python
#
# import os
# import random
# import pygame
#
# # Class for the orange dude
# class Player(object):
#
#     def __init__(self):
#         self.imagem_link = pygame.image.load('link.png')
#
#         #criando a hitbox
#         self.rect = self.imagem_link.get_rect()
#
#     def move(self, dx, dy):
#
#         # Move each axis separately. Note that this checks for collisions both times.
#         if dx != 0:
#             self.move_single_axis(dx, 0)
#         if dy != 0:
#             self.move_single_axis(0, dy)
#
#     def move_single_axis(self, dx, dy):
#
#         # Move the rect
#         self.rect.x += dx
#         self.rect.y += dy
#
#         # If you collide with a wall, move out based on velocity
#         for wall in walls:
#             if self.rect.colliderect(wall.rect):
#                 if dx > 0: # Moving right; Hit the left side of the wall
#                     self.rect.right = wall.rect.left
#                 if dx < 0: # Moving left; Hit the right side of the wall
#                     self.rect.left = wall.rect.right
#                 if dy > 0: # Moving down; Hit the top side of the wall
#                     self.rect.bottom = wall.rect.top
#                 if dy < 0: # Moving up; Hit the bottom side of the wall
#                     self.rect.top = wall.rect.bottom
#
# # Nice class to hold a wall rect
# class Wall(object):
#
#     def __init__(self, pos):
#         walls.append(self)
#         self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#
# # Initialise pygame
# os.environ["SDL_VIDEO_CENTERED"] = "1"
# pygame.init()
#
# # Set up the display
# pygame.display.set_caption("Get to the red square!")
# screen = pygame.display.set_mode((320, 240))
#
# clock = pygame.time.Clock()
# walls = [] # List to hold the walls
# player = Player() # Create the player
#
# # Holds the level layout in a list of strings.
# level = [
# "WWWWWWWWWWWWWWWWWWWW",
# "W                  W",
# "W         WWWWWW   W",
# "W   WWWW       W   W",
# "W   W        WWWW  W",
# "W WWW  WWWW        W",
# "W   W     W W      W",
# "W   W     W   WWW WW",
# "W   WWW WWW   W W  W",
# "W     W   W   W W  W",
# "WWW   W   WWWWW W  W",
# "W W      WW        W",
# "W W   WWWW   WWW   W",
# "W     W    E   W   W",
# "WWWWWWWWWWWWWWWWWWWW",
# ]
#
# # Parse the level string above. W = wall, E = exit
# x = y = 0
# for row in level:
#     for col in row:
#         if col == "W":
#             Wall((x, y))
#         if col == "E":
#             end_rect = pygame.Rect(x, y, 16, 16)
#         x += 16
#     y += 16
#     x = 0
#
# running = True
# while running:
#
#     clock.tick(60)
#
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#         if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
#             running = False
#
#     # Move the player if an arrow key is pressed
#     key = pygame.key.get_pressed()
#     if key[pygame.K_LEFT]:
#         player.move(-2, 0)
#     if key[pygame.K_RIGHT]:
#         player.move(2, 0)
#     if key[pygame.K_UP]:
#         player.move(0, -2)
#     if key[pygame.K_DOWN]:
#         player.move(0, 2)
#
#     # Just added this to make it slightly fun ;)
#     if player.rect.colliderect(end_rect):
#         raise SystemExit, "You win!"
#
#     # Draw the scene
#     screen.fill((0, 0, 0))
#     for wall in walls:
#         pygame.draw.rect(screen, (255, 255, 255), wall.rect)
#     pygame.draw.rect(screen, (255, 0, 0), end_rect)
#     pygame.draw.rect(screen, (255, 200, 0), player.rect)
#     pygame.display.flip()

# Pygame template - skeleton for a new pygame project
import pygame
import random
from pygame.locals import *

largura = 360
altura = 480
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
imagemlink = ['cima.png','baixo.png','esq.png','dir.png']
# initialize pygame and create window

all_sprites = pygame.sprite.Group()

class Monstros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largura - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3,3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > altura + 10 or self.rect.left < -25 or self.rect.right > largura + 25:
            self.rect.x = random.randrange(largura - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

#criando o player
class link (pygame.sprite.Sprite) :
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_link = pygame.image.load(imagemlink[0])

        #criando a hitbox
        self.rect = self.imagem_link.get_rect()

        #posição do jogador
        self.rect.centerx = largura/2
        self.rect.centery = altura - 100


        #Adicionais do jogo
        self.listaDisparo = []
        self.vida = True
        self.velocidade = 10


    def movimento_direita (self) :
        self.rect.right += self.velocidade
        self.movimento()

    def movimento_esquerda (self) :
        self.rect.left -= self.velocidade
        self.movimento()

    # pra não passar da tela
    def __movimento (self):
        if self.vida == True :
            if self.rect.left <= 0 :
                self.rect.left = 0

            elif self.rect.right >= 0:
                self.rect =1200


    # def movimento (self):
    #     if self.vida == True :
    #
    #         #não sair a esquerda
    #         if self.rect.left <= 0 :
    #           self.rect.left = 0
    #
    #         #não sair a direita
    #         elif self.rect.right >= 1200 :
    #             self.rect.right = 1200


    def atacar (self, x, y):
        minha_espada= espada (x,y)
        self.listaDisparo.append(minha_espada)


    #para colocar algo na tela
    def colocar(self, superficie) :
        superficie.blit(self.imagem_link,self.rect)

#Varíaveis pré-jogo
# Game loop

def zelda():
    running = True
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    jogador = link()
    imagem_fundo = pygame.image.load('arena.png')
    all_sprites = pygame.sprite.Group()
    monstros = pygame.sprite.Group()
    for i in range(8):
        m = Monstros()
        all_sprites.add(m)
        monstros.add(m)
    while True:

        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

            # teclas pressionadas
            if event.type == pygame.KEYDOWN:

                if event.key == K_LEFT:
                    jogador.imagem_link = pygame.image.load(imagemlink[2])
                    jogador.rect.left -= jogador.velocidade


                elif event.key == K_RIGHT:
                    jogador.imagem_link = pygame.image.load(imagemlink[3])
                    jogador.rect.right += jogador.velocidade

                 #movimento cima e baixo FORA DO TUTO
                # if evento.key == K_UP:
                #     jogador.rect.up += jogador.velocidade
                #
                # if evento.key == K_DOWN :
                #     jogador.rect.down += jogador.velocidade

                 #movimento cima e baixo FORA DO TUTO
                if event.key == K_UP:
                    jogador.imagem_link = pygame.image.load(imagemlink[0])
                    jogador.rect.top -= jogador.velocidade
                if event.key == K_DOWN :
                    jogador.imagem_link = pygame.image.load(imagemlink[1])
                    jogador.rect.bottom += jogador.velocidade

        # checa a colisão do monstro com o jogador
        hits = pygame.sprite.spritecollide(jogador, monstros, False)
        if hits:
            zelda()
        # atualiza todos os sprites
        all_sprites.update()



        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        jogador.colocar(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

zelda()

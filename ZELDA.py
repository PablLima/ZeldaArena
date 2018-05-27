import pygame,sys
import random
from pygame.locals import *

# Tamanho da tela
largura=1200
altura=640
imagemlink = ['cima.png','baixo.png','esq.png','dir.png']

# Pede no inicio do jogo se será tela cheia (1) ou janela (0)
#telacheia=int(input(0))
# Por enquanto, o padrão é janela
telacheia=0

# Variáveis de cores
RED=(255,255,0)
YELLOW = (255, 255, 0)

class espada (pygame.sprite.Sprite) :
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_espada = pygame.image.load('espada.png')

        self.rect = self.imagem_espada.get_rect()
        self.velocidade_espada = 5
        self.rect.top = posy
        self.rect.left = posx

    #trajetoria da espada
    def trajetoria (self) :
        self.rect.top = self.rect.top - self.velocidade_espada

    #para colocar espada na tela
    def colocar (self, superficie) :
        superficie.blit(self.imagem_espada, self.rect)



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


    #def atacar (self, x, y):
    #    minha_espada= espada (x,y)
    #    self.listaDisparo.append(minha_espada)
    def atacar (self, x, y):
        minha_espada= espada (x-22,y-75)
        self.listaDisparo.append(minha_espada)

    #para colocar algo na tela
    def colocar(self, superficie) :
        superficie.blit(self.imagem_link,self.rect)


    ###QUANDO QUISER BOTAR QUALQUER COMANDO OU AÇÃO FAZER UMA DEF AQUI
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
        if self.rect.top > altura + 10:
            self.rect.x = random.randrange(largura - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# class hitAmigo(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface ((10, 20))
#         self.image.fill(YELLOW)
#         self.rect = self.image.get_rect()
#         self.rect.botton = y
#         self.rect.centerx = x
#         self.speedy = -10
#
#     def update(self):
#         self.rect.y += self.speedy
#         # se sair fora da tela
#         if self.rect.bottom < 0:
#             self.kill()

#Varíaveis pré-jogo
# all_sprites = pygame.sprite.Group()
# monstros = pygame.sprite.Group()
# hitamigos = pygame.sprite.Group()
# for i in range(8):
#     m = Monstros()
#     all_sprites.add(m)
#     monstros.add(m)
#começa o game
def zelda ():
    pygame.init()

    #Define se será tela cheia ou janela
    if telacheia == 0:
        tela = pygame.display.set_mode((largura,altura))
    else:
        tela = pygame.display.set_mode((largura,altura),pygame.FULLSCREEN)

    pygame.display.set_caption('ZELDA ARENA')

    jogador = link()
    imagem_fundo = pygame.image.load('arena.png')

    #para mudar se algo o fizer parar de jogar
    jogando=True

    #daonde sai a espada
    espada_link = espada (largura / 2, altura - 100)

#FPS
    relogio = pygame.time.Clock()



#fecha o game e bota os objetos

    while True :
        #FPS
        relogio.tick(60)

        #pra iniciar a bareira e não passar do lado
        #jogador.movimento()

        espada_link.trajetoria()

        #evento q fecha o game
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                #isso ^ é igual a um break
                #break


        #movimentação do personagem
        if evento.type == pygame.KEYDOWN:

            if evento.key == K_LEFT:
                jogador.imagem_link = pygame.image.load(imagemlink[2])
                jogador.rect.left -= jogador.velocidade


            elif evento.key == K_RIGHT:
                jogador.imagem_link = pygame.image.load(imagemlink[3])
                jogador.rect.right += jogador.velocidade

             #movimento cima e baixo FORA DO TUTO
            # if evento.key == K_UP:
            #     jogador.rect.up += jogador.velocidade
            #
            # if evento.key == K_DOWN :
            #     jogador.rect.down += jogador.velocidade

             #movimento cima e baixo FORA DO TUTO
            if evento.key == K_UP:
                jogador.imagem_link = pygame.image.load(imagemlink[0])
                jogador.rect.top -= jogador.velocidade
            else:
                jogador.rect.top += 0
            if evento.key == K_DOWN :
                jogador.imagem_link = pygame.image.load(imagemlink[1])
                jogador.rect.bottom += jogador.velocidade
            else:
                jogador.rect.top += 0



            #ataque
            if evento.key == K_SPACE:
                x,y = jogador.rect.center
                jogador.atacar (x,y)

        #colocar os objetos na  tela
        tela.blit(imagem_fundo, (0, 0))
        jogador.colocar(tela)

        if len(jogador.listaDisparo) > 0 :
            for z in jogador.listaDisparo :
                z.colocar(tela)
                z.trajetoria()

                #limitar aonde o tiro vai
                if z.rect.top < (jogador.rect.center[1]-50) :
                    jogador.listaDisparo.remove(z)
                    print(jogador.listaDisparo)


        pygame.display.update()



zelda()

import pygame,sys
from pygame.locals import *
import random
global jogadorcentery
jogadorcentery = 0
# Tamanho da tela
largura=1280
altura=720

# CORES PRÉ-DEFINIDAS
YELLOW = (255, 255, 0)

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('ZELDA ARENA')
#FPS
tempo = pygame.time.Clock()

class Monstros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ghost.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largura - self.rect.width)
        self.rect.y = altura
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > altura + 10 or self.rect.left < -25 or self.rect.right > largura + 25:
            self.rect.x = random.randrange(largura - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
    #def colocar(self, superficie) :
    #   superficie.blit(self.image,self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -20
    def update(self):
        self.rect.y += self.speedy
        #print(pygame.time.Clock())
        # morre se sair fora da tela
        #if self.rect.bottom < 0:
        #    self.kill()
        if direcao == "left" and self.rect.centery < jogador.rect.centery - 30:
            self.kill()
        if direcao == "right" and self.rect.centery < jogador.rect.centery - 30:
            self.kill()
        if direcao == "up" and self.rect.centery < jogador.rect.centery - 75:
            self.kill()

        # Essa macacagem gera bug na espada pra baixo
        if direcao == "down":
            self.speedy = +20
            if self.rect.centery > jogador.rect.centery + 50:
                self.kill()

#criando o player
class link (pygame.sprite.Sprite) :
    def __init__(self):
        global imagem_link
        imagem_link = ['cima.png', 'baixo.png', 'esq.png', 'dir.png']
        pygame.sprite.Sprite.__init__(self)
        self.imagem_link = pygame.image.load(imagem_link[0])
        #criando a hitbox
        self.rect = self.imagem_link.get_rect()
        #posição do jogadors
        self.rect.centerx = largura/2
        self.rect.centery = altura - 100
        #Adicionais do jogo
        self.listaDisparo = []
        self.vida = True
        self.velocidade = 50
    def movimento (self):
        if self.vida == True :
            #não sair a esquerda
            if self.rect.left <= 0 :
              self.rect.left = 0
            #não sair a direita
            elif self.rect.right >= 1280 :
                self.rect.right = 1280
            # não sair para cima
            elif self.rect.top >= 530:
                self.rect.top = 530
            # não sair a baixo
            elif self.rect.bottom <= 180:
                self.rect.bottom = 180


    #def atacar (self, x, y):
    #    minha_espada= espada (x-22,y-75)
    #    self.listaDisparo.append(minha_espada)
    #para colocar algo na tela
    def shoot(self):
        if direcao == "left":
            bullet = Bullet(self.rect.centerx - 160, self.rect.centery + 70)
            bullet.image = pygame.image.load('espada_esq.png')
        if direcao == "right":
            bullet = Bullet(self.rect.centerx + 60, self.rect.centery + 75)
            bullet.image = pygame.image.load('espada_dir.png').convert()
        if direcao == "up":
            bullet = Bullet(self.rect.centerx + 10, self.rect.centery + 30)
            bullet.image = pygame.image.load('espada.png')
        if direcao == "down":
            bullet = Bullet(self.rect.centerx, self.rect.centery)
            bullet.image = pygame.image.load('espada_baixo.png')
        all_sprites.add(bullet)
        bullets.add(bullet)
    def colocar(self, superficie) :
        superficie.blit(self.imagem_link,self.rect)

# class orc (pygame.sprite.Sprite) :
#     def __init__(self, posx, posy):
#         pygame.sprite.Sprite.__init__(self)
#        #imagne sdo inimigo
#         self.imagem_orc1 = pygame.image.load('inimigo.png')
#         self.imagem_orc2 = pygame.image.load('orc2.png')
#         #lista para borar varios inimigos
#         self.lista_imagens = [self.imagem_orc1 , self.imagem_orc2]
#         self.pos_imagem = 0
#         self.imagem_inimigo = self.lista_imagens [self.pos_imagem]
#         self.rect = self.imagem_inimigo.get_rect()
#         self.listadisparo = []
#         self.velocidade  = 10
#         self.rect.top = posy
#         self.rect.left = posx
#         #tempo de spawn dos inimigos
#         self.spawn_inimigo = 10
#     #trajetoria da espada
#     def comportamento (self,tempo) :
#         if self.spawn_inimigo == tempo :
#             self.pos_imagem += 1
#             self.spawn_inimigo += 1
#             if self.pos_imagem > len(self.lista_imagens)-1 :
#                 self.pos_imagem = 0
#     #para colocar espada na tela
#     def colocar (self, superficie) :
#         self.imagem_inimigo = self.lista_imagens[self.pos_imagem]
#         superficie.blit(self.imagem_inimigo, self.rect)

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

    ###QUANDO QUISER BOTAR QUALQUER COMANDO OU AÇÃO FAZER UMA DEF AQUI
#começa o game
global flag
flag = False
#bullets = pygame.sprite.Group()

# Sons do jogo
pygame.mixer.music.load('zelda.ogg')
pygame.mixer.music.play(loops=1)

somespada = pygame.mixer.Sound('sword.wav')
sommorte = pygame.mixer.Sound('dead2.wav')
somacerto = pygame.mixer.Sound('hit.wav')
sompasso = pygame.mixer.Sound('walk.wav')
def zelda ():
    global direcao
    global bullets
    global all_sprites
    global jogador
    global first
    font = pygame.font.Font(None, 54)
    font_color = pygame.Color('yellow')
    inimigosmortos=0
    direcao = "up"
    first = 0
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    monstros = pygame.sprite.Group()
    jogador = link()
    imagem_fundo = pygame.image.load('arena.png')
    #para mudar se algo o fizer parar de jogar
    jogando=True

    #daonde sai a espada
    espada_link = espada (largura / 100 , altura - 150)

    #gerar monstros
    for i in range(20):
        m = Monstros()
        all_sprites.add(m)
        monstros.add(m)

    # LOOP DO JOGO
    while True :

        #FPS
        tempo.tick(60)
        #relogio do jogo
        #tempo = int(pygame.time.get_ticks()/1000)
        #pra iniciar a bareira e não passar do lado
        jogador.movimento()
        espada_link.trajetoria()
        #evento q fecha o game
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                #isso ^ é igual a um break
                #break
                # movimentação do personagem

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT or evento.key == K_RIGHT or evento.key == K_UP or evento.key == K_DOWN:
                    pygame.mixer.Sound.play(sompasso)
                    if evento.key == K_LEFT:
                        jogador.imagem_link = pygame.image.load(imagem_link[2])
                        jogador.rect.left -= jogador.velocidade
                        # debug
                        if jogador.rect.left < jogador.rect.left + jogador.velocidade:
                            direcao = "left"
                    elif evento.key == K_RIGHT:
                        jogador.imagem_link = pygame.image.load(imagem_link[3])
                        jogador.rect.right += jogador.velocidade
                        # debug
                        if jogador.rect.right > jogador.rect.right - jogador.velocidade:
                            direcao = "right"
                    elif evento.key == K_UP:
                        jogador.imagem_link = pygame.image.load(imagem_link[0])
                        jogador.rect.top -= jogador.velocidade
                        # debug
                        if jogador.rect.top < jogador.rect.top + jogador.velocidade:
                            direcao = "up"
                    elif evento.key == K_DOWN:
                        jogador.imagem_link = pygame.image.load(imagem_link[1])
                        jogador.rect.bottom += jogador.velocidade
                        # debug
                        if jogador.rect.bottom > jogador.rect.bottom - jogador.velocidade:
                            direcao = "down"
                #ataque
                elif evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    #jogadorcentery = jogador.rect.centery
                    #print(jogadorcentery)
                    #if direcao == "down":
                    #    jogador.speedy = +20
                    jogador.shoot()
                    #first = pygame.time.get_ticks()
                    #print(pygame.time.get_ticks())
                    pygame.mixer.Sound.play(somespada)
                    #jogador.atacar(x,y)
                elif evento.type == pygame.KEYUP:
                        jogador.rect.top += 0

        if (first + 2000) < pygame.time.get_ticks():
            flag = True
        #colocar os objetos na  tela
        tela.blit(imagem_fundo, (0, 0))
        jogador.colocar(tela)
        #inimigo.colocar(tela)
        #inimigo.comportamento(tempo)
        #monstros.update(tela(0,0))
        # if len(jogador.listaDisparo) > 0 :
        #     for z in jogador.listaDisparo :
        #         z.colocar(tela)
        #         z.trajetoria()
        #         #limitar aonde o tiro vai
        #         if z.rect.top < 455 :
        #             jogador.listaDisparo.remove(z)
        #Checa colisão
        hits = pygame.sprite.groupcollide(bullets, monstros, True, True)
        for hit in hits:
            pygame.mixer.Sound.play(somacerto)
            inimigosmortos+=1
            m = Monstros()
            all_sprites.add(m)
            monstros.add(m)
        hits = pygame.sprite.spritecollide(jogador, monstros, False)
        if hits:
            pygame.mixer.Sound.play(sommorte)
            #zelda()
        #hits2 = pygame.sprite.spritecollide(bullets, monstros, True)
    #oq acontece depois de 'morrer'
            #all_sprites.remove(m)
            #monstros.remove(m)
            #zelda()
        #if hits2:
        #    print(len(monstros),'monstros restantes.')
        text = font.render(str(inimigosmortos), True, font_color)
        text2 = font.render(str("Combo:"), True, font_color)
        tela.blit(text, (110, 80))
        tela.blit(text2, (50, 40))

        all_sprites.update()
        all_sprites.draw(tela)
        pygame.display.update()
zelda()

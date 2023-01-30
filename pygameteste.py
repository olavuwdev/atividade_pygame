import pygame
import random
import time

pygame.init()
janela = (1280, 720)
tela = pygame.display.set_mode(janela)
pygame.display.set_caption("Biblioteca PYGAME")

# Define a cor de fundo
fundo = (255, 255, 255)

# Definir o tamanho e a cor do bloco preto
tamanho_do_bloco = (50, 50)
cor_do_bloco = (0, 0, 0)
posição_do_bloco = [janela[0]//2, janela[1]//2]

# Variável para controlar o tempo da última geração de bloco vermelho
time_block = 0

# Lista de blocos vermelhos na tela
blocos_vermelhos = []

# velocidade do bloco
v_do_bloco = 1

# Loop de jogo
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    # Verificar as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        posição_do_bloco[1] -= v_do_bloco
    if keys[pygame.K_DOWN]:
        posição_do_bloco[1] += v_do_bloco
    if keys[pygame.K_LEFT]:
        posição_do_bloco[0] -= v_do_bloco
    if keys[pygame.K_RIGHT]:
        posição_do_bloco[0] += v_do_bloco
    
    # Verificar se é hora de gerar um novo bloco vermelho
    current_time = time.time()
    if current_time - time_block >= 4:
        size = (random.randint(20, 100), random.randint(20, 100))
        position = [random.randint(0, janela[0]-size[0]), random.randint(0, janela[1]-size[1])]
        color = (255, 0, 0)
        blocos_vermelhos.append((size, position, color))
        time_block = current_time
    
    # Verificar colisões entre blocos vermelhos e o bloco preto
    for i, (size, position, color) in enumerate(blocos_vermelhos):
        if position[0] < posição_do_bloco[0] + tamanho_do_bloco[0] and \
           position[0] + size[0] > posição_do_bloco[0] and \
           position[1] < posição_do_bloco[1] + tamanho_do_bloco[1] and \
           position[1] + size[1] > posição_do_bloco[1]:
            blocos_vermelhos.pop(i)
            break
    
    # Preencher a tela com a cor de fundo
    tela.fill(fundo)
    
    # Desenhar os blocos vermelhos
    for size, position, color in blocos_vermelhos:
        pygame.draw.rect(tela, color, (position[0], position[1], size[0], size[1]))
    
    # Desenhar o bloco preto
    pygame.draw.rect(tela, cor_do_bloco, (posição_do_bloco[0], posição_do_bloco[1], tamanho_do_bloco[0], tamanho_do_bloco[1]))
    
    # Atualizar a tela
    pygame.display.update()

# Encerrar programa
pygame.quit()

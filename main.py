import pygame
import constantes

pygame.init()

size = constantes.ALTO_VENTANA, constantes.ANCHO_VENTANA

screen = pygame.display.set_mode(size)

run = True
while run == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
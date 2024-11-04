import pygame
import constantes
from personaje import Personaje



pygame.init()

#INICIO Y CONFIGURACION DE VENTANA:
size = constantes.ALTO_VENTANA, constantes.ANCHO_VENTANA
ventana_level1 = pygame.display.set_mode(size)
pygame.display.set_caption('ISLAND PY')

#CREACION DEL PERSONAJE:
jugador = Personaje(50,50)

#VARIABLES MOVIMIENTO:
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#RELOJ PARA CONTROLAR FRAMERATE:
reloj = pygame.time.Clock()

#BUCLE DONDE SE EJECUTA EL JUEGO:
run = True
while run:

	#RELOJ A 60 FPS
	reloj.tick(constantes.FPS)

	#PARA RELLENAR EL FONDO CUANDO SE MUEVA EL PERSONAJE
	ventana_level1.fill(constantes.COLOR_BG)

	#CALCULAR MOVIMIENTO JUGADOR:
	delta_x = 0
	delta_y = 0
	if mover_derecha:
		delta_x = constantes.VELOCIDAD
	if mover_izquierda:
		delta_x = -constantes.VELOCIDAD
	if mover_abajo:
		delta_y = constantes.VELOCIDAD
	if mover_arriba:
		delta_y = -constantes.VELOCIDAD

	#MOVER AL JUGADOR
	jugador.movimiento(delta_x, delta_y)



	for event in pygame.event.get():


		#EVENTO PARA FINALIZAR EL JUEGO:
		if event.type == pygame.QUIT:
			run = False

		#TECLAS MOVIMIENTO:
		#CUANDO PULSAMOS:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				mover_izquierda = True
			if event.key == pygame.K_s:
				mover_abajo = True
			if event.key == pygame.K_d:
				mover_derecha = True
			if event.key == pygame.K_w:
				mover_arriba = True

		#CUANDO LEVANTAMOS:
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				mover_izquierda = False
			if event.key == pygame.K_s:
				mover_abajo = False
			if event.key == pygame.K_d:
				mover_derecha = False
			if event.key == pygame.K_w:
				mover_arriba = False

	#DIBUJAR JUGADOR EN VENTANA
	jugador.dibujar(ventana_level1)

	#ACTUALIZAR PANTALLA CON CAMBIOS
	pygame.display.update()
pygame.quit()
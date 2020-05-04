import pygame, sys #Importa modulo pygame y modulo sistema

#Creación de pantalla
width = 640
height = 480

screen = pygame.display.set_mode((width, height))#Enseña la pantalla
screen.fill((246, 147, 48))#da color a la pantalla, (rojo, verde, azul)
pygame.display.set_caption("Ciclo básico de pygame")

pygame.init()#Inicia pygame, (pygame.font.init(), por si no funciona solo con el init

#ciclo (pintar pantalla, manejar pantalla, modificar pantalla)
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    pygame.display.flip()#Refrescar la pantalla

pygame.quit()#Salir de pygame
sys.exit()#Caer sistema en el juego para que no pete
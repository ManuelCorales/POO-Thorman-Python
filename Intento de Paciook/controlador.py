import vista
import juego
import pygame
import sys

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}

class Controlador:
    def __init__(self):
        # El controlador inicializa el juego
        # y la vista.
        self.dimensiones = (640, 480)
        self.juego = juego.Juego('Fede', self.dimensiones)
        self.vista = vista.Vista(self.dimensiones, self.juego)

        self.cargar_imagenes()
        self.main_loop()

    
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                #self.juego.mover_bm(event.tevent_name())
                if event.type==pygame.KEYDOWN: # alguien presionó una tecla
                    #print(pygame.event.event_name(event.type))
                    #print(event.key)
                    if str(event.key)=='32':
                        self.juego.plantarBomba()
                    else:
                        if str(event.key) in CONTROLES:
                            self.juego.moverThor(CONTROLES[str(event.key)])
                        else:
                            print(str(event.key))
                    self.vista.recargarFondo()

                    self.vista.recargarThor()
                pygame.display.flip()

    def cargar_imagenes(self):
        self.vista.carga_imagen_fondo('Wallpaper.jpg')
        self.vista.cargar_imagen_bomberman('bmsprite.png', (2,2))
        return None

if __name__=="__main__":
    controlador = Controlador()
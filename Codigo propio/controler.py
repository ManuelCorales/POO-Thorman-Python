import visual
import game
import pygame

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class Controler:
    def __init__(self):
        self.dimentions = (640, 480)
        self.game = game.game('Fede', self.dimentions)
        self.visual = visual.visual(self.dimentions, self.game)

        self.loadImages()
        self.mainLoop()

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                # self.game.mover_bm(event.tevent_name())
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    # print(pygame.event.event_name(event.type))
                    # print(event.key)
                    self.game.moveThor(CONTROLS[str(event.key)])

                    self.visual.reloadBackground()

                    self.visual.reloadThorman()
                pygame.display.flip()

    def loadImages(self):
        self.visual.loadBackgroundImage('/home/fran/Documents/Objetos/poo-bomberman/Codigo propio/grasstexture.jpg')
        self.visual.loadThormanImage('/home/fran/Documents/Objetos/poo-bomberman/Codigo propio/bmsprite.png', (2,2))
        return None

if __name__ == "__main__":
    controler = Controler()

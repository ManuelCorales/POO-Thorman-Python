from visual import Visual
<<<<<<< HEAD
import sys
=======
import enemyThread
>>>>>>> 087574e293610ed12d530571fada8e60761e42f4
import bombsThread
import time
import game
import pygame
import tickerThread
import bombsExplotionThread
import Collisions as colls
import threading
from pydispatch import dispatcher
import thormanStandingThread


CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0],
            '276': [-1, 0], 'Standing Still': [100, 100]}


class Controler():
    def __init__(self):
        self.activeObjects = []
        self.dimentions = (1200, 600)  # (640, 480)
        self.game = game.Game('Fran y Manu', self.dimentions)
        self.activeObjects.append(self.game.createThorman())
        self.visual = Visual(self.dimentions, self.game)
        self.loadImages()
        self.thormanMoving = True
        self.firstFlip = True
<<<<<<< HEAD
        self.bombs = None
        # --------- THREADS -----------
        self.bombsTimeThreadRun = bombsThread.bombTimeCounter(daemon=True)
        # self.bombsThreadRun = threading.Thread(target=self.bombsTimeThread.run)
        self.bombsTimeThreadRun.start()
=======
        # --------- THREADS -----------
        self.ticker = tickerThread.ticker(daemon=True)
        self.ticker.start()
        self.bombsTimeThread = bombsThread.bombTimeCounter(daemon=True)
        self.bombsThreadRun.start()
>>>>>>> 087574e293610ed12d530571fada8e60761e42f4
        self.explotionNumber = 0
        self.bombsExplotionThreadList = []
        self.thormanStandingThreadRun = thormanStandingThread.standingStill(daemon=True)
        self.thormanStandingThreadRun.start()
        self.enemiesThreadList = []
        # -----------------------------
        dispatcher.connect(receiver=self.explodeBomb, signal='Exploded', sender='bombsThread')
        dispatcher.connect(receiver = self.reloadExplotionSprite, signal = 'Change Explotion Sprite', sender = 'bombsExplotionThread' )
        dispatcher.connect(receiver = self.delExplotionSprite, signal = "Delete Explotion", sender = 'bombsExplotionThread' )
        dispatcher.connect(receiver = self.reloadThorman, signal = "Stand Still", sender = 'thormanStandingThread' )
        dispatcher.connect(receiver=self.flip, signal = 'Finished')
        dispatcher.connect(receiver=self.avanzarx, signal = 'Tick')
        self.mainLoop()

    def avanzarx(self):
        self.avanzar = True

    def mainLoop(self):
        # self.game.createEnemies()
        while True:
<<<<<<< HEAD
=======
            if self.avanzar == False:
                continue
>>>>>>> 087574e293610ed12d530571fada8e60761e42f4
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    if self.thormanMoving == False:
                        dispatcher.send(signal = "Moving", sender = 'Controler')
                        self.thormanMoving = True
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        self.game.moveThorman(CONTROLS['275'])
                    if keys[pygame.K_LEFT]:
                        self.game.moveThorman(CONTROLS['276'])
                    if keys[pygame.K_UP]:
                        self.game.moveThorman(CONTROLS['273'])
                    if keys[pygame.K_DOWN]:
                        self.game.moveThorman(CONTROLS['274'])
                    if keys[pygame.K_SPACE]:
                        if self.game.getAvailableBombs() != 0:
                            self.activeObjects.append(self.game.plantBomb())
                            self.reloadBombsThread()
                    else:
                        try:
                            self.game.setThormanDirection(str(event.key))
                            self.visual.reloadEverything()
                        except Exception:
                            pass
                else:
                    self.game.setThormanDirection('Standing Still')
                    if self.thormanMoving == True:
<<<<<<< HEAD
                       dispatcher.send(signal = "Not Moving", sender = 'Controler')
                       self.thormanMoving = False
            if self.firstFlip == True:
                pygame.display.flip()
                self.firstFlip = False
            colls.closeness(self.activeObjects)

=======
                        dispatcher.send(signal = "Not Moving", sender = 'Controler')
                        self.thormanMoving = False
            if self.firstFlip == True:
                pygame.display.flip()
                self.firstFlip = False
            avanzar = False
>>>>>>> 087574e293610ed12d530571fada8e60761e42f4
    # --------- LIGHTNINGS(EXPLOTIONS) -----------
    def reloadExplotionSprite(self, explotionNumber): 
        self.visual.reloadEverything()
        if explotionNumber == 3:
            pass
        else:
            self.game.setExplotionSprite(explotionNumber)

    def delExplotionSprite(self, explotionNumber):
        self.explotionNumber -= 1
        self.game.delExplodingBomb(explotionNumber)
        self.visual.reloadEverything()

    # --------- MJOLNIR(BOMBS) -----------

    def reloadBombsThread(self):
        # acá estamos creando una bocha de threads
        # yo haría una lista de thread
        dispatcher.send(signal='Add Bomb', sender='Controler')

    def explodeBomb(self):
        dispatcher.send(signal='Start Changing Explotion Sprites', sender='Controler')
        bombsExplotionThreadRun = bombsExplotionThread.bombAnimation(daemon=True, explotionNumber=self.explotionNumber)
        self.bombsExplotionThreadList.append(bombsExplotionThreadRun)
        bombsExplotionThreadRun.start()
        self.explotionNumber += 1
        self.game.addExplodingBombs()
        self.game.removeBombs()
        self.visual.reloadEverything()
    # --------- THORMAN(BOMBERMAN) -----------

    def reloadThorman(self):
        self.visual.reloadEverything()
    
    # --------- HULKS (ENEMIES) -----------

    def createEnemyThread(self):
        enemyThread = enemyThread.enemy(daemon=True)
        self.enemiesThreadList.append(enemyThread)
        enemyThread.start()
        self.game.addEnemy()
    # --------- OTHERS -----------
    def flip(self):
        pygame.display.flip()

    def loadImages(self):
        self.visual.loadBackgroundImage('../assets/Wallpaper.jpg')
        self.visual.loadThormanImage('../assets/Thorman/ThormanRight1.png',
                                     (2, 2))
        self.visual.loadLimit()
        return None

    def appendActiveObject(self, newFriend):
        self.activeObjects.append(newFriend)

if __name__ == "__main__":
    controler = Controler()

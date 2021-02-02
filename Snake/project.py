"""
Main file of Snake game
"""


import pygame
import random
import sys


# GLOBAL VARIABLES
FPS = 20
WINDOWWIDTH = 900
WINDOWHEIGHT = 600
CELLSIZE = 25
assert WINDOWWIDTH % CELLSIZE == 0
assert WINDOWHEIGHT % CELLSIZE == 0
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#        R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0    # index of snake's head


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.SysFont("Arial", 18)
    pygame.display.set_caption("Snake")

    showStartScreen()
    while True:
        runGame()   # main part of the code
        showGameOverScreen()


def runGame():
    # Set a random start point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wormCoords = [{"x": startx,     "y": starty},
                  {"x": startx - 1, "y": starty},
                  {"x": startx - 2, "y": starty}]
    direction = RIGHT

    # start the apple in a random place
    apple = getRandomLocation()

    while True:     # main game loop
        for event in pygame.event.get():    # main handling loop
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != UP:
                    direction = DOWN
                if event.key == pygame.K_ESCAPE:
                    terminate()

        # check if the worm has hit itself or the edge
        # crash into a boarding of screen
        if wormCoords[HEAD]["x"] == -1 or wormCoords[HEAD]["x"] == CELLWIDTH or wormCoords[HEAD]["y"] == -1 or \
                wormCoords[HEAD]["y"] == CELLHEIGHT:
            return  # game over
        # crash into oneself
        for wormBody in wormCoords[1:]:
            if wormBody["x"] == wormCoords[HEAD]["x"] and wormBody["y"] == wormCoords[HEAD]["y"]:
                return  # game over

        # check if worm has eaten an apple
        if wormCoords[HEAD]["x"] == apple["x"] and wormCoords[HEAD]["y"] == apple["y"]:
            # don't remove worm's tail segment
            apple = getRandomLocation()     # set a new apple's location
        else:
            del wormCoords[-1]  # remove last snake's segment

        # move the snake by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"] - 1}
        elif direction == DOWN:
            newHead = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"] + 1}
        elif direction == LEFT:
            newHead = {"x": wormCoords[HEAD]["x"] - 1, "y": wormCoords[HEAD]["y"]}
        elif direction == RIGHT:
            newHead = {"x": wormCoords[HEAD]["x"] + 1, "y": wormCoords[HEAD]["y"]}
        wormCoords.insert(0, newHead)

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawPressMsg():
    pressKeySurf = BASICFONT.render("Press any key to start.", True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(pygame.QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.SysFont("Arial", 100)
    titleSurf1 = titleFont.render("Snake", True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render("Snake", True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:     # begin the animation loop
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressMsg()

        if checkForKeyPress():
            pygame.event.get()      # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        degrees1 += 3
        degrees2 += 7


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {"x": random.randint(0, CELLWIDTH - 1), "y": random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.SysFont("Arial", 150)
    gameSurf = gameOverFont.render("Game", True, WHITE)
    overSurf = gameOverFont.render("Over", True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH // 2, 10)
    overRect.midtop = (WINDOWHEIGHT // 2, gameRect.height + 20)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


def drawScore(score):
    scoreSurf = BASICFONT.render("Score: %s" % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord["x"] * CELLSIZE
        y = coord["y"] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


def drawApple(coord):
    x = coord["x"] * CELLSIZE
    y = coord["y"] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):   # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == "__main__":
    main()
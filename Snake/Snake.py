"""
Snake game
"""


import pygame
import random
import sys


FPS = 20
W_WIDTH = 900
W_HEIGHT = 600
CELLSIZE = 25
CELLWIDTH = W_WIDTH / CELLSIZE
CELLHEIGHT = W_HEIGHT / CELLSIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
GRAY = (40, 40, 40)
LIGHTGRAY = (55, 55, 55)
BGCOLOR = BLACK


UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0

def main():
    global DISPLAY, FPSCLOCK, BASICFONT
    pygame.init()
    DISPLAY = pygame.display.set_mode((900, 600))
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.SysFont("Mistral", 24)
    pygame.display.set_caption("Snake")
    showStartScreen()
    while True:
        runGame()


def runGame():
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wormCoords = [{"x": startx,     "y": starty},
                  {"x": startx - 1, "y": starty},
                  {"x": startx - 2, "y": starty}]
    direction = RIGHT

    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
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

        if wormCoords[HEAD]["x"] == -1 or wormCoords[HEAD]["x"] == CELLWIDTH or wormCoords[HEAD]["y"] == -1 or\
                wormCoords[HEAD]["y"] == CELLHEIGHT:
            return  # game over

        for wormBody in wormCoords[1:]:
            if wormBody["x"] == wormCoords[HEAD]["x"] and wormBody["y"] == wormCoords[HEAD]["y"]:
                return  # game over

        if wormCoords[HEAD]["x"] == apple["x"] and wormCoords[HEAD]["y"] == apple["y"]:
            apple = getRandomLocation()
        else:
            del wormCoords[-1]

        if direction == UP:
            newHead = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"] - 1}
        elif direction == DOWN:
            newHead = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"] + 1}
        elif direction == LEFT:
            newHead = {"x": wormCoords[HEAD]["x"] - 1, "y": wormCoords[HEAD]["y"]}
        elif direction == RIGHT:
            newHead = {"x": wormCoords[HEAD]["x"] + 1, "y": wormCoords[HEAD]["y"]}
        wormCoords.insert(0, newHead)

        DISPLAY.fill(BGCOLOR)
        drawGrid()
        drawSnake(wormCoords)
        drawScore(len(wormCoords) - 3)
        drawApple(apple)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {"x": random.randint(1, CELLWIDTH - 2), "y": random.randint(1, CELLHEIGHT - 2)}


def showStartScreen():
    titleFont = pygame.font.SysFont("Mistral", 140)
    titleFont1 = pygame.font.SysFont("Mistral", 130)
    titleFont2 = pygame.font.SysFont("Mistral", 120)
    titleSurf = titleFont.render("Snake", True, WHITE, GRAY)
    titleSurf1 = titleFont1.render("Snake", True, GREEN)
    titleSurf2 = titleFont2.render("Snake", True, RED)

    degrees1 = 0
    degrees2 = 0

    while True:
        DISPLAY.fill(BGCOLOR)
        titleRect = titleSurf.get_rect()
        titleRect.center = (W_WIDTH / 2, W_HEIGHT / 2)
        DISPLAY.blit(titleSurf, titleRect)

        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (W_WIDTH / 2 + 10, W_HEIGHT / 2 + 10)
        DISPLAY.blit(rotatedSurf1, rotatedRect1)


        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (W_WIDTH / 2 + 20, W_HEIGHT / 2 + 20)
        DISPLAY.blit(rotatedSurf2, rotatedRect2)

        drawPressMsg()

        if checkForKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        degrees1 += 3
        degrees2 += 7


def checkForKeyPress():
    if len(pygame.event.get(pygame.QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showGameOverScreen():
    pass


def drawPressMsg():
    pressKeyMsg = BASICFONT.render("Press any key to start.", True, LIGHTGRAY)
    pressKeyRect = pressKeyMsg.get_rect()
    pressKeyRect.topleft = (W_WIDTH - 240, W_HEIGHT - 100)
    DISPLAY.blit(pressKeyMsg, pressKeyRect)


def drawScore(score):
    scoreSurf = BASICFONT.render("SCORE: %s" % score, True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (W_WIDTH - 120, 10)
    DISPLAY.blit(scoreSurf, scoreRect)


def drawSnake(wormCoords):
    for coord in wormCoords:
        x = coord["x"] * CELLSIZE
        y = coord["y"] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAY, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAY, GREEN, wormInnerSegmentRect)


def drawApple(coord):
    x = coord["x"] * CELLSIZE
    y = coord["y"] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAY, RED, appleRect)


def drawGrid():
    for x in range(0, W_WIDTH, CELLSIZE):
        pygame.draw.line(DISPLAY, GRAY, (x, 0), (x, W_HEIGHT))
    for y in range(0, W_HEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAY, GRAY, (0, y), (W_WIDTH, y))


main()
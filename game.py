import pygame
import random

# import classes necessary to create the game
from ball import Ball
from bar import Bar
from text import Text

# possible game states
STATUS_PLAYING = 1
STATUS_LOSE    = 2
STATUS_WIN     = 3

#
# The game contains one Ball and one Bar.  It moves them
# each frame.  If they collide the game is over, and stops
# allowing motion.
#
# The Ball and Bar are drawn every frame.  If the game is
# over, then a Text message is also drawn.
#
class Game:

    # create all of the objects necessary for the game play and display
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mBall = Ball(width/3, height/2, 10, (255, 255, 0))
        self.mBars = []
        self.mbotBars = []
        self.spawnBar()
        #self.spawnbotBar()
        self.mCount = 0
        self.mPoints = 0 
        #self.mBar = Bar(width/2, height/3, 100, 10, (255, 255, 0))
        #self.mBar.accelerate(20)
        self.mGameOver = False
        self.mGameStatus = STATUS_PLAYING
        self.mWinnerMessage = Text("You Win!", self.mWidth/2, self.mHeight/2)
        self.mLoserMessage = Text("Sorry, try again.", self.mWidth/2, self.mHeight/2)
        
        return

    # accelerate the ball vertically by a specified amount
    def bounceBall(self, amount):
        self.mBall.bounce(amount)
        return

    def spawnBar(self):
        h = random.randrange(100, 450, 25)
        color = (random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256))
        bar = Bar(550, 0, 50, h, color)
        bar.accelerate(20)
        self.mBars.append(bar)
        color2 = (random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256))
        randy = h + 100
        botbar = Bar(550, randy, 50, 500-randy, color)
        botbar.accelerate(20)
        self.mbotBars.append(botbar)
        return
        

    # move all of the objects, according to the physics of this world
    def evolve(self):
        
        if self.mGameOver:
            # game over, nothing will move
            return
        
        self.mPointsmessage = Text("Points = "+str(self.mPoints), 400, 400)

        # move the Ball and Bar
        self.mBall.evolve(self.mHeight)
        for botbar in self.mbotBars:
            botbar.evolve(self.mWidth)
        for bar in self.mBars:
            bar.evolve(self.mWidth)
        if self.mBars[self.mCount].getX() < 150:
            self.spawnBar()
            #self.spawnbotBar()
            self.mCount += 1
            self.mPoints +=1
        # check for collisions
        if self.mBall.collidesWithBarToLose(bar):
            print self.mPoints
            self.mGameOver = True
            self.mStatus = STATUS_LOSE
        elif self.mBall.collidesWithBarToLose(botbar):
            print self.mPoints
            self.mGameOver = True
            self.mStatus = STATUS_LOSE
        elif self.mBall.hitground():
            print self.mPoints
            self.mGameOver = True
            self.mStatus = STATUS_LOSE
        elif self.mBall.hitroof():
            print self.mPoints
            self.mGameOver = True
            self.mStatus = STATUS_LOSE
        return

    # redraw the whole screen
    def draw(self, surface):
        # make the background, be drawing a solid colored rectangle
        rect = pygame.Rect(0, 0, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, (169,169,169), rect, 0)

        self.mPointsmessage.draw(surface)

        # draw the Ball and Bar
        self.mBall.draw(surface)
        for bar in self.mBars:
            bar.draw(surface)
        for botbar in self.mbotBars:
            botbar.draw(surface)
        #botbar.draw(surface)
        if self.mGameOver:
            # draw end of game message
            if self.mStatus == STATUS_LOSE:
                self.mLoserMessage.draw(surface)
            elif self.mStatus == STATUS_WIN:
                self.mWinnerMessage.draw(surface)
        return

    

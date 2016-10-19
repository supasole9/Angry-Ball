import pygame
import math
import sound

# A circular object that can move vertically
# on the screen.  Gravity tries to accelerate
# it down every frame.  It can be accelerated up
# by a method call.  If it touches the top of the
# screen, it will bounce back down.  If it touches
# the bottom of the screen, it will stop until
# accelerated up again.  Extra methods at the bottom
# of the class are used to detect if the circle
# collides with a rectangle, and if so, which border
# line it touches.

class Ball:
    def __init__(self, x, y, r, color):
        self.mX = x
        self.mY = y
        self.mR = r
        self.mColor = color
        self.mDy = 0
        self.mGravity = 2
        self.mSound = sound.Sound("bounce_sound.wav")
        return
    
    def bounce(self, amount):
        self.mDy -= amount
        self.mSound.play()
        return

    def evolve(self, height):
        self.mDy += self.mGravity
        self.mY += self.mDy
        if self.mY + self.mR >= height - 1:
            self.mY = height - 1 - self.mR
            self.mDy = 0
        if self.mY - self.mR < 0:
            self.mY = self.mR
            if self.mDy < 0:
                self.mDy = - self.mDy
        return

    def draw(self, surface):
        pygame.draw.circle(surface, self.mColor, (self.mX, self.mY), self.mR, 0)
        return
    
    def hitground(self):
        if self.mY + self.mR >= 500 - 1:
            return True

    def hitroof(self):
        if self.mY - self.mR <= 0 + 1 :
            return True

    def collidesWithBarToWin(self, bar):
        return self.collidesWithBarTop(bar)
        
    def collidesWithBarToLose(self, bar):
        return self.collidesWithBarBottom(bar) or self.collidesWithBarLeftSide(bar) or self.collidesWithBarRightSide(bar)
        
    def collidesWithBarTop(self, bar):
        return self.collidesWithHorizontalLine(bar.getX(), bar.getX() + bar.getWidth(), bar.getY())
        
    def collidesWithBarBottom(self, bar):
        return self.collidesWithHorizontalLine(bar.getX(), bar.getX() + bar.getWidth(), bar.getY() + bar.getHeight())

    def collidesWithBarLeftSide(self, bar):
        return self.collidesWithVerticalLine(bar.getX(), bar.getY(), bar.getY() + bar.getHeight())
        
    def collidesWithBarRightSide(self, bar):
        return self.collidesWithVerticalLine(bar.getX() + bar.getWidth(), bar.getY(), bar.getY() + bar.getHeight())
        

    # Checks if the ball intersects with a horizontal line
    # theory: If one of the end points is inside the circle it collides
    #         If the x position of the center of the ball is between the points and
    #            the y position of the center of the ball is within radius of y it collides
    #         Otherwise, it doesn't collide.
    #              
    def collidesWithHorizontalLine(self, x1, x2, y):
        # make sure x1 <= x2
        if x1 > x2:
            t = x1
            x1 = x2
            x2 = t

        d1 = math.sqrt( (x1-self.mX)*(x1-self.mX) + (y-self.mY)*(y-self.mY) )
        d2 = math.sqrt( (x2-self.mX)*(x2-self.mX) + (y-self.mY)*(y-self.mY) )
        dy = abs(self.mY - y)
        if d1 <= self.mR or d2 <= self.mR:
            return True
        elif self.mX >= x1 and self.mX <= x2 and dy <= self.mR:
            return True
        else:
            return False


    # Checks if the ball intersects with a vertical line
    # theory: If one of the end points is inside the circle it collides
    #         If the y position of the center of the ball is between the points and
    #            the xy position of the center of the ball is within radius of x it collides
    #         Otherwise, it doesn't collide.
    #              
    def collidesWithVerticalLine(self, x, y1, y2):
        # make sure y1 <= y2
        if y1 > y2:
            t = y1
            y1 = y2
            y2 = t

        d1 = math.sqrt( (x-self.mX)*(x-self.mX) + (y1-self.mY)*(y1-self.mY) )
        d2 = math.sqrt( (x-self.mX)*(x-self.mX) + (y2-self.mY)*(y2-self.mY) )
        dx = abs(self.mX - x)
        if d1 <= self.mR or d2 <= self.mR:
            return True
        elif self.mY >= y1 and self.mY <= y2 and dx <= self.mR:
            return True
        else:
            return False

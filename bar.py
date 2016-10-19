import pygame

# A rectangular object that moves horizontally.
# If it reaches the side of the screen, it will
# bounce off and move in the other direction.

class Bar:
    def __init__(self, x, y, w, h, color):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
        self.mColor = color
        self.mDx = 0
        return

    def getX(self):
        return self.mX
        
    def getY(self):
        return self.mY
        
    def getWidth(self):
        return self.mWidth
        
    def getHeight(self):
        return self.mHeight
        
    def accelerate(self, ddx):
        if self.mDx >= 0:
            self.mDx += ddx
        else:
            self.mDx -= ddx
        return

    def evolve(self, width):
        self.mX -= self.mDx
        if self.mX + self.mWidth >= width - 1:
            self.mX = width - 1 - self.mWidth
            if self.mDx > 0:
                self.mDx = - self.mDx
##        if self.mX <= 0:
##            self.mX = 0
##            if self.mDx < 0:
##                self.mDx = - self.mDx
        return

    def draw(self, surface):
        rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, self.mColor, rect, 0)
        return
            
    
    
    


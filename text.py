import pygame

# Initialize the font system for use in PyGame
pygame.font.init()

# Create a font to be shared by all Text objects
g_font_height = 24
g_font = pygame.font.SysFont("Courier New", g_font_height)

# Possible alignments for the drawn text
ALIGNMENT_CENTER = 1
ALIGNMENT_LEFT   = 2
ALIGNMENT_RIGHT  = 3

#
# The Text class, used to draw text in a PyGame window
# Many features are missing, such as setters for the
# various data members.  mColor and mAlignment are
# hard coded in the constructor, etc.
#
class Text:

    def __init__(self, string, x, y):
        self.mX = x
        self.mY = y
        self.mString = string
        self.mColor = (255, 255, 0)
        self.mAlignment = ALIGNMENT_CENTER
        return

    def draw(self, surface):
        text_object = g_font.render(self.mString, False, self.mColor)
        text_rect = text_object.get_rect()
        
        if self.mAlignment == ALIGNMENT_CENTER:
            text_rect.center = (self.mX, self.mY)
        elif self.mAlignment == ALIGNMENT_LEFT:
            text_rect.bottomleft = (self.mX, self.mY)
        elif self.mAlignment == ALIGNMENT_RIGHT:
            text_rect.bottomright = (self.mX, self.mY)
        else:
            print "mAlignment has unexpected value:", self.mAlignment
        surface.blit(text_object, text_rect)
        return

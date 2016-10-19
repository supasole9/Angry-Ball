#
# The Bouncy Ball game requires the user to get a circle
# to touch the top of a moving rectangle.  Touching any other
# part of the rectangle will cause the user to fail. 
#

import pygame
import math
import game_mouse
from game import Game

class PygameBouncy(game_mouse.Game):

    def __init__(self, width, height, fps):

        game_mouse.Game.__init__(self, "Bouncy Ball",
                                 width,
                                 height,
                                 fps)
        # create the game
        self.mGame = Game(width, height)
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        # Accelerate the ball upwards when the UP key is pressed
        if pygame.K_UP in newkeys:
            self.mGame.bounceBall(10)
        
        if 1 in newbuttons:
            print "button clicked"

        # Evolve the motion of all objects once every frame
        self.mGame.evolve()
        return
    
    def paint(self, surface):
        # Draw all objects once every frame
        self.mGame.draw(surface)
        return

def main():
    screen_width = 600
    screen_height = 500
    frames_per_second = 10
    game = PygameBouncy(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

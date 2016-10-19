import pygame
import os

pygame.mixer.init()

class Sound:

    def __init__(self, sound_file_name):
        if os.path.exists(sound_file_name):
            self.mSound = pygame.mixer.Sound(sound_file_name)
        else:
            self.mSound = None
        return
    
    def play(self):
        if self.mSound:
            self.mSound.play()
        return

    def setVolume(self, percent):
        if percent >= 0 and percent <= 1 and self.mSound:
            self.mSound.set_volume(percent)
            return True
        return False

        

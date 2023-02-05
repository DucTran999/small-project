import os
from time import sleep

class Utilization:
    """A class provides methods to make the game run smoothly"""
    
    @classmethod
    def clear_console_screen(cls):
        """ Clear the console screen to avoid distracting players."""
        os.system('cls')
    
    @classmethod
    def delay(cls, time, message=''):
        """Small delay when loading or changing screens for player comfort."""
        print(message)
        sleep(time)
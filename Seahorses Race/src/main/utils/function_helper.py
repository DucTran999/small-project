import os
import time

class FunctionHelper:
    """This class in charge of processing small task."""
    @staticmethod
    def clear_screen():
        os.system('cls')
    
    @staticmethod
    def delay_with_announcement(announcement: str, time_delay: int):
        print(announcement, "...")
        time.sleep(time_delay)
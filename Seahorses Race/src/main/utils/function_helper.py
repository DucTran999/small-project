import os
import time

class FunctionHelper:
    """This class in charge of processing small task."""
    @classmethod
    def clear_screen(cls):
        os.system('cls')
    
    @classmethod
    def delay_with_announcement(cls, announcement: str, time_delay: int):
        print(announcement, "...")
        time.sleep(time_delay)
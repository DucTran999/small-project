"""Utilities module:
provides functions that perform small tasks and are called multiple times.
"""

import os
import time


def clear_console() -> None:
    os.system('cls')


def delay(seccond: int, message: str = ''):
    # Small amount of time delay before executing some events.
    print(message)
    time.sleep(seccond)

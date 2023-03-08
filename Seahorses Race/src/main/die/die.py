from dataclasses import dataclass


@dataclass(frozen=True)
class Die:
    """Class represents a die."""
    faces: tuple[int] = (1, 2, 3, 4, 5, 6)
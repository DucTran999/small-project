class Seahorse:
    """This class represent a seahorse in game.""" 
    def __init__(self, seahorse_id: int, pos: int=0, state: str='Warm up') -> None:
        """Seahorse constructor
        
        Param:
        - seahorse_id: Identify seahorse.
        - pos: seahorse current position
        - state: default state is 'Warm up'. This will be affected by the box event.
        
        state Glossary: 
            'Warm up': seahorse not ready to race.
            'Ready': seahorse at the start.
            'Running': seahorse is running.
            'Finish': seahorse finished the race.
            'Cannot race': seahorse have to quit the race.
        """
        self.__seahorse_id = seahorse_id
        self.__position = pos
        self.__state = state
    
    def __repr__(self) -> str:
        return (
            f"id: {self.seahorse_id}" 
            f" - pos: {self.position}"
            f" - state: {self.state}"
        )
    
    @property
    def seahorse_id(self) -> int:
        return self.__seahorse_id
    
    @property
    def position(self) -> int:
        return self.__position
    
    @position.setter
    def position(self, new_pos: int) -> None:
        self.__position = new_pos
    
    @property
    def state(self) -> int:
        return self.__state

    @state.setter
    def state(self, new_state) -> int:
        self.__state = new_state
    
    def move(self, step: int) -> None:
        self.state = 'Running'
        current_pos = self.position
        new_pos = current_pos + step
        if new_pos > 12:
            self.state = 'Finish'
            new_pos = 13
        self.position = new_pos
    
    def move_to_start(self) -> None:
        self.position = 0
        self.state = 'Ready' 
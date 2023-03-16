import abc

class IFilterSeahorseService(abc.ABC):
    
    @abc.abstractmethod
    def get_seahorses_available_id_list(self) -> list[int]:
        pass
    
    @abc.abstractmethod
    def get_seahorse_warm_up_id_list(self) -> list[int]:
        pass

    @abc.abstractmethod
    def get_seahorse_can_move_id_list(self) -> list[int]:
        pass
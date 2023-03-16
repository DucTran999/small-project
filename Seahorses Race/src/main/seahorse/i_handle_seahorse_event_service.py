import abc

class IHandleSeahorseEventService(abc.ABC):
    
    @abc.abstractmethod
    def handle_seahorse_get_box_event(self):
        pass
    
    @abc.abstractmethod
    def handle_seahorse_get_face_6_event(self):
        pass

    @abc.abstractmethod
    def handle_seahorse_get_not_face_6_event(self):
        pass
import abc

class IHandleSeahorseEventService(abc.ABC):
    
    @abc.abstractmethod
    def update_seahorse_info_get_box_event(self, seahorse, event_name,
                                           event_value):
        pass
    
    @abc.abstractmethod
    def update_seahorse_info_get_face_6_event(self):
        pass

    @abc.abstractmethod
    def update_seahorse_info_get_not_face_6_event(self):
        pass
import abc


class TopicDAO(metaclass=abc.ABCMeta):
    
    @abc.abstractclassmethod
    def get_all_topic_from_file(self):
        pass
    
    @abc.abstractclassmethod
    def get_topic_by_name_from_file(self):
        pass
    
    @abc.abstractclassmethod
    def add_topic_to_file(self):
        pass
    
    @abc.abstractclassmethod
    def add_quiz_to_file(self):
        pass
    
    @abc.abstractclassmethod
    def delete_topic_from_file(self):
        pass

    @abc.abstractclassmethod
    def update_topic_name_to_file(self):
        pass
    
    def delete_quiz_from_file(self):
        pass
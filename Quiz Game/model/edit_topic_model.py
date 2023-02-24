from dao_impl.topic_dao_impl import TopicDAOImplement


class EditTopicModel:
    """Help Edit Controller manipulate data"""
    def __init__(self) -> None:
        self.topic_dao_impl = TopicDAOImplement()
    
    def get_topic(self, topic_name: str):
        return self.topic_dao_impl.get_topic_by_name_from_file(topic_name)
    
    def rename_topic(self, topics: list[str], old_name: str, new_name: str) -> None:
        self.topic_dao_impl.update_topic_name_to_file(topics, old_name, new_name)
    
    def delete_quiz_by_id(self, topic, quiz_id: int):
        self.topic_dao_impl.delete_quiz_from_file(topic, quiz_id)
    
    def add_new_quiz(self, topic_name, quizzes):
        self.topic_dao_impl.add_quiz_to_file(topic_name, quizzes)
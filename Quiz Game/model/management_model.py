from dao.file_helper import FileHelper
from dao_impl.topic_dao_impl import TopicDAOImplement

from model.topic import Topic


class ManagementModel:
    """Processing the objects and data used in the management features."""
    def __init__(self) -> None:
        self.topic_dao = TopicDAOImplement()

    def get_topic_list(self) -> list | None:
        return self.topic_dao.get_all_topic_from_file()
    
    def find_topic_by_name(self, user_input: str, topics: list) -> int:
        """Find the topic's id with the exact name."""
        return topics.index(user_input) if user_input in topics else -1
    
    def add_new_topic(self, topic: Topic):
        self.topic_dao.add_topic_to_file(topic.topic_name)
        self.topic_dao.add_quiz_to_file(topic.topic_name, topic.quizzes)
    
    def add_quiz_list_to_file(self, topic_name: str, quiz_list: list[dict]):
        FileHelper.write_json_file(topic_name, quiz_list)
    
    def delete_topic(self, topic_id: int, topics: list[str]) -> None:
        topic_name = topics[topic_id]
        topics.remove(topic_name)
        self.topic_dao.remove_topic_from_file(topic_name, topics)
    
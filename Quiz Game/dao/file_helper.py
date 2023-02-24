import json
import os


class FileHelper:
    """This class provides functions for interacting with the files."""
       
    @staticmethod
    def read_text_file(file_name: str) -> list or None:
        filepath = f"Quiz Game/data_source/{file_name}.txt"
        try:
            with open(filepath, mode='r', encoding='utf-8') as file_obj:
                content = file_obj.readlines()
        except FileNotFoundError:
            error_message = (
                f"<!> Can't load resource from {file_name}.txt file!\n"
                "<i> Help: Change current working directory to small_project "
                "or check the filename."
                )
            print(error_message)
        else:
            return content
    
    @classmethod
    def append_text_file(cls, file_name: str, topic_name: str) -> None:
        file_path = f"Quiz Game/data_source/{file_name}.txt"
        try:
            with open(file_path, mode='a', encoding='utf-8') as file_obj:
                file_obj.write("\n")
                file_obj.write(topic_name)
        except FileNotFoundError:
            error_message = (
                f"<!> Can't write to the {file_name}!\n"
                "<i> Help: Change current working directory to small_project"
                )
            print(error_message)
    
    @classmethod
    def write_text_file(cls, file_name: str, topics: list) -> None:
        file_path = f"Quiz Game/data_source/{file_name}.txt"
        last_topic_id = len(topics) - 1
        try:
            with open(file_path, mode='w', encoding='utf-8') as file_obj:
                for topic_id, topic in enumerate(topics):
                    if topic_id != last_topic_id:
                        topic = topic + "\n"
                    file_obj.write(topic)
            print("<i> Topic List Updated!")
        except FileExistsError:
            error_message = (f"<!> Can't overwrite to the {file_name}!")
            print(error_message)
    
    @classmethod
    def delete_text_file(cls, file_name: str) -> None:
        file_path = f"Quiz Game/data_source/{file_name}.txt"
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print(f"The {file_name} file is already deleted or does not exist.")
        
    @classmethod
    def read_json_file(cls, file_name) -> list or None:
        file_path = f"Quiz Game/data_source/{file_name}_quiz.json"
        try:
            with open(file_path) as file_obj:
                content = json.load(file_obj)
        except FileNotFoundError:
            error_message = (
                f"<!> Can't load the {file_name}!\n"
                "<i> Help: Change current working directory to small_project"
                )
            print(error_message)
        else:
            return content
    
    @classmethod
    def write_json_file(cls, file_name: str, quiz_list: list[dict]):
        file_path = f"Quiz Game/data_source/{file_name}_quiz.json"
        try:
            with open(file_path, mode='w', encoding='UTF-8') as file_obj:
                content = json.dumps(quiz_list, indent=4)
                file_obj.write(content)
        except FileExistsError:
            error_message = (f"<!> {file_name} EXISTED!\n")
            print(error_message)
     
    @classmethod
    def delete_json_file(cls, file_name: str) -> None:
        file_path = f"Quiz Game/data_source/{file_name}_quiz.json"
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print(f"The {file_name} file is already deleted or does not exist.")
    
    @classmethod
    def rename_json_file(cls, old_name: str, new_name:str):
        file_path = "Quiz Game/data_source/{}_quiz.json"
        old_path = file_path.format(old_name)
        new_path = file_path.format(new_name)
        os.rename(old_path, new_path)
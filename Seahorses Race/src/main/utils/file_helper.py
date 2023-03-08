import json


class FileHelper:
    """Providing methods to manipulate file
    
    Available method:
    - read_text_file
    - read_json_file
    """
    @classmethod
    def read_text_file(cls, filename: str) -> list[str] or None:
        filepath = f"Seahorses Race/src/db/{filename}.txt"
        try:
            with open(filepath, mode='r', encoding='utf-8') as file_obj:
                content = file_obj.read()
        except FileNotFoundError:
            print(f"<!> The '{filename}' file not found!\n"
                  "<i> Help: Change current working dir to small-project")
        else:
            return content
    
    @classmethod
    def read_json_file(cls, filename: str) -> list[dict] or None:
        filepath = f"Seahorses Race/src/db/{filename}.json"
        try:
            with open(filepath, mode='r', encoding='utf-8') as file_obj:
                content = json.load(file_obj)
        except FileNotFoundError:
            print(f"<!> The '{filename}' file not found!\n"
                  "<i> Help: Change current working dir to small-project")
        else:
            return content
        
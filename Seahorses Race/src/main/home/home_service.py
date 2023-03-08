from utils.file_helper import FileHelper


class HomeService:
    """Responsible for data manipulation abiding by the HomeController directive."""
    def get_guideline(self):
        return FileHelper.read_text_file('guideline')

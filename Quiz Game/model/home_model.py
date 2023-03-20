from dao.file_helper import FileHelper
class HomeModel:
    """Processing data use for Home.
    
    This class is responsible for handling data for the Home page according to 
    the Home Controller command.
    
    Available method:
    - get_guideline:  
    """
    def get_guideline(self) -> list[str]:
        """Get guideline content from file and process it.

        Variable:
        - guideline raw: hold data after reading from file.
        
        Return:
            If guideline_raw is None return it directly. 
            Otherwise, process the data before returning.
        """
        filename = "guideline" 
        guideline_raw = FileHelper.read_text_file(filename)
        if guideline_raw != None:
            # Remove whitespace and newline characters for each line.
            return [line.strip() for line in guideline_raw]
        return guideline_raw 

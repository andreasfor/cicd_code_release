import os
 
class SupportClass:
    
    def get_workspace_path() -> str:
        """
        This class should reside inside src folder and when called return the directory path of src, regardless of which system it is called at. 
        The string returned will be used as root for PYTHONPATH when calling packages.  

        :return: The string returned will be used as root for PYTHONPATH when calling packages
        :rtype: str
        """
        workspace_path = os.path.abspath(os.path.dirname(__file__))

        return workspace_path
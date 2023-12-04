import os
 
class SupportClass:
    
    def get_workspace_path() -> str:
        """
        This class should reside outside src folder and when called return the directory path, regardless of which system it is called at. 
        The string returned will be used as root for PYTHONPATH when calling packages.  

        :return: The string returned will be used as root for PYTHONPATH when calling packages
        :rtype: str
        """
        workspace_path = os.path.abspath(os.path.dirname(__file__))

        workspace_path = workspace_path.replace('\\', '/')

        return workspace_path

print(SupportClass.get_workspace_path())
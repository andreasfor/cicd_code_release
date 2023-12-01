

"""
TODO
1, Set PYTHONPATH as good as this time slots allows
2, i dont really get the __init__ file. It works anyway? And it did not work to use a relative path with it either.  
3, Discuss the best folder structure for a small to medium project 
"""

#-------------------
# Option 1
# ------------------
# import sys
# sys.path.insert(0, r'C:\Users\anforsbe\OneDrive - Capgemini\Documents\Visual Studio Code\test_cicd\cicd_code_resease/src')

#-------------------
# Option 2
# ------------------

# import os
# import sys
# from dotenv import load_dotenv

# load_dotenv()

# sys.path.insert(0, os.getenv("PYTHONPATH"))

#-------------------
# Option 3
# ------------------

# import sys
# from support import SupportClass

# sys.path.insert(0, SupportClass.get_workspace_path())

#-------------------
# CODE
# ------------------


from src.my_first_class_dir.first_class import Addition

# rom my_first_class_dir.first_class import Addition

class SecondClass:
    def powered_fn(number_one, number_two, exponent=2):

        base = Addition.add_fn(number_one, number_two)

        result = base ** exponent
        return result
    

if __name__ == "__main__":

    powered_number = SecondClass.powered_fn(2,2)
    print(powered_number)
#import sys
# sys.path.append("c:/Users/anforsbe/OneDrive - Capgemini/Documents/Visual Studio Code/test_cicd")

import My_First_Class as MFS

class SecondClass:
    def powered_fn(number_one, number_two, exponent=2):

        base = MFS.Addition.add_fn(number_one, number_two)

        result = base ** exponent
        return result
    

if __name__ == "__main__":
#    import sys
#    print(sys.path)

    powered_number = SecondClass.powered_fn(2,2)
    print(powered_number)
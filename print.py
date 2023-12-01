import sys
import os
import os.path



src_path_os = os.getenv("PYTHONPATH")
src_path_str = "C:/Users/anforsbe/OneDrive - Capgemini\Documents/Visual Studio Code/test_cicd/cicd_code_resease/src"

print(src_path_os)
print(src_path_str)

for idx, (os_path_char, string_path_char) in enumerate(zip(src_path_os, src_path_str)):

    if os_path_char == string_path_char:
        print(f"Equal at idx: {idx}. The char is: {os_path_char}, {string_path_char}")
    else:
        print(f"NOT EQUAL at idx: {idx}. The char is: {os_path_char}, {string_path_char}")

if os.path.exists(src_path_os):
    print("dir exists")
else:
    print("Does not exists")

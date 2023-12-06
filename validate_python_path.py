""""
This script checks
"""

import sys
import os
import os.path

src_path_os = os.getenv("PYTHONPATH")
src_path_str = "c:/Users/anforsbe/Visual Studio Code/CICD/cicd_code_release"

print(f"src_path_os: {src_path_os}")
print(f"src_path_str: {src_path_str}")

for idx, (os_path_char, string_path_char) in enumerate(zip(src_path_os, src_path_str)):

    if os_path_char == string_path_char:
        print(f"Equal at idx: {idx}. The char is: {os_path_char}, {string_path_char}")
    else:
        print(f"NOT equel at idx: {idx}. The char is: {os_path_char}, {string_path_char}")

if os.path.exists(src_path_os):
    print("Dir exists")
else:
    print("Dir does NOT exists")

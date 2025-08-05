import os

def check_path_type(path):
    
    if os.path.exists(path):
        if os.path.isfile(path):
            return "File"
        elif os.path.isdir(path):
            return "Directory"
    return "Neither"



print(f"'.' is a: {check_path_type('.')}")


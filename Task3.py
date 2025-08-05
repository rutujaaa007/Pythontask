
# creates a new folder called test_folder in the current working directory if it doesn't already exist.

import os
folder_name = "test_folder"

if not os.path.exists(folder_name):

    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")

else:
    
    print(f"The Folder '{folder_name}' already exists")




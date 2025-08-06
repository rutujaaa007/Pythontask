import os

def input_folder():
    
    folder_name = "data_input"

    if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        
    else:
        print(f"Folder '{folder_name}' already exists.")


all_files_and_directories = os.listdir('.')
item=[ ]
print("File found ")
for item in all_files_and_directories:
    if os.path.isfile(item) and item.endswith('.txt'):
        print(item)





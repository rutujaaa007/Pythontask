import os

all_files_and_directories = os.listdir('.')
item=[ ]
print("File found ")
for item in all_files_and_directories:
    if os.path.isfile(item) and item.endswith('.txt'):
        print(item)
    
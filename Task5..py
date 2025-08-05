import os
import shutil

with open("hello.txt", "w") as f:
    f.write("This is a quarterly report.")
with open("meeting_notes.txt", "w") as f:
    f.write("Some notes from the meeting.")
with open("important_data.csv", "w") as f:
    f.write("1,2,3")

reports_folder_name = "reports"

if not os.path.exists(reports_folder_name):
    os.mkdir(reports_folder_name)
    print(f"The folder '{reports_folder_name}' was created.")
else:
    print(f"The folder '{reports_folder_name}' already exists.")


all_items = os.listdir('.')

txt_files_to_move = []


for item in all_items:
    
    if os.path.isfile(item) and item.endswith('.txt'):
        txt_files_to_move.append(item)


if len(txt_files_to_move) == 0:
    print("No .txt files were found in the current directory. Nothing to move.")
else:
    print(f"Found {len(txt_files_to_move)} file(s) to move.")
    
    for filename in txt_files_to_move:
        
        source_path = os.path.join('.', filename)
        destination_path = os.path.join(reports_folder_name, filename)
        shutil.move(source_path, destination_path)
        
        print (f"'{filename}', Moved in {reports_folder_name} Directory")




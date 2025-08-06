import os

def process_files_simply():
    
    input_folder = "data_input"
    output_folder = "data_output"
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    
    if not os.listdir(input_folder):
        print(f"'{input_folder}' is empty")
        with open(os.path.join(input_folder, "notes.txt"), 'w') as f:
            f.write("# This is a quick note.\n")
            
        with open(os.path.join(input_folder, "log.txt"), 'w') as f:
            f.write("Log entry 1: temp issue detected.\n")
            f.write("# Ignore this log comment.\n")
            f.write("Log entry 2: system is stable.\n")
        print("Sample files 'notes.txt' and 'log.txt' created in 'data_input'.")


    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.join(output_folder, filename)

            lines_count = 0
            words_count = 0
            modified_content_lines = []

            print(f"Processing '{filename}':")

            try:
                with open(input_filepath, 'r', encoding='utf-8') as infile:
                    for line in infile:
                    
                        if line.strip().startswith('#'):
                            continue 

                        lines_count += 1
                        words_count += len(line.strip().split()) 

                    
                        modified_line = line.replace("temp", "permanent")
                        modified_content_lines.append(modified_line)

            
                with open(output_filepath, 'w', encoding='utf-8') as outfile:
                    outfile.writelines(modified_content_lines)

                print(f"  - Lines processed (excluding comments): {lines_count}")
                print(f"  - Words processed (excluding comments): {words_count}")
                print(f"  - Modified version saved to '{output_filepath}'")

            except Exception as e:
                print(f"  - Error processing '{filename}': {e}")


if __name__ == "__main__":
    process_files_simply()

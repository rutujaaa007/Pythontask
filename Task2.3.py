import os

os.makedirs('data_output', exist_ok=True)

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename, 'r') as f_in, open(os.path.join('data_output', filename), 'w') as f_out:
            lines = 0
            words = 0
            for line in f_in:
                if not line.startswith('#'):
                    lines += 1
                    modified_line = line.replace('temp', 'permanent')
                    words += len(modified_line.split())
                    f_out.write(modified_line)
            print(f"File: {filename}, Lines: {lines}, Words: {words}")

from pathlib import Path

files_dir = Path('files_backup')

merged = ''
for index, filepath in enumerate(files_dir.iterdir()): ### Enumerate gives each item an index so you know which file is being processed
    with open(filepath, 'r') as file:
        content = file.readlines()  ### Gives you a list of content on a line per line basis, you need to turn it into a string
        new_content = content[1:]
    if index == 0:   ### If it's the first file being read, copy the header as well
        content = ''.join(content)
        merged = merged + content + '\n'
    else: ### Otherwise use the "new_content" value that removes the first line from the csv file (header)
        new_content = ''.join(new_content)
        merged = merged + new_content + '\n'
        
with open('merged.csv', 'w') as file:
     file.write(merged)
     
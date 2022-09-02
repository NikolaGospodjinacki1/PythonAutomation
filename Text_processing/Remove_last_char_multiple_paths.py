from pathlib import Path
import os

root_path = Path('.')
backup_path = Path('./files_backup')

### Copy all .csv files to a backup directory
if not backup_path.exists:
    os.system('mkdir files_backup')
    
os.system('cp -a ./*.csv ./files_backup/')

for filepath in root_path.glob('*.csv'):
    with open(filepath, 'r') as file:
        content = file.read()
        new_content = content[:-1]
        
    with open(filepath, 'w') as file:   
        file.write(new_content)
        
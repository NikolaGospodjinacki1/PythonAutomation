from genericpath import isfile
from pathlib import Path
from datetime import datetime

root_dir = Path('files_date_created')
paths = root_dir.glob('**/*')

for path in paths:
    if path.is_file():
        #stats = path.stat()
        #second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(path.stat().st_ctime)
        date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
        new_filename = f"{date_created_str}-{path.name}"
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filepath)
    
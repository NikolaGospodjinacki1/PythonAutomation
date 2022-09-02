import re
from pathlib import Path

root_dir = Path('files')
file_names = root_dir.iterdir()
filenames_str = [filename.name for filename in file_names]

pattern = re.compile("nov[a-z]*-(?:[1-9]|1[0-9]|20).txt", re.IGNORECASE)
matches = [filename for filename in filenames_str if pattern.findall(filename)]
print(matches)
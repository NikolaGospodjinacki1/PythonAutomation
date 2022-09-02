### gives you absolute paths for matched files
from pathlib import Path

root_dir = Path('files')
search_term = "new"


for path in root_dir.glob("*"):
  if (search_term in path.stem) and (path.is_file()):
    print(path.absolute())
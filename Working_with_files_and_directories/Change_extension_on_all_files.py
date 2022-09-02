from pathlib import Path

root_path = Path('files')
### rglob = **/* so useful when you have subdirectories ##
for path in root_path.rglob('*.testext'):
    if path.is_file():
        print(path)
        new_filepath = path.with_suffix('.csv')
        print(new_filepath)
        path.rename(new_filepath)
from pathlib import Path
import zipfile

root_dir = Path('files')
destination_path = Path('files')

for path in root_dir.glob("*.zip"): ### use glob when you DON'T want to check the SUBdirectories
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_path / Path(path.stem)  ### Create separate directory based on zip archive name
        zf.extractall(path=final_path)       ### directory where paths should be extracted
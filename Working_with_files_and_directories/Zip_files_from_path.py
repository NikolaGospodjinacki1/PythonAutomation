from pathlib import Path
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf: ### 'r'= extract 
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink() ###deletes the original file that is being zipped 
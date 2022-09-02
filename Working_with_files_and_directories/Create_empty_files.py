from pathlib import Path

root_dir = Path('files')

### upper bound is exclusive ###
for i in range(10, 16):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename) ### files/10.txt
    filepath.touch()
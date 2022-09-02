from pathlib import Path

root_path = Path('files_sub_sub_folder')
all_files = root_path.glob('**/*')

for file in all_files:
    if file.is_file():
        print(file)
        new_filename = f"{file.parts[-3]}-{file.parts[-2]}-{file.name}"
        print(new_filename)
        new_filepath = file.with_name(new_filename)
        print(new_filepath)
        file.rename(new_filepath)
        
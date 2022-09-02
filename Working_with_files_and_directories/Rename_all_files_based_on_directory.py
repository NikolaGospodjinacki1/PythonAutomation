from pathlib import Path

root_dir = Path('files_based_on_directory')
file_paths = root_dir.glob("**/*")

for file_path in file_paths:
    if file_path.is_file():
        parent_directory = file_path.parts[-2]
        new_filename_string =  f"{parent_directory}-{file_path.name}" 
        print(new_filename_string)
        new_filepath = file_path.with_name(new_filename_string)       
        print(new_filepath)
        file_path.rename(new_filepath)
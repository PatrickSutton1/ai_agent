import os

def write_file(working_directory, file_path, content):
    abs_wd = os.path.abspath(working_directory)
    target_file = os.path.join(abs_wd, file_path)
    if file_path:
        # check directory is in the allowed path
        if target_file.startswith(abs_wd):
            if os.path.exists(target_file):
                with open(target_file, 'w') as f:
                    f.write(content)
                print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
            else:
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                with open(target_file, 'w') as f:
                    f.write(content)
                print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
        else:
            print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

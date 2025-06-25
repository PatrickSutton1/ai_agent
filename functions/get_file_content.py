import os

def get_file_content(working_directory, file_path):
    abs_wd = os.path.abspath(working_directory)
    target_file = os.path.join(abs_wd, file_path)
    if file_path:
        # check if target directory is a directory
        if os.path.isfile(target_file):
            # check directory is in the allowed path
            if target_file.startswith(abs_wd):
                # Important to max characters - token cost would be too high otherwise
                MAX_CHARS = 10000
                with open(target_file, 'r') as f:
                    file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == MAX_CHARS:
                    print(file_content_string)
                    print(f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]')
                else:
                    print(file_content_string)
            else:
                print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        else: print(f'Error: File not found or not a regular file: "{file_path}"')


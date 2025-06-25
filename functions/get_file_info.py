import os

def get_file_info(working_directory, directory=None):
    abs_wd = os.path.abspath(working_directory)
    target_dir = os.path.join(abs_wd, directory)
    abs_targ_dir = os.path.abspath(target_dir)
    if directory:
        # check if target directory is a directory
        if os.path.isdir(target_dir):
            # check directory is in the allowed path
            if abs_targ_dir.startswith(abs_wd):
                for file in os.listdir(abs_targ_dir):
                    full_path = os.path.join(abs_targ_dir, file)
                    print(f'{file}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}')
            else:
                    print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        else: print(f'Error: "{directory}" is not a directory')

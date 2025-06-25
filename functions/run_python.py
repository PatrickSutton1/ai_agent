import os
import subprocess

def run_python_script(working_directory, file_path):
    """
    Runs a Python script located at file_path in the specified working_directory.
    
    Args:
        working_directory (str): The directory in which to run the script.
        file_path (str): The path to the Python script to be executed (Must be within the working_directory).
    
    Returns:
        str: The output of the script execution.
    """
    abs_wd = os.path.abspath(working_directory) 
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    print(target_file)
    if target_file.startswith(abs_wd):
        if os.path.isfile(target_file):
            if target_file.endswith('.py'):
                subprocess.run(['python', target_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30, cwd=abs_wd)
                if subprocess.STDOUT is not None:
                    print(f'STDOUT: {subprocess.PIPE}')
                    print(f'STDERR: {subprocess.STDOUT}')
                elif subprocess.CompletedProcess.returncode != 0:
                    print(f'Process exitex with code {subprocess.CompletedProcess.returncode}')
                else:
                    print("No output produced.")
            else:
                print(f'Error: "{file_path}" is not a Python file.')
        else:
            print(f'Error: File "{file_path}" not found.')
    else:
        print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

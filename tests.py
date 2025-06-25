# from functions.get_file_info import get_file_info

# get_files_info("calculator", ".")
# get_files_info("calculator", "pkg")
# get_files_info("calculator", "/bin")
# get_files_info("calculator", "../")

# from functions.get_file_content import get_file_content

# get_file_content("calculator", "lorem.txt") # Test truncation works

# get_file_content("calculator", "main.py")
# get_file_content("calculator", "pkg/calculator.py")
# get_file_content("calculator", "/bin/cat")

from functions.write_file import write_file

write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

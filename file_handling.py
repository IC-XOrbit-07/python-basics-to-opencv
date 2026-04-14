# FILE HANDLING

# CONSTANTS

FILE_PATH  = "./File Handling/write_file.txt"                                       # File Location to read, write and append
FILE_CONTENT     = "This is file content"                                           # File content to add
DEFAULT_ENCODING = "UTF-8"                                                          # Default Encoding

# FILE OPENING MDOE (write binary (wb), append binary (ab), read binary(rb)), read & write both(r+)
READ_BINARY_MODE       = "rb"
WRITE_BINARY_MODE      = "wb"                                                       # Override file content
READ_WRITE_BINARY_MODE = "r+"                                                       # File must exist in this mode  
APPEND_BINARY_MODE     = "ab"

print("-----------------------------------------------Writing File (Start)--------------------------------------------------")

write_file = open(FILE_PATH, WRITE_BINARY_MODE)                                    # open(): Takes file path & opening mode

print("Mode in which file opened    : ", write_file.mode)                          # To access the mode in which file is opened
print("Path of file opened          : ", write_file.name)                          # To get the name of current file

write_file.write(bytes(FILE_CONTENT, DEFAULT_ENCODING))                            # To write data in file

write_file.close()                                                                 # To free file, so other process can use it

print("-------------------------------------------------Writing File (END)--------------------------------------------------")

print()             

print("-----------------------------------------------Reading File (Start)--------------------------------------------------")

read_file = open(FILE_PATH, READ_BINARY_MODE)

print("Mode in which file opened    : ", read_file.mode)                           # To access the mode in which file is opened
print("Path of file opened          : ", read_file.name)                           # To get the name of current file
file_content = read_file.read()                                                    # Variable to store file content
print("File Content                 : ", file_content.decode())                    # (if using r+ mode then no need to write .decode())

read_file.close()                                                                  # To free file, so other process can use it

print("-----------------------------------------------Reading File (End)----------------------------------------------------")

print()

print("-----------------------------------------------Using with (Start)----------------------------------------------------")

with open(FILE_PATH, READ_BINARY_MODE) as file:
    file_content = file.read()
    print("File Content with `with`     : ", file_content.decode())

# File automatically closed here

print("------------------------------------------------Using with (End)-----------------------------------------------------")



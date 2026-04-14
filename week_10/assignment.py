# Reset before Script A
with open("data.txt", "w+") as f:
    f.write("ABCDEFGHIJ")
    f.seek(0)
    print("Original:", f.read())

# Script A
with open("data.txt", "r+") as f:
    f.read(3)
    f.write("XYZ")
    f.seek(0)
    print("After Script A:", f.read())

# Reset before Script B
with open("data.txt", "w+") as f:
    f.write("ABCDEFGHIJ")
    f.seek(0)
    print("Reset to:", f.read())

# Script B
with open("data.txt", "w+") as f:
    f.read(3)
    f.write("XYZ")
    f.seek(0)
    print("After Script B:", f.read())

# Explanation:
#
# The initial content of `data.txt` is "ABCDEFGHIJ".
#
# In Script A, the file is opened in `r+` mode, which allows both reading and writing 
# without deleting existing content. The call to `f.read(3)` reads the first three 
# characters and moves the file pointer to position 3, so when `f.write("XYZ")` is 
# executed, it overwrites the next three characters in the file, resulting in 
# "ABCXYZGHIJ".
# Or at least this was the intention.
# Due to the current version of Python, `f.read(3)` reads to the third cursor position, 
# from where a read would continue, but the O.S. level file pointer (because the file 
# is opened in text mode and not binary) is at the end of the file and writing resumes 
# from there. Thus, resulting in "ABCDEFGHIJXYZ".
# 
# I then reset the content of `data.txt` is "ABCDEFGHIJ" before running Script B.
#
# In Script B, the file is opened in `w+` mode, which truncates the file immediately, 
# clearing all existing content. As a result, `f.read(3)` reads nothing because the 
# file is empty, and `f.write("XYZ")` writes to the beginning of the file, resulting in 
# "XYZ". 
# 
# This demonstrates that `r+` modifies existing content at the current file pointer 
# position, while `w+` clears the file before writing.

from pathlib import Path

# we could wrote also import pathlib; pathlib is a library that allows us to find were is a file among others properties

# -- Constant with the new of the file to open --> when is in capital letter is a constant
FILENAME = "RNU6_269P.txt"
# FILENAME= "../Hello/Hello.py" --> to read folders that are not in the same directory

# -- Open and read the file
file_contents = Path(FILENAME).read_text()  # .read_text() --> is the same as when we wrote "with open () as f:"

# -- Print the contents on the console
print(file_contents)

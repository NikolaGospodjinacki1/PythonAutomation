with open('file3.csv' 'r') as file:
    content = file.read()

#print(content[:-1])  give me a string with the entire contents of a file excluding the last character
modified_content=content[:-1]

with open('file3.csv', 'w') as file: ### use the same name (file3) to overwrite the pre-existing content/file !!! MAKE A BACK-UP before doing so 
    file.write(modified_content)
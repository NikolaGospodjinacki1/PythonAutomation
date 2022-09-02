content = """First text

Whatever

This is fine too

Second text"""

with open('file1.txt', 'w') as file:  # overwrites existing file if it exists   
    file.write(content)
    #file.write('Second text')


#file.close() #close the file for operations, can't write more text in file after that, NOT NEEDED IF USED WITH with
with open('file1.txt', 'r') as file: ### Needs to be existing file or you get an error   DEFAULT MODE IS 'r' so you don't need to include this argument
    content =file.read()

print(content)
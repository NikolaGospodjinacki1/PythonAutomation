with open ('merged.csv','r') as file:
    content = file.readlines()  ### Read file as a bunch of lines
    
content[0] = 'ID,AMOUNT,COST\n'  ### New text that will replace the first line

with open ('merged.csv', 'w') as file:
    file.writelines(content)  ### Write the replacement text instead of the line with the index of 0 (first line)
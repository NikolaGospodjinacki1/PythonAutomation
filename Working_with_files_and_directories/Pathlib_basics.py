from pathlib import Path

p1 = Path('files/ghi.txt')

if not p1.exists():
    with open(p1, 'w') as file:
        print(file.write("Content 3"))
        
        
print(p1.name) #full name 
print(p1.stem) #no extension
print(p1.suffix) #just .extension

p2 = Path('files') #directory path
all_file_names_generator = p2.iterdir() #Output of ITERDIR method is a Generator, so it's reading 1 name every time its called 
for item in all_file_names_generator:
    print(item) #type(item) .name .stem . suffix work here 
    
    
    
#else:
#    with open(p1, 'a') as file:
#        print(file.write(p1))
        
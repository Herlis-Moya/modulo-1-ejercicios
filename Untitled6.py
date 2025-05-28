value1 = int(input("Coloca tu primer numero"))

value2 = int(input("Coloca tu segundo numero"))

value3 = int(input("Coloca tu tercer numero"))

if value1 >= (value2 and value3):
    print(value1,"Es el mayor!") 
elif value1 <= value2 and value3:
    print(value1,"Es el menor!")
else:
    print(value1,"No es mayor o menor")
    
if value2 >= (value1 and value3):
    print(value2,"Es el mayor!")
elif value2 <= value1 and value3:
    print(value2,"Es el menor!")
else: 
    print(value2,"No es mayor o menor")
    
if value3 >= (value1 and value2):
    print(value3,"Es el mayor!")
elif value3 <= value1 and value2:
    print(value3,"Es el menor!")
else:
    print(value3,"No es mayor o menor")
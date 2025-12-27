#  program takes the number of rows and columns as input from the user and prints a solid rectangle

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

i = 1
while i <= row:
    
    j = 1
    while j <= column:
        print('*', end=' ')
        j = j + 1 

    print(' ')
    i = i + 1

print('EOP')
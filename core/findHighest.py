num_array = [1,5,7,9,110,15,16,19]
print(num_array)
print(len(num_array))


big = num_array[0]


i = 0

while i<len(num_array):
    print(num_array[i])
    if(num_array[i] > big):
        big = num_array[i]
    i = i + 1

print('Largest Number : ' + str(big) )
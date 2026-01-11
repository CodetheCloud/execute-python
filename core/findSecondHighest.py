num_array = [1,5,7,90,110,15,16,19]
print(num_array)
print(len(num_array))
big = num_array[0]
secondBig = num_array[0]

i = 0
while i<len(num_array):
    print(num_array[i])
    if(num_array[i] > big):
        secondBig = big
        big = num_array[i]
    elif(num_array[i] > secondBig):
        secondBig = num_array[i]
    i = i + 1

print('Largest Number : ' + str(big) )
print('2nd Largest Number : ' + str(secondBig) )


"""
set largest to the first value in the array
set secondLargest to the smallest possible
now iterate thru the array.
if the current value is greater than largest:
    replace secondLargest with Largest
    replace largest with current value
else check to see if current value is greater than secondLargest and assign if true.
"""
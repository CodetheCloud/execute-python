#  Program to Check if a Number is Even or Odd

num = int ( input('Enter any integer : '))

print('You have entered '+ str(num) )

if(num % 2 == 0):
    print(f'Number {num} is Even')
else:
    print(f'Number {num} is Odd')

print('EOP')
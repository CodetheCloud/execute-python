# Program to reverse a string in python

user_text = input('Enter any valid string :')

print(user_text)
user_text_arr = list(user_text)

arr_size = len(user_text_arr)


reverse_arr = []
j = arr_size - 1

while j >= 0:
    print(user_text_arr[j])  # it wil print arr in reverse order
    reverse_arr.append(user_text_arr[j])
    j = j - 1

print(reverse_arr)
result_no_spaces = "".join(reverse_arr)

print(result_no_spaces)
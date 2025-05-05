numbers = [
    11, 5, 8, 32, 15, 3, 20, 
    132, 21, 4, 555, 9, 20
]

filtered_numbers = [
    num for num in numbers 
    if num < 30 and num % 3 == 0
]

print(filtered_numbers)

# Еще можно так
#  numbers = [
#    11, 5, 8, 32, 15, 3, 20, 
#    132, 21, 4, 555, 9, 20
#]

# filtered_numbers = [
#    num for num in numbers 
#   if num < 30 and num % 3 == 0
#]

#print(filtered_numbers)
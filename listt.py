def sum_of_squares(numbers):
   
    sum_squares = 0
    for num in numbers:
        sum_squares += num**2
    return sum_squares

numbers = [2,4,4,5,9,20]
sum_squares = sum_of_squares(numbers)
print(sum_squares)  # Output: 55
# big O notation is used to measure how running time or space requirements for your program grows as input size grows


# ----------------O(n)----------------------
# a size of array size(arr) with 100 operations takes 0.22 milliseconds
# a size of array size(arr) with 1000 operations takes 2.30 milliseconds

# comparing two program,
# time taken can be represented as,
#     time = a*n + b 
#         where a and b are constant and n is the numbers of operations

# we can represent it in terms of fastest growing term as,
#     time = a*n 

# by using drop constant we can represent it as,
#     time = O(n)
#     Big O time complexity of a program is in order of n 


# Eg: 
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return print(squared_numbers)

numbers = [2, 5, 8, 9]
get_squared_numbers(numbers)

# Output: [4, 25, 64, 81]
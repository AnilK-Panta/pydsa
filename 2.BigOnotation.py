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

print("Big O notation in order of n O(n)")
# Eg: 
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return print(squared_numbers)

numbers = [2, 5, 8, 9]
get_squared_numbers(numbers)

# Output: [4, 25, 64, 81]


# ----------------O(1)----------------------
# a size of array size(arr) with 100 operations takes 0.22 milliseconds
# a size of array size(arr) with 1000 operations takes 0.23 milliseconds

# Comparing two programs,
# Time is almost constant, so it is a constant function
# time taken can be represented as,
#     time = a + b

# we can represent it in terms of fastest growing term as,
#     time = a

# by using drop constant we can represent it as,
#     time = O(1)
print("Big O notation in order of 1 O(1)")
# Eg 
def find_first_pe(price, eps, index):
    pe=price[index]/eps[index]
    return print(pe)

find_first_pe([200, 500, 750], [100, 230, 500], 2)

# Output: 1.5


# ----------------O(n2)----------------------
# Time = an2 + c 
print("Big O notation in order of n2 O(n2)")
# Eg 
numbers=[3,6,2,4,3,6,8,9]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i]==numbers[j]:
            print(numbers[i])
            print(" is a dublicate")
            break


# Above examples were for time complexity 
# space complexity also works same but a bit more reliable one 
# Eg:
print("Time v/s Space Complexity")
# Search 68 from the array of numbers 
ArrayNumbers=[4, 9, 15, 21, 34, 57, 68, 91]
# Using Time Complexity:
print("Time Complexity")
for i in range(len(ArrayNumbers)):
    if ArrayNumbers[i]==68:
        print(i)

print("Space Complexity (Binery Search)")
average = len(ArrayNumbers)/2
for average in range(len(ArrayNumbers)):
    if ArrayNumbers[average]==68:
        print(average)
        break
    else:
        if ArrayNumbers[average]>68:
            average= average + average/2
        else:
            average= average - average/2
        

# For Binary Search complexity
# Iteration k=n/2^k 
# 1=n/2^k 
# n=2^k 
# log2n = log22^k 
# log2n = k*log22 
# k = logn 
# O(logn)

# For above example 
# k = O(logn) = log28 = log22^3 = 3*log22 = 3 iterations 
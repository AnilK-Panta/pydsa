# Array Structure
# Stock_Price=[200, 349, 245, 603, 500]
# Stock Price in day one is Stock_Price[0]=200
# Stock Price in day three is Stock_Price[2]=245
# i.e
Stock_Price=[200, 349, 245, 603, 500]
print("Stock Price list for last five day is", Stock_Price)
print("Stock Price in day one is", Stock_Price[0])
print("Stock Price in day three is", Stock_Price[2])

# Some Array Operations and its Big O Notation
# E.g 1
# Find the index of 603
for i in range(len(Stock_Price)):
    if Stock_Price[i]==603:
        print("The index of 603 is: ", i)
# It is O(n)


# E.g 2
# Print all the prices in the array --> ARRAY TRAVERSAL
for i in range(len(Stock_Price)):
    print("Prices in the Array in day ", i , "is", Stock_Price[i])
# It is O(n)

# E.g 3
# Insert 284 at index 1 --> ARRAY INSERTION
Stock_Price.insert(1, 284)
print("After inserting 284 in index 1 the new Array is:", Stock_Price)
# It is O(n)

# E.g 4
# Delete element at index 2 --> ARRAY DELETION
Stock_Price.remove(245)
print("After removing 245 the new Array is:", Stock_Price)


# Mega Exercise 
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Creating Array 
Expense=[2200,2350,2600,2130,2190]

# In Feb, how many dollars you spent extra compare to January?
print('Expense of Feb compared to Jan: ',Expense[1]-Expense[0])

# Find out your total expense in first quarter (first three months) of the year.
print("Total expenses of first quarter:", Expense[0]+Expense[1]+Expense[2])
# total=0
# for i in range(3):
#     total += Expense[i]
#     if i==2:
#         print(total)

# Find out if you spent exactly 2000 dollars in any month
# for i in range(len(Expense)):
#     if Expense[i]==2000:
#         print("Yes")
print("Did I spent 2000 in any month? ", 2000 in Expense)


# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# Expense.insert(5, 1980)

Expense.append(1980)
print('New expense list is: ', Expense)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
Expense[2]=Expense[2]-400
print("Updated list after refund: ",Expense)
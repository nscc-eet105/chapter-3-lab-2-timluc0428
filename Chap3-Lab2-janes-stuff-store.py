#Tim Lucas
#Lab 3-2
#2025 06 10

print("Jane's Stuff Store\n")
#prompt user for number of items they wish to purchase
items_purchased = int(input("How many items would you like purchase? "))
print()

total_price = 0
#use a loop to promt user for price of each item
for i in range(items_purchased):
    price = float(input(f"Enter the price of item {i +1}: "))
    #calculate total cost of all items
    total_price += price    

#calculate average cost of each item
average_cost = total_price / items_purchased
#print out total cost and average cost of each item. 
print(f"\nThe total cost of your items is ${total_price:.2f}")
print(f"The average cost of each item is ${average_cost:.2f}")
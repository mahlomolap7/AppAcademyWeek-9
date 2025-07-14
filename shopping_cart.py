
# Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more products to thier cart
# At the end show the food items and the total cost to the user 

foods = []
prices = []
total =0

while True:
    food = input("Enter a food product (or type 'exit' to finish): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price for {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("\nYour Shopping Cart:")  

for food in foods:
    print(food, end= " ")  
    
for price in prices:
    total += price  
          
print("\n")    
print(f"Your total cost is: R{total}")   
   
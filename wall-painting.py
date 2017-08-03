# 1. Setup
use_per_gallon = 400

# 2. Input
print('Whats the width of the bleeping wall?')
width = float(input())

print('Whats the height of the bleeping wall?')
height = float(input())

print('Whats the cost per bleeping gallon of paint?')
cost = float(input())

print('How many freaking gallons?')
amount = float(input())

area_to_paint = width * height

num_of_gal = area_to_paint / use_per_gallon

total_cost = cost * num_of_gal



# 3. Transform

print("$" + str(total_cost) + " bleeping dollars. STOP WASTING MONEY!")
# 4. Output

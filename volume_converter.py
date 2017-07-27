#setup
liters_per_gallon = 3.785411784

#input
print ('Input gallons')
gallons = float(input())

#transform
liters = liters_per_gallon * gallons

# output
print(str(gallons) +  ' gallons is ' + str(liters) + ' liters. ')

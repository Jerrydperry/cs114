# convert gallons to liters and print it out.

liters_per_gallon = 3.785411784
gallons_per_liters = 1
num = 3.785411784

print("liters to gallons or gallons to liters")


print('how many gallons')
gallons = float(input())

liters = liters_per_gallon * gallons

print(str(gallons) + ' gallons is ' + str(liters) + ' liters.')

print('how many liters?')
liters = float(input())

# almost had it

print(str(liters) + ' liters is ' + str(gallons) + ' gallons.')

#script to convert weight in stone and pounds to kg
# 14 pounds in a stone and one stone is 6.35029kg
stone = 0
pounds = 1
kgTotal = (pounds/14)*6.3509 + stone*6.35029 # had to modify this formula

print("Weight in kg: " + str(kgTotal)) # had to add str() to convert number to string

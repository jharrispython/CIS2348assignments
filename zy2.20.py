# James Harris
# 2078031
cups_lemon = float(input('Enter amount of lemon juice (in cups):\n'))
cups_water = float(input('Enter amount of water (in cups):\n'))
cups_agave = float(input('Enter amount of agave nectar (in cups):\n'))

cups_serving = int(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields %.2f servings' % cups_serving)
print('%.2f cup(s) lemon juice' % cups_lemon)
print('%.2f cup(s) water' % cups_water)
print('%.2f cup(s) agave nectar\n' % cups_agave)

cups_serving2 = float(input('How many servings would you like to make?\n'))

lemon_juice = cups_lemon / cups_serving
water = cups_water / cups_serving
agave_nectar = cups_agave / cups_serving

cups_lemon2 = lemon_juice * cups_serving2
cups_water2 = water * cups_serving2
cups_agave2 = agave_nectar * cups_serving2

print('\nLemonade ingredients - yields %.2f servings' % cups_serving2)
print('%.2f cup(s) lemon juice' % cups_lemon2)
print('%.2f cup(s) water' % cups_water2)
print('%.2f cup(s) agave nectar' % cups_agave2)

gallons_lemon = cups_lemon2/16
gallons_water = cups_water2/16
gallons_agave = cups_agave2/16

print('\nLemonade ingredients - yields %.2f servings' % cups_serving2)
print('%.2f gallon(s) lemon juice' % gallons_lemon)
print('%.2f gallon(s) water' % gallons_water)
print('%.2f gallon(s) agave nectar' % gallons_agave)
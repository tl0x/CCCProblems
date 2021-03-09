burger = int(input()) - 1
side = int(input()) - 1
drink = int(input()) - 1
dessert = int(input()) - 1

burgers = [461, 431, 420, 0]
sides = [100,57,70,0]
drinks = [130,160,118,0]
desserts = [167,266,75,0]

sum = burgers[burger] + sides[side] + drinks[drink] + desserts[dessert]

print(burgers[burger], sides[side], drinks[drink], desserts[dessert])

print("Your total calorie count is " + str(sum) + ".")
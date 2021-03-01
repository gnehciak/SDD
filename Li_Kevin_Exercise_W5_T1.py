def isFloat(i):
    try:
        float(i)
        return True
    except ValueError:
        return False
# 1
ing1, ing2 = input("Ingredient 1: "), input("Ingredient 2: ")
print(ing1, ing2)
# 2
card1, card2 = input("Card 1: "), input("Card 2: ")
while card1 != card2:
    print('Keep playing.')
    card1 = card2
    card2 = input("Card 2: ")
print("Snap")
# 3
price = input("Original Price: ")
while not isFloat(price):
    print("Please enter a valid value")
    price = input("Original Price: ")
print('$', round(float(price) * 0.8, 2), sep='')
# 4
test = {'test 1: ':None, 'test 2: ':None, 'test 3: ':None}
avg = 0
for i in test:
    test[i] = input(i)
    while not isFloat(test[i]):
        print("Please enter a valid value.")
        test[i] = input(i)
    avg += float(test[i])
avg = round(avg/3, 2)
print(f"Your average is: {avg}" if avg <= 90 else f"Congratulations, your result of {avg} is greater than 90!")
# 5
limit = input("Limit: ")
while not limit.isdigit():
    print("Please enter a valid value.")
    limit = input("Limit: ")
squarenum = 1
while squarenum ** 2 <= float(limit):
    print(squarenum ** 2)
    squarenum += 1
# 6
salesp = {}
peep = input("Sales Person: ")
while peep:
    price = input("Price: ")
    while not isFloat(price):
        print("Please enter a valid value.")
        price = input("Price: ")
        price = float(price)
    salesp[peep] = salesp[peep] + round(price*0.1, 2) if peep in salesp else round(price*0.1, 2)
    price = 0
    peep = input("Sales Person: ")
for i in salesp.keys():
    print(i, ' $', round(salesp[i], 2), sep='')

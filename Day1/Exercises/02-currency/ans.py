

def currency_converter(amount):

    amount = int(amount * 100)
    quantities = ("hundred dollar bill", "fifty dollar bill", "twenty dollar bill", "ten dollar bill", 
    "five dollar bill", "one dollar bill", "quarter", "dime", "nickel", "penny")
    quantities_plural = ("hundred dollar bills", "fifty dollar bills", "twenty dollar bills",
    "ten dollar bills", "five dollar bills", "one dollar bills", "quarters", "dimes", "nickels", "pennies")
    values = (10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1)
    for i in range(len(values)):
        total = amount // values[i]
        if total > 1:
            print("You have {} {}".format(total,quantities_plural[i]))
        elif total == 1:
            print("You have {} {}".format(total,quantities[i]))
        amount = amount - total * values[i]

currency_converter(121.33)
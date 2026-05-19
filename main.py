<<<<<<< HEAD
def calculate_total(price, quantity, percentageTax=0):
    total = price * quantity
    total += total * percentageTax / 100
=======
def calculate_total(price, quantity, percentageDiscount):
    total = price * quantity
    total -= total * percentageDiscount / 100
>>>>>>> feature/add-discount-support
    return total


def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity)
    print(f"Total amount: {total}")


main()
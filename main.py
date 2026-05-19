def calculate_total_with_tax(price, quantity, percentageTax=0):
    total = price * quantity
    total += total * percentageTax / 100
def calculate_total_with_discount(price, quantity, percentageDiscount):
    total = price * quantity
    total -= total * percentageDiscount / 100
    return total


def main():
    price = 100
    quantity = 2

    total = calculate_total_with_discount(price, quantity, 10)
    total = calculate_total_with_tax(total, 1, 5)
    print(f"Total amount: {total}")
    print(f"Total amount with tax: {total}")

main()
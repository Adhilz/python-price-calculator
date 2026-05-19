def calculate_total(price, quantity, percentageTax=0):
    total = price * quantity
    total += total * percentageTax / 100
    return total


def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity)
    print(f"Total amount: {total}")


main()
def compute_discount(quantity, price, discount_rate):
    discount_amount = quantity * price * discount_rate
    discounted_price = quantity * price - discount_amount
    return discount_amount, discounted_price

def main():
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))
    discount_rate = float(input("Enter the discount rate (in decimal): "))

    discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

    print(f"\nQuantity: {quantity}")
    print(f"Price per item: ${price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")

if __name__ == "__main__":
    main()

def CalcDiscount(amount, percentage):
    discount_value = (amount * percentage) / 100
    return float(discount_value)

price = 1000.0
discount_percent = 20.0

result = CalcDiscount(price, discount_percent)

print(f"For a price of {price} with a discount of {discount_percent}%,")
print(f"The discount amount is: {result}")
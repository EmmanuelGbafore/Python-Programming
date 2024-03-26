def calculate_discount(price, discount_percentage):
    final_price = (1 - discount_percentage) * price

    if discount_percentage >= 0.2:
        print("Final price after applying the discount:", final_price)
    else:
        print("No discount applied. Original price:", price)

# Prompt the user for inputs
price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount percentage (as a decimal): "))

# Call the function with user inputs
calculate_discount(price, discount_percentage)

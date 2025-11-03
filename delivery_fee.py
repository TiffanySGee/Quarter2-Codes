# Delivery Fee Calculator
# Programmer: (Your Name)
# Grade 8 Project

# Ask the user for the distance and rate
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

# Compute the total delivery fee
total_fee = distance * rate

# Display the result
print("Total Delivery Fee: ₱" + str(format(total_fee, ".2f")))
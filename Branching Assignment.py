# Electric Charges Program

# Prompt for input
kw_hours = int(input("Enter the KW hours used: "))

# Rates in cents
rate_first_1000 = 7.633
rate_over_1000 = 9.259

# Calculate amount owed
if kw_hours <= 1000:
    amount_owed = (kw_hours * rate_first_1000) / 100
else:
    amount_owed = (
        (1000 * rate_first_1000) +
        ((kw_hours - 1000) * rate_over_1000)
    ) / 100

# Output result (rounded to two decimals for extra credit)
print(f"Amount owed is ${amount_owed:.2f}")

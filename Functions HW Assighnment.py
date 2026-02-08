# Function to calculate the area of a circle
def area_of_circle(pi, radius):
    return pi * (radius ** 2)


# Function to calculate total due with tax
def total_due(money, tax_rate):
    return money + (money * tax_rate)


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# ----- Main Program -----

# Area of a Circle
pi = 3.14159
radius = float(input("Enter the radius: "))
area = area_of_circle(pi, radius)
print(round(area, 2))

# Taxes
money = float(input("Enter the money amount: "))
tax_rate_input = input("Enter the tax rate (as a percentage): ")
tax_rate = float(tax_rate_input.replace('%', '')) / 100
total = total_due(money, tax_rate)
print(round(total, 2))

# Temperature Conversion
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(round(celsius, 5))

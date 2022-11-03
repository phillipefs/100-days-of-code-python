"""
Example Input 
weight = 80
height = 1.75

Example Output
80 / 1.75 x 1.75 = 26.1224
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your height in kg: "))

bmi = int(weight / height ** 2)

print(f"The BMI is {bmi}")
"""
year = 365 Days, 52 weeks and 12 months

Create a program using maths and f-strings that tells us how many days, weeks, months we have left if we live intil 90 yerars old. 

Example Input
56 
Output
You have 12410 days, 1768 weeks and 408 months left

"""

age = int(input("What is yout current age ? "))

years_remaining = 90 - age

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
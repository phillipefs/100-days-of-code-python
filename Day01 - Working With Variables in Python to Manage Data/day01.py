import os
print("Welcome to the Band Name Genetator")


while True:
    
    option = input("Select the Option: Create Name Band (c) or Exit (e): ")
    if option =="e":
        break
    else:
        name_city = input("What's name of the city you grew up in ? ")
        name_pet = input("What's your pet's name? ")
        os.system('cls')

        print(f"Your band name could be {name_city} {name_pet}")

print("#### BYE ####")
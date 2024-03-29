#Password Generator Project
import random
import string_utils

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# let = ""
# for i in range(nr_letters):
#   random_char = random.choice(letters)
#   let += random_char

# sym = ""
# for i in range(nr_symbols):
#   random_sym = random.choice(symbols)
#   sym += random_sym

# num = ""
# for i in range(nr_numbers):
#   random_num = random.choice(numbers)
#   num += random_num

# password = let+sym+num
# print(f"Here is your password: {password}")

#----------------------------------------------
# password = ""

# for char in range(nr_letters):
#   password += random.choice(letters)

# for char in range(nr_symbols):
#   password += random.choice(symbols)

# for char in range(nr_numbers):
#   password += random.choice(numbers)

# print(f"Here is your password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = ""

# for char in range(nr_letters):
#   password += random.choice(letters)

# for char in range(nr_symbols):
#   password += random.choice(symbols)

# for char in range(nr_numbers):
#   password += random.choice(numbers)

# password = string_utils.shuffle(password)
# print(f"Here is your password: {password}")

#---------------------------------------------

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list += random.choice(symbols)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Here is your password: {password}")
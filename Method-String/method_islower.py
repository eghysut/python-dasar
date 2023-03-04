# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=islower#str.islower

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi islower() mengembalikan nilai boolean True jika semua karakter dalam huruf kecil,
# jika tidak, maka akan mengembalikan nilai boolean False. 
# Angka, simbol, dan spasi di abaikan, hanya karakter alfabet (a-zA-Z).

# Syntax
# string.islower()

# Nilai Parameter
# tidak ada nilai parameter

x = "hello 123 world"
print(x.islower())  
# Output:
# True

y = "hello_world@gmil.com"
print(y.islower())  
# Output:
# True

print("#!/usr/bin/python".islower()) 
# Output:
# True

x = "Hello 123 World"
print(x.islower())  
# Output:
# False

y = "hello_World@gmail.com"
print(y.islower())  
# Output:
# False

print("#!/usr/bin/Python".islower()) 
# Output:
# False

# periksa apakah karakter huruf kecil semua?
if "python3.8|3.9|3.10".islower():
    print("passed")
else:
    print("failed")
# Output:
# passed

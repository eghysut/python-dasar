# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=capitalize#str.capitalize

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi capitalize()
# mengembalikan string di mana karakter pertama adalah huruf besar.

# Syntax
# string.capitalize()

# Nilai Parameter
# Tidak ada nilai parameter

print("hello world".capitalize())   
# Output:
# Hello world

x = "hello world".capitalize()
print(x)  
# Output:
# Hello world

y = "100 hello world".capitalize()
print(y) 
# Output:
# 100 hello world

# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

s = "hello world"
# string melakukan perubahan
print(s.capitalize())   
# Output:
# Hello world

# string tidak melakukan perubahan
print(s)               
# Output:
# hello world

# string tidak melakukan perubahan
s = "hello world"
s.capitalize()
print(s)    
# Output:
# hello world

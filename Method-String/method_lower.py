# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.lower

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi lower() mengembalikan string di mana semua karakter adalah huruf kecil.
# simbol dan Angka diabaikan.

# Syntax
# string.lower()

# Nilai Parameter
# tidak ada nilai parameter

x = "HELLO WORLD"
print(x.lower())    
# Output:
# hello world

y = "H3Ll0_w0RlD#1"
print(y.lower())    
# Output:
# h3ll0_w0rld#1

print("heLlO_WoRlD@gmail.com".lower())  
# Output:
# hello_world@gmail.com

print("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) 
# Output:
# abcdefghijklmnopqrstuvwxyz

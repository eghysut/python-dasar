# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=swapcase#str.swapcase

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi swapcase() mengembalikan string di mana semua huruf besar menjadi huruf kecil dan sebaliknya.

# Syntax
# string.swapcase()

# Nilai Parameter
# tidak ada nilai parameter

x = "Hello World"
print(x.swapcase())
# Output:
# hELLO wORLD

y = "HELLO WoRlD!"
print(y.swapcase())
# Output:
# hello wOrLd!

print("Alice#Carl#ELIOT".swapcase()) 
# Output:  
# aLICE#cARL#eliot

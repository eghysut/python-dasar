# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isspace#str.isspace

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli. 

# fungsi isspace() mengembalikan nilai boolean True jika semua karakter dalam string adalah spasi putih.
# jika tidak, maka akan mengembalikan nilai boolean False.

# Syntax
# string.isspace()

# Nilai Parameter
# tidak ada nilai parameter

x = " "
print(x.isspace())  
# Output:
# True

y = "\n"
print(y.isspace())  
# Output:
# True

print("\t".isspace())   # True
print("\f".isspace())   # True
print("\r".isspace())   # True

x = " hello world "
print(x.isspace())  
# Output:
# False

y = "  \b"
print(y.isspace())  
# Output:
# False

z = "   s   "
print(z.isspace())  
# Output:
# False

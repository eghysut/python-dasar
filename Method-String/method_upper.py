# -- Method String -- 

# https://docs.python.org/3/library/stdtypes.html?highlight=upper#str.upper

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi upper() mengembalikan string dimana semua karakter dalam huruf besar.
# simbol dan angka diabaikan.

# Syntax
# string.upper()

# Nilai Parameter
# Tidak ada nilai parameter

s = "hello world!".upper()
print(s)    
# Output:
# HELLO WORLD!

s = "99hello world".upper()
print(s)    
# Output:
# 99HELLO WORLD

print("#hello_world123@gmail.com".upper())  
# Output:
# #HELLO_WORLD123@GMAIL.COM


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "hello world!"
# string melakukan perubahan
print(s.upper())    
# Output:
# HELLO WORLD!

# string tidak melakukan perubahan
print(s)    
# Output:
# hello world!

# string tidak melakukan perubahan
x = "hello world!"
x.upper()
print(x)    # hello world

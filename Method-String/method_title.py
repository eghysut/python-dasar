# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=title#str.title

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi title() mengembalikan string di mana karakter pertama di setiap kata adalah huruf besar.
# Seperti header, atau judul.
# Jika kata tersebut mengandung angka atau simbol, huruf pertama setelah itu akan diubah menjadi huruf besar.

# Syntax
# string.title()

# Nilai Parameter
# tidak ada nilai parameter

x = "hello world"
print(x.title())    
# Output:
# Hello World

y = "123hello world"
print(y.title())    
# Output:
# 123Hello World

x = "@alice $carl #eliot"
print(x.title())    
# Output:
# @Alice $Carl #Eliot

print("123a456b789c".title())   
# Output:
# 123A456B789C

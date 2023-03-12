# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=lstrip#str.lstrip

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi lstrip() menghapus semua karakter tertentu atau utama (karakter diawal/dikiri string).
# (defaultnya/standarnya adalah karakter spasi yang akan dihapus)

# Syntax
# string.lstrip(karakter)

# Nilai Parameter
# Parameter             Deskripsi
# karakter              Opsional. Satu set karakter untuk dihapus sebagai karakter utama

x = "   Hello World"
print(x.lstrip()) 
# Output:
# Hello World

y = "https://www.google.com"
print(y.lstrip('htps:/'))   
# Output:
# www.google.com


x = "   hello world    "
print(x.lstrip())
# Output:
# hello world  "ini sebenernya ada karakter (spasi)"

print(x.lstrip(), '<-spasi')  
# Output:
# hello world      <-spasi

print(x.lstrip() + '<-spasi') 
# Output:
# hello world     <-spasi

y = "..,,,Hello, world!"
print(y.lstrip('.,')) 
# Output:
# Hello, world!

# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi strip() menghapus semua karakter awal (spasi di awal) dan akhir 
# (spasi di akhir) (karakter default/standarnya adalah spasi yang akan dihapus)

# Syntax
# string.strip(karakter)

# Nilai Parameter
# Parameter             Deskripsi
# karakter              Opsional. Satu set karakter untuk dihapus sebagai karakter utama/pengikut

x = "   hello world   "
print(x.strip())    
# Output:
# hello world

y = "...hello world..."
print(y.strip('.')) 
# Output:
# hello world

x = "https://www.google.com"
print(x.strip('htps:/'))   
# Output:
# www.google.com

print("hello world".strip('abcdefgh'))  
# Output:
# llo worl

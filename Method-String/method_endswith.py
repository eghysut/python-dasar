# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=endswith#str.endswith

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi endswith() mengembalikan nilai boolean True jika string diakhiri dengan
# nilai yang ditentukan, jika tidak ada akan mengembalikan nilai boolean False.

# Syntax
# string.endswith(value, start, end)

# Nilai Parameter
# paramter          Deskripsi
# value             Dibutuhkan. Nilai untuk memeriksa apakah string diakhiri dengan karakter tertentu.
# start             opsional. Nilai integer yang menentukan di posisi mana untuk memulai pencarian.
# end               opsional. Nilai integer yang menentukan di posisi mana untuk mengakhiri pencarian.

nama = "alice, bob, carl, eliot"
x = nama.endswith('eliot')
print(x)    
# Output:
# True

s = "hello world!"
x = s.endswith("world!")
print(x)    
# OUtput:
# True

y = s.endswith("!")
print(y)    
# Output:
# True

print("hello world.".endswith(".")) 
# Output:
# True

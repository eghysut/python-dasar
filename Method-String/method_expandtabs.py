# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=expandtabs#str.expandtabs

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi expandtabs() menetapkan ukuran tab untuk jumlah tertentu dari spasi.

# Syntax
# string.expandtabs(tabsize)

# Nilai Paramter
# parameter         Deskripsi
# tabsize           Opsional. Angka yang menentukan ukuran tab. Ukuran tab defaultnya adalah 8

s = "hello\tworld!"
print(s.expandtabs())   
# Output:
# hello   world!

print(s.expandtabs(2))  
# Output:
# hello world!

print(s.expandtabs(4)) 
# Output:
# hello   world!

print(s.expandtabs(12)) 
# Output:
# hello       world!

s = "w\to\tr\tl\td"
print(s.expandtabs())   
# Output:
# w       o       r       l       d

print(s.expandtabs(2))  
# Output:
# w o r l d

print(s.expandtabs(4))  
# Output:
# w   o   r   l   d

print(s.expandtabs(10)) 
# Output:
# w         o         r         l         d

# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rfind#str.rfind

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi rfind() menemukan kemunculan terakhir dari nilai yang ditentukan.
# jika nilainya tidak ditemukan mengembalikan -1.
# fungsi rfind() hampir sama dengan fungsi rindex().

# Syntax
# string.rfind(value, start, end)

# Nilai Parameter
# Parameter             Deskripsi
# value                 Dibutuhkan. Nilai yang harus dicari
# start                 Opsional. Di mana untuk memulai pencarian. Standarnya/default adalah 0
# end                   Opsional. Di mana untuk mengakhiri pencarian. Standanya/default adalah ke akhir string.

text = "hello alice carl eliot"
x = text.rfind('alice')
print(x)    
# Output:
# 6

y = text.rfind('carl')
print(y)    
# Output:
# 12

print(text[x:]) 
# Output:
# alice carl eliot

print(text[y:]) 
# Output:
# carl eliot

text = "hello alice carl eliot alice world"
x = text.rfind('alice')
y = text.rfind('e')
z = text.rfind('e', 14, 20)
print(x)    # 23
print(y)    # 27
print(z)    # 17
print(text[x:]) # alice world
print(text[y:]) # e world
print(text[z:]) # eliot alice world

print("hello world".rfind('war'))   
# Output:
# -1

# jika ingin mempelajari lebih lanjut tentang string slice[start:end] kunjungi folder_name: "Bagian1-DASAR/stage09_slice_string.py"

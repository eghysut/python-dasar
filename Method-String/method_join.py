# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi join() mengambil semua item dalam iterable dan menggabungkannya menjadi satu string.
# sebuah string harus ditentukan sebagai pemisah.
# jika ada nilai yang bukan string di iterable, maka akan menghasilkan kesalahan runtime TypeError 

# Syntax
# string.join(iterable)

# Nilai Parameter
# Parameter         Deskripsi
# iterable          Dibutuhkan. Objek apa pun yang dapat diubah di mana semua nilai yang dikembalikan adalah string

# Catatan: 
# Saat menggunakan dict sebagai iterable, nilai yang dikembalikan adalah kuncinya/keys, bukan nilainya/values.

# menggunakan tipe data string
s = "hello world"
x = "#".join(s)
print(x)    
# Output:
# h#e#l#l#o# #w#o#r#l#d

print("-".join("12.030")) 
# Output:
# 1-2-.-0-3-0

# menggunakan tipe data list
l = ['alice', 'carl', 'eliot']
x = " -> ".join(l)
print(x)    
# Output:
# alice -> carl -> eliot

list_num = ['alice', 10, 'carl', 20, 'eliot']
x = " ".join(str(i) for i in list_num)
print(x)    
# Output:
# alice 10 carl 20 eliot

# menggunakan tipe data tuple
t = ('usr', 'bin', 'python')
x = "/".join(t)
print(x)    
# Output:
# usr/bin/python

print("-".join(str(i) for i in (10, 5.5, 20))) 
# Output:
# 10-5.5-20

# menggunakan tipe data dict
# Catatan: 
# Saat menggunakan dict sebagai iterable, nilai yang dikembalikan adalah kuncinya/keys, bukan nilainya/values.
d = {'nama':'alice', 'usia':'23', 'email':'alice@gmail.com'}
x = ":".join(d)
print(x)    
# Output:
# nama:usia:email

print(":".join(d.values())) 
# Output:
# alice:23:alice@gmail.com

dict_num = {'nama':'alice', 'usia':23, 'nrp':555444}
print(" ".join(str(val) for val in dict_num.values()))  
# Output:
# alice 23 555444

# Berhati-hatilah jika anda memiliki iterabel yang memiliki, ukuran atau item 1
print("b".join('a'))    # a
print("b".join(['a']))  # a
print("b".join(('a')))  # a
# fungsi join() sangat cerdas karena menyisipkan, item atau data anda di antara string iterable yang ingin anda ikuti,
# ini berarti bahwa jika anda melewati iterable, ukuran atau item 1,
# anda tidak akan melihat fungsi join()

print("b".join('ac'))       # abc
print("b".join(['a', 'c'])) # abc
print("b".join(('a', 'c'))) # abc

# jika ingin mempelajari lebih lanjut tentang method-list kunjungi folder_name: "Method-List"
# jika ingin mempelajari lebih lanjut tentang method-dict kunjungi folder_name: "Method-Dict"
# jika ingin mempelajari lebih lanjut tentang comprehension kunjungi folder_name: "python-comprehension"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan str() kunjungi folder_name: "Fungsi-Bawaan"

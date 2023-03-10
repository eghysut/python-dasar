# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.pop

# fungsi pop() menghapus item yang ditentukan dari dictionary.
# Nilai item yang dihapus adalah nilai kembalian dari fungsi pop().

# Syntax
# dictionary.pop(namakey, defaultvalue)

# Nilai Parameter
# Parameter                 Deskripsi
# namakey                   Dibutuhkan. Nama keys/kunci item yang ingin Anda hapus.
# defaultvalue              Opsional. Nilai untuk dikembalikan jika nama kunci yang ditentukan tidak ada.
#                           Jika parameter ini tidak ditentukan, dan item dengan kunci yang ditentukan tidak ditemukan, 
#                           pesan kesalahan akan muncul.

# menghapus "alamat" dari dictionary
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarata'}
dictku.pop('alamat')
print(dictku)   
# Output:
# {'nama': 'alice', 'usia': 23}

# mengembalikan nilai yang dihapus
dictku = {'nama':'carl', 'usia':26, 'alamat':'bandung'}
hasil = dictku.pop('alamat')
print(hasil)    
# Output:
# bandung

# menggunakan parameter nilai default
dictku = {'nama':'alice', 'usia':23}
hasil = dictku.pop('alamat', 'tidak ada')
print(hasil)
# Output:
# tidak ada

# jika nama kunci tidak ada, akan menampilkan pesan kesalahan KeyError
dictku = {'nama':'eliot', 'usia':22, 'alamat':'surabaya'}
dictku.pop('jurusan')
print(dictku)
# Output:
# Traceback (most recent call last):
#   File "method_pop.py", line 28, in <module>
#     dictku.pop('jurusan')
# KeyError: 'jurusan'

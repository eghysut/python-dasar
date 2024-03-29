# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.issubset

# fungsi issubset() mengembalikan nilai boolean True jika semua item dalam set ada di set yang ditentukan,
# jika tidak maka mengembalikan nilai boolean False.

# Syntax
# set.issubset(set)

# Nilai Parameter
# Parameter                 Deskripsi
# set                       Dibutuhkan. Set untuk mencari item yang sama

# mengembalikan True jika semua item di set x ada di set y
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'alice', 'carl', 'eliot'}
hasil = x.issubset(y)
print(hasil)    
# Output:
# True

x = {1, 2, 3}
y = {6, 5, 4, 3, 2, 1}
hasil = x.issubset(y)
print(hasil)    
# Output:
# True

# mengembalikan False jika tidak semua item dalam set x ada di set y
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'alice', 'carl'}
hasil = x.issubset(y)
print(hasil)    
# Output:
# False

x = {1, 2, 3}
y = {6, 5, 4, 3, 2}
hasil = x.issubset(y)
print(hasil)    
# Output:
# False

# sementara set dianggap sebagai set bagian dari dirinya sendiri.
x = {'alice', 'carl', 'eliot'}
hasil = x.issubset(x)
print(hasil)    
# Output:
# True

# menggunakan operator comparison/perbandingan <=
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'alice', 'carl', 'eliot'}
hasil = x <= y
print(hasil)    
# Output:
# True

x = {1, 2, 3}
y = {6, 5, 4, 3, 2, 1}
hasil = x <= y
print(hasil)    
# Output:
# True

# mengembalikan False jika tidak semua, item dalam set x ada di set y
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'alice', 'carl'}
hasil = x <= y
print(hasil)    
# Output:
# False

x = {1, 2, 3}
y = {6, 5, 4, 3, 2}
hasil = x <= y
print(hasil)    
# Output:
# False

# sementara set dianggap sebagai set bagian dari dirinya sendiri.
x = {'alice', 'carl', 'eliot'}
hasil = x <= x
print(hasil)    
# Output:
# True

# menggunakan operator comparison/perbandingan <
# Catatan: Operator <adalah satu-satunya cara untuk menguji apakah suatu 
# set adalah subset yang tepat. 
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'alice', 'carl', 'eliot'}
hasil = x < y
print(hasil)    
# Output:
# True

# suatu set bukanlah sebagai set bagian dari dirinya sendiri.
x = {'alice', 'carl', 'eliot'}
hasil = x < x
print(hasil)   
# Output:
# False

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"

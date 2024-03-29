# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.discard

# fungsi discard() menghapus item yang ditentukan dari set.
# fungsi ini berbeda dengan fungsi remove(), karena
# fungsi remove() akan memunculkan error jika item yang ditentukan tidak ada,
# dan fungsi discard() tidak akan memunculkan pesan error.

# Syntax
# set.discard(value)

# Nilai Parameter
# Parameter                     Deskripsi
# value                         Dibutuhkan. Item yang akan dicari, dan dihapus.

# Catatan: contoh di Output ini dengan Output Anda akan berbeda, karena data set tidak terurut

# menghapus elemen dari set
x = {'alice', 'carl', 'eliot'}
x.discard('eliot')
print(x)    
# Output:
# {'alice', 'carl'}

# tidak memunculkan pesan error runtime
x.discard('hello')
print(x)    
# Output:
# {'alice', 'carl'}

# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.pop

# fungsi pop() menghapus item acak dari set.
# Metode ini mengembalikan item yang dihapus.

# Syntax
# set.pop()

# Nilai Parameter
# tidak ada nilai parameter

# Catatan: contoh di Output ini dengan Output Anda akan berbeda, karena data set tidak terurut 

x = {'alice', 'carl', 'eliot'}
x.pop()
print(x)    
# Output:
# {'eliot', 'alice'}

# Catatan: fungsi pop() mengembalikan nilai yang dihapus.
x = {'alice', 'carl', 'eliot'}
hasil = x.pop()
print(hasil)    # carl 
print(x.pop())  # eliot

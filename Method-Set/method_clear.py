# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.clear

# fungsi clear() menghapus semua elemen dalam satu set.

# Syntax
# set.clear()

# Nilai Parameter
# tidak ada nilai parameter

# Catatan: contoh di Output ini dengan Output Anda akan berbeda, karena data set tidak terurut 

setku = {'alice', 'carl', 'eliot'}
print(setku)
# Output:
# {'carl', 'alice', 'eliot'}

setku.clear()

print(setku)
# Output:
# set()

# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.copy

# fungsi copy() menyalin set.

# Syntax
# set.copy()

# Nilai Parameter
# tidak ada nilai parameter

# Catatan: contoh di Output ini dengan Output Anda akan berbeda, karena data set tidak terurut 

setku = {'alice', 'carl', 'eliot'}
set_copy = setku.copy()
print(setku)
# Output:
# {'carl', 'alice', 'eliot'}

print(set_copy)

print(setku == set_copy)    
# Output:
# True

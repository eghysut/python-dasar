# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isdecimal#str.isdecimal

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isdecimal() mengembalikan nilai boolean True jika semua karakter decimal (0-9)
# dan bisa juga digunakan pada objek unicode

# Syntax
# string.isdecimal()

# Nilai Parameter
# tidak ada nilai parameter

x = "0123456789" # int
y = "\u0030"     # unicode
print(x.isdecimal())    # True
print(y.isdecimal())    # True


h = "0xff"
b = "0b11"
f = "2.0"
print(h.isdecimal()) # False
print(b.isdecimal()) # False
print(f.isdecimal()) # False

emoji = "🤨" # emoji unicode
print(emoji.isdecimal())    
# Output:
# False

alphabet = "αβγδεζηθικλμνξοπρςστυφχψ" # alphabet unicode
print(alphabet.isdecimal()) 
# Output:
# False

pecahan = "½"
print(pecahan.isdecimal())  
# Output:
# False

print("hello123".isdecimal())   
# Output:
# False

x = "\u0030" # int 0 unicode
print(x.isdecimal())    
# Output:
# True

y = "\u0039" # int 9 unicode
print(y.isdecimal()) 
# Output:
# True

print(int(x, base=16))  
# Output:
# 0

print(int(y, base=16))  
# Output:
# 9
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan int() kunjungi folder_name: "Fungsi-Bawaan/fungsi_int.py"

# menghasilkan karakter unicode
#def kode_unicode(nomor_kode):
#    return chr(int(nomor_kode.lstrip("U+").zfill(3), base=16))
#
#for i in range(30, 81): # range(1, 1000)
#    print(fr"\u" + str(i).zfill(3), kode_unicode("U+" + str(i)))

# jika ingin mempelajari lebih lanjut tentang formating string kunjungi folder_name: "python-formatting"
# jika ingin mempelajari lebih lanjut tentang encoding unicode kunjungi folder_name: "python-encoding"

# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=splitlines#str.splitlines

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi splitlines() membagi string menjadi tipe data list. 
# Pemisahan dilakukan pada jeda baris.

# Syntax
# string.splitlines(jedabaris)

# Nilai Parameter
# Parameter             Deskripsi
# jedabaris             Opsional. Menentukan apakah jeda baris harus disertakan (True), atau tidak (False). Nilai default adalah False

x = "hello \nworld"
print(x.splitlines())       
# Output:
# ['hello ', 'world']

y = "hello \nworld"
print(y.splitlines(True))   
# Output:
# ['hello \n', 'world']

x = """Python adalah bahasa pemrograman tujuan umum yang ditafsirkan, 
tingkat tinggi. Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, 
filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan."""
print(x.splitlines())

x = "hello alice carl eliot"
print(x.splitlines())   
# Output:
# ['hello alice carl eliot']

# jika ingin mempelajari lebih lanjut tentang Method-List kunjungi folder_name: "Method-List"

# Dalam Python, Magic method __abs__() adalah metode khusus dalam Python
# yang digunakan untuk mengimplementasikan operasi nilai mutlak (abs) pada suatu objek.
# Metode ini memungkinkan Anda untuk menentukan perilaku nilai mutlak kustom pada objek Anda.

# Definisi:
# Metode __abs__() digunakan untuk mengimplementasikan operasi nilai mutlak pada objek. 
# Metode ini mengembalikan nilai mutlak dari objek saat ini

# Syntax:
# def __abs__(self):
#   Implementasi logika nilai mutlak
#   Mengembalikan nilai mutlak dari self

# Parameter:
# self: Merujuk pada objek saat ini.

# Contoh penggunaan magic method __abs__():
class NilaiAbsolut:
    def __init__(self, nilai):
        self.nilai = nilai

    def __abs__(self):
        return abs(self.nilai)

# membuat objek NilaiAbsolut
x = NilaiAbsolut(-10)

# nilai Absolut(mutlak) dari objek x
hasil = x.__abs__()
print(hasil)
# Output:
# 10

# menggunakan fungsi bawaan abs()
print(abs(x))
# Output:
# 10

# membuat objek NilaiAbsolut
y = NilaiAbsolut(1+2j)

# nilai Absolut(mutlak) dari objek y
hasil = y.__abs__()
print(hasil)
# Output:
# 2.23606797749979

# menggunakan fungsi abs()
print(abs(y))
# Output:
# 2.23606797749979

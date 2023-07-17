# Magic method __floordiv__ adalah method khusus dalam Python 
# yang digunakan untuk mengimplementasikan operasi pembagian bulat (floor division) (//) pada objek.
# method ini memungkinkan objek untuk berperilaku seperti tipe data bawaan yang mendukung operasi pembagian bulat.

# Deskripsi:
# Method __floordiv__ digunakan untuk mengubah perilaku operasi floor
# division ketika operator // digunakan pada objek.

# Syntax:
# def __floordiv__(self, other):
    # implementasi floor division

# Parameter
# self: Merupakan objek yang menggunakan operator //.
# other: Merupakan objek yang menjadi operand kedua dalam operasi floor division.
# nama parameter "other" bisa diganti dengan nama apapun.

# Ketika Anda menggunakan operator pembagian bulat (//) antara dua objek,
# Python akan mencari dan memanggil magic method __floordiv__ pada objek pertama,
# dan meneruskan objek kedua sebagai argumen. 
# method ini harus mengembalikan hasil pembagian bulat objek tersebut.

# Berikut adalah contoh penggunaan magic method __floordiv__ pada suatu kelas:
class Floordiv:
    def __init__(self, nilai):
        self.nilai = nilai

    def __floordiv__(self, other):
        return Floordiv(self.nilai // other.nilai)

# membuat objek Floordiv
obj1 = Floordiv(10)
obj2 = Floordiv(2)

# pembagian bulat antara dua objek obj1 dengan obj2
hasil = obj1 // obj2
print(hasil.nilai)
# Output:
# 5

class Fraction:
    def __init__(self, nilai):
        self.nilai = nilai

    def __floordiv__(self, other):
        if type(self.nilai) == list:
            hasil = []
            for i, j in zip(self.nilai, other.nilai):
                hasil.append(i // j)
            return hasil
        else:
            return Fraction(self.nilai // other.nilai)

# membuat objek Fraction
obj1 = Fraction([10, 20, 30])
obj2 = Fraction([2, 5, 6])

hasil = obj1 // obj2
print(hasil)
# Output:
# [5, 4, 5]

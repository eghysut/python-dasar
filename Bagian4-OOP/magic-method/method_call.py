# method __call__() adalah method khusus yang digunakan untuk memungkinkan objek dipanggil seperti fungsi.
# Method ini digunakan untuk memberikan sifat fungsi pada objek, 
# sehingga objek dapat diperlakukan seperti fungsi dan dipanggil dengan argumen.

# Ketika suatu objek dipanggil, Python akan mencari method __call__() pada kelas objek. 
# Jika method __call__() ditemukan, maka Python akan memanggil method tersebut dan menjalankan blok kode di dalamnya.
# Method __call__() biasanya digunakan untuk mengimplementasikan objek yang dapat dipanggil, 
# seperti decorator atau class-based views pada web framework.

# Syntax
# class MyClass:
#    def __call__(self, arg1, arg2, ...):
        # kode yang akan dijalankan saat objek dipanggil seperti fungsi

# Nilai Parameter
# Parameter             Deskripsi
# self                  merujuk pada objek itu sendiri.
# arg1, arg2, ...       argumen yang diberikan saat objek dipanggil seperti fungsi.

# Dalam method __call__(), kita dapat menentukan logika atau kode yang 
# ingin dijalankan ketika objek tersebut dipanggil seperti fungsi. 
# Kode yang dituliskan pada method __call__() akan dieksekusi saat objek dipanggil seperti fungsi.

# Berikut ini adalah contoh sederhana penggunaan metode __call__()
class A:
    def __call__(self):
        return "hello world"

x = A()
y = A()
print(x())
print(y())
# Output:
# hello world
# hello world

# menjumlahkan dari setiap bilangan 
class Tambah:
    def __init__(self):
        self.total = 0
    
    def __call__(self, *args):
        for i in args:
            self.total += i
        return self.total

# membuat objek dan memanggilnya
tambah = Tambah()
print(tambah(1, 2)) # 1 + 2 = 3
# Output:
# 3

print(tambah(5, 5)) # 3 + 5 + 5 = 13
# Output:
# 13

print(tambah(10, 20, 30))   # 13 + 10 + 20 + 30 = 73
# Output:
# 73

# contoh menggunakan argumen *args dan **kwargs
class A:
    def __init__(self):
        print('Objek dibuat')
    
    def __call__(self, *args, **kwargs):
        print('Objek dipanggil dengan argumen:', args, kwargs)

# Membuat objek dan memanggilnya
obj = A()
obj(1, 2, a=3, b=4)
# Output:
# Objek dibuat
# Objek dipanggil dengan argumen: (1, 2) {'a': 3, 'b': 4}

# Berikut beberapa contoh tambahan menggunakan fungsi decorator:
import time

class root:
    def __init__(self, func):
        self.func = func
        self.jumlah = 0

    def __call__(self, *args, **kwargs):
        self.jumlah += 1
        print(f"\rMemanggil fungsi {self.func.__name__}: {self.jumlah}", end='', flush=True)
        rv = self.func(*args, **kwargs)
        return rv

@root
def fibonaci(n):
    if n < 2:
        return n
    else:
        #print(n)
        return fibonaci(n - 1) + fibonaci(n - 2)

start = time.perf_counter()
fibonaci(20)
end = time.perf_counter()

result = end - start
print(f"\ntimes: {result} second")
# Output:
# Memanggil fungsi fibonaci: 21891
# times: 8.8199903 second
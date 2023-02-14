# tipe data python
# dalam pemrograman, tipe data merupakan konsep penting.
# variabel dapat menyimpan data dari tipe yang berbeda,
# dan tipe yang berbeda dapat melakukan hal yang berbeda

# python memiliki tipe data bawaan secara default, berikut dalam kategori:
# Tipe Text:        str
# Tipe Numerik:     int, float, complex
# Tipe Urutan:      list, tuple, range
# Tipe Pemetaan:    dict
# Tipe Set:         set, frozenset
# Tipe Boolean:     bool
# Tipe Biner:       bytes, bytearray, memoryview
# Tipe Tidak ada:   NoneType

# Menadapatkan tipe data
# fungsi type() menampilkan tipe data objek apa pun
x = 5
print(type(x), x)
# Output:
# <class 'int'> 5

# Mengatur tipe data di python, 
# tipe data diatur saat anda menetapkan nilai ke variabel

# tipe set
str_x = "hello world"
print(type(str_x), str_x)   
# Output:
# <class 'str'> hello world

# tipe int
int_x = 10
print(type(int_x), int_x)   
# Output:
# <class 'int'> 10

# tipe float
float_x = 10.5
print(type(float_x), float_x)   
# Output:
# <class 'float'> 10.5

# tipe complex
complex_x = 1j
print(type(complex_x), complex_x)   
# Output:
# <class 'complex'> 1j

# tipe list
list_x = ['alice', 'carl', 'eliot']
print(type(list_x), list_x)     
# Output:
# <class 'list'> ['alice', 'carl', 'eliot']

# tipe tuple
tuple_x = ('alice', 'carl', 'eliot')
print(type(tuple_x), tuple_x)   
# Output:
# <class 'tuple'> ('alice', 'carl', 'eliot')

# tipe range
range_x = range(5)
print(type(range_x), range_x)   
# Output:
# <class 'range'> range(0,5)

# tipe dict
dict_x = {'nama':'alice', 'usia':23}
print(type(dict_x), dict_x)     
# Output:
# <class 'dict'> {'nama':'alice', 'usia':23}

# tipe set
set_x = {'alice', 'carl', 'eliot'}
print(type(set_x), set_x)       
# Output:
# <class 'set'> {'alice', 'carl', 'eliot'}

# tipe frozenset
frozen_x = frozenset({'alice', 'carl', 'eliot'})
print(type(frozen_x), frozen_x) 
# Output:
# <class 'frozenset'> frozenset({'eliot', 'carl', 'alice'})

# tipe boolean
true_x = True
false_x = False
print(type(true_x), true_x)     # <class 'bool'> True
print(type(false_x), false_x)   # <class 'bool'> False

# tipe biner
bytes_x = b"hello world"
bytes_y = bytes(10)
bytearray_x = bytearray(5)
bytmemory_x = memoryview(bytes(5))
print(type(bytes_x), bytes_x)   # <class 'bytes'> b'hello world'
print(type(bytes_y), bytes_y)   # <class 'bytes'> b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(type(bytearray_x), bytearray_x)   # <class 'bytearray'> bytearray(b'\x00\x00\x00\x00\x00')
print(type(bytmemory_x), bytmemory_x)   # <class 'memoryview'> <memory at 0x00000272DCADE200> 

# tipe tidak ada
none_x = None
print(type(none_x), none_x)    
# Output:
# <class 'NoneType'> None

#===============================================================================
# mengatur tipe data tertentu
# jika anda ingin menentukan tipe data, anda dapat menggunakan fungsi konstraktor python:
# ada beberapa contoh ini berkaitan dengan casting tipe data. file_name "stage7_casting_type_data.py"

str_x = str("hello world")
str_y = str(100)
print(str_x)  # hello world
print(str_y)  # 100

int_x = int("23") 
int_y = int(15.500)
print(int_x)  # 23
print(int_y)  # 15.0

float_x = float('15')
float_y = float(15)
print(float_x)  # 15
print(float_y)  # 15.0

complex_x = complex(1.9999999999j)
print(complex_x)  # 1.9999999999j

list_x = list(('alice', 'carl', 'eliot'))
list_y = list(range(5))
print(list_x) # ['alice', 'carl', 'eliot']
print(list_y) # [0, 1, 2, 3, 4]

tuple_x = tuple(['alice', 'carl', 'eliot'])
tuple_y = tuple('hello world')
print(tuple_x)                # ('alice', 'carl', 'eliot')
print(tuple_y, type(tuple_y)) # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd') <class 'tuple'>

dict_x = dict(nama='alice', usia=23)
print(dict_x) # {'nama': 'alice', 'usia': 23}

set_str = set('hello world')
set_list = set(['alice', 'carl', 'eliot'])
set_tuple = set(('alice', 'carl', 'eliot'))
print(set_str)    # {'o', 'l', 'd', 'r', 'w', ' ', 'h', 'e'}
print(set_list)   # {'eliot', 'carl', 'alice'}
print(set_tuple)  # {'eliot', 'carl', 'alice'}

true_x = bool(1)
false_y = bool(0)
print(true_x)     # True
print(false_x)    # False

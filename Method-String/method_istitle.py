# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=istitle#str.istitle

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi istitle() mengembalikan nilai boolean True jika semua kata dalam teks dimulai dengan huruf besar,
# DAN sisa kata adalah huruf kecil, jika tidak, maka akan mengembalikan nilai boolean False.
# Simbol dan angka diabaikan.

# Syntax
# string.istitle()

# Nilai Parameter
# tidak ada nilai parameter

x = "Hello World"
print(x.istitle()) 
# Output:
# True

y = "Hello Alice, Carl, Eliot"
print(y.istitle())  
# Output:
# True

print("123 Hello_@World!#1".istitle()) 
# Output:
# True

print("#!/Usr/Bin/Python3".istitle()) 
# Output:
# True

x = "Hello world"
print(x.istitle()) 
# Output:
# False

y = "Hello Alice, carl, eliot"
print(y.istitle()) 
# Output:
# False

print("#!/Usr/Bin/python3".istitle()) 
# Output:
# False

print("#Hello_world@gmail.com".istitle()) 
# Output:
# False

# periksa apakah karakter diawali dengan huruf besar?
if "Python3.8|Python3.9|Python3.10".istitle():
    print("passed")
else:
    print("failed")
# Output:
# passed

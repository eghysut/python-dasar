# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isupper#str.isupper

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isupper() mengembalikan nilai boolean True jika semua karakter dalam huruf besar.
# jika tidak, maka akan mengembalikan nilai boolean False.
# Angka, simbol, dan spasi tidak diperiksa atau diabaikan, hanya karakter alfabet(a-zA-Z).

# Syntax
# string.isupper()

# Nilai Parameter
# tidak ada nilai parameter

x = "HELLO WORLD"
print(x.isupper())  
# Output:
# True

y = "#HELLO@123WORLD"
print(y.isupper())  
# Output:
# True

print("HELLO @ALICE, @CARL, @ELIOT".isupper())  
# Output:
# True

print("!A@B#C$D%E^F&G*H(I)J-K+L_M=".isupper())  
# Output:
# True

x = "Hello World"
print(x.isupper())  
# Output:
# False

y = "Hello123WorlD"
print(y.isupper())  
# Output:
# False

print("HELLO @Alice, @Carl, @Eliot".isupper())  
# Output:
# False

print("!A@B#C$D%E^F&G*H(I)J-K+L_m=".isupper())  
# Output:
# False

# Periksa apakah karakter memiliki huruf besar semua?
if "PYTHON3.8|PYTHON3.9|PYTHON3.10".isupper():
    print("passed")
else:
    print("failed")
# Output:
# passed

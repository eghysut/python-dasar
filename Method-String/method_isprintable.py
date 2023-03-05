# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isprintable#str.isprintable

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli. 

# fungsi isprintable() mengembalikan nilai boolean True jika semua karakter dapat dicetak.
# jika tidak, maka akan mengembalikan nilai boolean False.
# Contoh karakter yang tidak dapat dicetak dapat berupa karakter escape/pelarian
# \r(carriage return), \n(newline), \t(tab), \b(backspace), \f(form feed)

# Syntax
# string.printable()

# Nilai Parameter
# tidak ada nilai parameter

x = "hello world"
print(x.isprintable())  
# Output:
# True

y = "#hello123world_@gmail.com"
print(y.isprintable())  
# Output:
# True

x = "hello\nworld"
print(x.isprintable())  
# Output:
# False

y = "hello\tworld"
print(y.isprintable()) 
# Output:
# False

print("hello\rworld".isprintable()) 
# Output:
# False

print("hello\fworld".isprintable()) 
# Output:
# False

print("hello\bworld".isprintable()) 
# Output:
# False

# periksa apakah ada kerakter pelarian/escape?
if "\u0030".isprintable():
    print("passed")
else:
    print("failed")
# passed

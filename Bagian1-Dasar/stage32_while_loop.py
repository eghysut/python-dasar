# definisi looping/perulangan
# Secara umum, looping atau perulangan pada Python adalah instruksi kode program 
# yang dieksekusi berulang kali. 
# Fungsinya untuk memerintah komputer melakukan sesuatu secara berulang-ulang 
# dengan jumlah tertentu selama sebuah kondisi yang telah ditentukan masih terpenuhi.

# while loop adalah perulangan uncountable atau perulangan yang jumlah proses 
# pengulangannya tidak ditentukan. 
# Ia akan menjalankan baris kode di dalam blok kodenya secara terus menerus 
# selama masih memenuhi ekspresi yang sudah ditentukan sebelumnya, 
# yang berarti ia akan terus mengulang selama kondisi bernilai True.

# Syntax
# while <conditional>:
#     <exppresion>

# <conditional> dapat berupa operator matematika, logika fungsi atau nilai boolean
# <expression> sebuah pernyataan apapun yang akan dieksekusi berulang kali selama <conditional> bernilai True.

# menggunakan operator comparison/perbandingan
x = 0
while x < 3:
    # ini disebut sebagai increment
    # x = x + 1
    # kode ini setara dengan diatas
    x += 1 # step base 
    print("hello world")
# Output:
# hello world
# hello world
# hello world

# Kode di atas akan mencetak "hello world" sebanyak 3 kali.
# karena while loop akan berjalan selama nilai dari variabel "x" kurang dari 3.
# Pada setiap iterasi, nilai variabel "x" akan ditambahkan 1 menggunakan operator "+=", 
# dan kemudian "hello world" akan dicetak ke layar. 
# Setelah variabel "x" mencapai nilai 3, loop berhenti dan program keluar dari loop/perulangan.

# menggunakan operator comparison/perbandingan
y = 3
while y > 0:
    # ini disebut sebagai decrement
    # y = y - 1
    # kode ini setara dengan diatas
    y -= 1
    print("hello alice")
# Output:
# hello alice
# hello alice
# hello alice

# Kode di atas akan mencetak "hello alice" sebanyak 3 kali.
# karena variabel "y" awalnya memiliki nilai 3. 
# Pada setiap iterasi, nilai "y" dikurangi satu dan kemudian "hello alice" dicetak. 
# Loop akan terus berlanjut hingga nilai "y" kurang dari atau sama dengan nol.

# menggunakan fungsi bawaan python len()
listku = ['alice', 'carl', 'eliot']
# print(len(listku)) # 3
while len(listku):
    # menggunakan fungsi pop() menghapus elemen list pada posisi yang ditentukan.
    # defaulnya -1 "menghapus element diakhir"
    x = listku.pop()
    print(f"nama {x} telah dihapus")
# Output:
# nama eliot telah dihapus
# nama carl telah dihapus
# nama alice telah dihapus

# Kode di atas akan menghapus setiap elemen yang terdapat pada listku,
# dengan menggunakan method pop() hingga list kosong. 
# Pada setiap iterasi while loop, elemen terakhir pada list dihapus menggunakan method pop(),
# dan elemen tersebut akan dicetak dalam bentuk string dengan format tertentu. 
# Loop akan berhenti saat panjang list menjadi 0.

x = ['alice', 'carl', 'eliot']
y = []
print(bool(x))  # Output: True
print(bool(y))  # Output: False
    
# Ringkasan:
# Perulangan akan terus berjalan selama kondisi yang diberikan dalam <conditional> bernilai True. 
# Setiap kali iterasi dilakukan, ekspresi yang terdapat dalam <expression> akan dieksekusi. 
# Saat kondisi pada <conditional> akhirnya bernilai False, program akan keluar dari perulangan 
# dan melanjutkan eksekusi kode berikutnya.

# jika anda ingin mengetahui tentang while loop dengan berbagai statement kunjungi folder_name: "python-looping"
# jika anda ingin mengetahui tentang operator comparison kunjungi folder_name: "python-operator"

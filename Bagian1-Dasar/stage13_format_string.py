# fungsi format() mengambil argumen yang diteruskan, untuk memformatnya dan 
# menempatkan string di mana placeholder {} berada.

x = 20
txt = "berapakah jumlah x: {}"
print(txt.format(x))    
# Output:
# berapakah jumlah x: 20

nama = "alice"
usia = 23
data = "nama: {} usia: {}"
print(data.format(nama, usia))  
# Output:
# nama: alice usia: 23

# fungsi format() dapat mengambil argumen dalam jumlah tak terbatas dan 
# tempatkan ke masing-masing placeholder {}.
nama = "alice"
usia = 23
email = "alice@gmail.com"
jurusan = "teknik komputer"
data_mahasiswa = "nama: {} usia: {} email: {} jurusan: {}"
print(data_mahasiswa.format(nama, usia, email, jurusan))
# Output:
# nama: alice usia: 23 email: alice@gmail.com jurusan: teknik komputer

# fungsi format() dapat menggunakan nomor indeks {0} untuk memastikan argumen
# ditempatkan di tempat penampung yang benar.
nama = "alice"
usia = 23
email = "alice@gmail.com"
text = "email: {2} nama: {0} usia: {1}"
print(text.format(nama, usia, email))  
# Output:
# email: alice@gmail.com nama: alice usia: 23

print("hello {}".format("world"))  # hello world

# menggunakan f-string
nama = "alice"
usia = 23
print(f"nama: {nama} usia: {usia}")     
# Output:
# nama: alice usia: 23

# jika ingin mempelajari lebih lanjut tentang pemformatan string python kunjung folder_name: "python-formatting/formatting_format.py"

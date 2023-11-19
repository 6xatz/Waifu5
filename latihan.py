# Akses List
list1 = ["0", "10", "20", "30", "40"]
print("Tampilkan elemen ke 3:", list1[3])
print("Nilai elemen ke 2 sampai 4:", list1[2:5])
print("Elemen terakhir:", list1[4], "\n")

# Merubah Elemen List
print("Merubah elemen ke 4")
list2 = [0, 1, 2, 3, 4]
print("List awal:", list2)
list2[4] = "6xatz"
print("List akhir:", list2)
print("Merubah semua elemen")
list3 = ["nol", "satu", "dua", "tiga", "empat"]
print("List awal:", list3)
list3[0:6] = [0, 1, 2, 3, 4]
print("List akhir:", list3, "\n")

# Menambah Elemen List
lista = [1, 2, 3]
listb = [6, 7, 8]
print("List sebelum dimodifikasi")
print("List A:", lista)
print("List B:", listb)
listb[2:2] = lista[0:2]
print("Mengambil 2 bagian List B dan A:", listb)
listb.append("6xatz")
print("Menambahkan List B dengan string:", listb)
listb.extend([12, 24, 28])
print("Menambahkan List B dengan 3 nilai:", listb)
listx = lista + listb
print("Menggabungkan List A dan List B:", listx, "\n")

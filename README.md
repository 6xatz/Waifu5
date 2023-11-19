## Mata Kuliah
Sebagai tugas praktikum: [5] Bahasa Pemrograman | Universitas Pelita Bangsa. 

## Latihan
<p align="left">
  <img src="/ss/latihan.jpg" width="450">
</p>

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

fungsi dan penjelasan sudah tertera pada ***#*** dan ***print*** diatas.

## Praktikum 5
<p align="left">
  <img src="/ss/praktikum5.png" width="400">
  <img src="/ss/flowchart.jpg" width="130">
</p>

    # List Initialization
    nama = []
    nim = []
    nilaiTugas = []
    nilaiUTS = []
    nilaiUAS = []
    nilaiAkhir = []

    print()

    # Input
    while True:
        nama.append(input("Masukan Nama: "))
        nim.append(input("Masukan NIM: "))
        nilaiTugas.append(int(input("Nilai Tugas: ")))
        nilaiUTS.append(int(input("Nilai UTS: ")))
        nilaiUAS.append(int(input("Nilai UAS: ")))

        nilaiAkhir.append(
            nilaiTugas[-1] * 30 / 100 + nilaiUTS[-1] * 35 / 100 + nilaiUAS[-1] * 35 / 100
        )

        print()
        _tanya = input("Tambah data ? [y/t]: ")
        print()
        if _tanya.lower() == "t":
            break

    # Output
    print("+----+-----------------------+--------+--------+-------+-------+---------+")
    print(
        "| {0:^2} | {1:^19} | {2:^8} | {3:^6} | {4:^5} | {5:^5} | {6:^7} |".format(
           "No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"
        )
    )
    print("-----+-----------------------+--------+--------+-------+-------+---------+")

    for no, (nama_val, nim_val, tugas_val, uts_val, uas_val, nilai_akhir_val) in enumerate(
        zip(nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir), start=1
    ):
        print(
            "| {0:>2} | {1:<19} | {2:>8} | {3:>6} | {4:>5} | {5:>5} | {6:>7} |".format(
                no, nama_val, nim_val, tugas_val, uts_val, uas_val, nilai_akhir_val
            )
        )

    print("+----+-----------------------+--------+--------+-------+-------+---------+")

kode diatas menggunakan ***separate structure*** atau ***[]*** agar lebih mudah menempatkan ***value***.
***append*** berfungsi untuk menambahkan data ke list yang sudah ada.

## Documentation
All associated resources. are licensed under the [MIT License](https://mit-license.org/).

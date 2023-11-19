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

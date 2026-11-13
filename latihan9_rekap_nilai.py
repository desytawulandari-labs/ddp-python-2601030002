jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa : "))

while jumlah_mahasiswa <= 0:
    print("Jumlah mahasiswa harus lebih dari 0.")
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa : "))

total_nilai = 0
jumlah_lulus = 0

nilai_tertinggi = None
nilai_terendah = None

for i in range(1, jumlah_mahasiswa + 1):
    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i} : "))

    while nilai < 0 or nilai > 100:
        print("Nilai harus berada pada rentang 0 sampai 100.")
        nilai = float(input(f"Masukkan ulang nilai mahasiswa ke-{i}: "))

    total_nilai += nilai

    if nilai >= 60:
        jumlah_lulus += 1

    if i == 1:
        nilai_tertinggi = nilai
        nilai_terendah = nilai
    else:
        if nilai > nilai_tertinggi:
            nilai_tertinggi = nilai

        if nilai < nilai_terendah:
            nilai_terendah = nilai

rata_rata = total_nilai / jumlah_mahasiswa

print("Nilai tertinggi :", nilai_tertinggi)
print("Nilai terendah :", nilai_terendah)
print(f"Rata-rata : {rata_rata:.2f}")
print("Jumlah mahasiswa yang lulus :", jumlah_lulus)
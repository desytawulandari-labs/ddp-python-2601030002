n = int(input("Masukkan bilangan n : "))

jumlah = 0

print("Output:", end=" ")

for angka in range(5, n + 1, 5):
    print(angka, end=" ")
    jumlah += angka

print()
print("Jumlah:", jumlah)


# TRACE TABLE (n = 20)
# -----------------------------------------------------
# | Iterasi | Angka | Jumlah Sebelum | Jumlah Sesudah |
# |---------|-------|----------------|----------------|
# |    1    |   5   |       0        |       5        |
# |    2    |   10  |       5        |       15       |
# |    3    |   15  |       15       |       30       |
# |    4    |   20  |       30       |       50       |
# -----------------------------------------------------
# Output akhir: Jumlah = 50
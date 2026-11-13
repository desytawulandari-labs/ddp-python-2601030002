angka_rahasia = 31
jumlah_tebakan = 0

print("Tebak angka dari 1 sampai 50!")

tebakan = int(input("Masukkan tebakan : "))

while tebakan != angka_rahasia:
    jumlah_tebakan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")

    tebakan = int(input("Coba lagi : "))

jumlah_tebakan += 1
print("Benar! Angka rahasianya adalah", angka_rahasia)
print("Jumlah tebakan :", jumlah_tebakan)
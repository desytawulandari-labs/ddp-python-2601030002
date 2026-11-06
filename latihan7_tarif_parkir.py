lama_parkir = int(input("Masukkan lama parkir (jam) : "))
langganan = input("Memiliki kartu langganan? (y/n) : ")

if langganan.lower() == "y":
    biaya = 0 
elif lama_parkir <= 0:
    biaya = 0
elif lama_parkir <= 2:
    biaya = 2000
else:
    biaya = 2000 + (lama_parkir - 2) * 1000

print("Biaya parkir : Rp.", biaya) 
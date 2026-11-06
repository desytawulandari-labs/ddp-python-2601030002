nilai = int(input("Masukkan nilai(0-100) : "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 80:
    print("Huruf A, LULUS")
elif nilai >= 70:
    print("Huruf B, LULUS")
elif nilai >= 60:
    print("Huruf C, LULUS")
else :
    print("Huruf D, TIDAK LULUS")


#TRACE TABLE


# TRACE TABLE
# -------------------------------------------------------------------
# | Nilai | < 0 atau > 100 | >= 80 | >= 70 | >= 60 |    Hasil       |
# |-------|----------------|-------|-------|-------|----------------|
# | 80    | False          | True  | -     | -     | A, LULUS       |
# | 79    | False          | False | True  | -     | B, LULUS       |
# | 60    | False          | False | False | True  | C, LULUS       |
# | 59    | False          | False | False | False | D, TIDAK LULUS |
# | 105   | True           | -     | -     | -     | Tidak valid    |



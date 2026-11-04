nama_barang = input("Masukkan nama barang : ")
harga_satuan = float(input("Masukkan harga satuan : "))
jumlah_barang = int(input("Masukkan jumlah barang : "))

subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_bayar = subtotal + ppn

print(f"=== RINCIAN BELANJA ===")
print(f"Nama barang : {nama_barang}")
print(f"Subtotal : {subtotal}")
print(f"PPN 11% : {ppn}")
print(f"Total bayar : {total_bayar}")
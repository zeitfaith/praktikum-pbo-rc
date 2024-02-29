# Membuka file Me.txt dalam mode menulis ('w')
with open("Me.txt", "w") as file:
    # Menulis data ke file
    file.write("Nama : Muhammad Fatih Hanbali S.Kom Al-Hafidz\n")
    file.write("NIM : 122140112\n")
    file.write("Resolusi Saya di Tahun ini : kuliah lancar jaya\n")

print("File Me.txt berhasil dibuat dan diisi dengan data.")

# Masukkan tinggi segitiga
tinggi = int(input("Masukkan tinggi segitiga: "))

# Iterasi melalui setiap baris segitiga
for i in range(1, tinggi + 1):
    # Cetak spasi untuk penjajaran kiri
    print(" " * (tinggi - i), end="")
    
    # Cetak '*' secara bertambah untuk setiap baris
    print('* ' * i)
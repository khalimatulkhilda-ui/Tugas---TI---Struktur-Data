def hitung_pergeseran(n, posisi):
    """
    Menghitung jumlah operasi pergeseran saat menghapus elemen di posisi tertentu.
    """
    if posisi == 0:
        # Menghapus elemen pertama
        return n - 1
    elif posisi == n - 1:
        # Menghapus elemen terakhir
        return 0
    else:
        # Untuk posisi lain, bisa dihitung sebagai jarak dari ujung
        return abs(n - 1 - posisi)

# Contoh perhitungan:
n = int(input("Masukkan jumlah elemen array: "))

# Menghapus elemen pertama
operasi_pertama = hitung_pergeseran(n, 0)
print(f"Jumlah operasi saat menghapus elemen pertama: {operasi_pertama}")

# Menghapus elemen terakhir
operasi_terakhir = hitung_pergeseran(n, n - 1)
print(f"Jumlah operasi saat menghapus elemen terakhir: {operasi_terakhir}")
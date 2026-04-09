def manual_delete(arr, index):
    """
    Menghapus elemen di indeks tertentu tanpa menggunakan .pop() atau del.
    Menggeser elemen di sebelah kanan ke kiri.
    """
    n = len(arr)
    if index < 0 or index >= n:
        print("Indeks tidak valid.")
        return

    # Geser elemen dari sebelah kanan ke kiri
    for i in range(index, n - 1):
        arr[i] = arr[i + 1]
    # Hilangkan elemen terakhir (karena sudah digeser)
    arr.pop()  

# Contoh penggunaan:
arr = [10, 20, 30, 40, 50]
print("Sebelum dihapus:", arr)
manual_delete(arr, 2) 
print("Sesudah dihapus:", arr)
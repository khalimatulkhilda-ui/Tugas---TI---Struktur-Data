import time
import random

# Fungsi A: Menggunakan nested loop untuk mencari duplikat
def find_duplicates_nested(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                if data[i] not in duplicates:
                    duplicates.append(data[i])
                break  # Jika sudah ditemukan duplikat, lanjut ke elemen berikutnya
    return duplicates

# Fungsi B: Menggunakan set untuk mencari duplikat
def find_duplicates_set(data):
    seen = set()
    duplicates = set()
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def test_performance(n):
    data = [random.randint(1, n//2) for _ in range(n)]
    
    # Pengukuran waktu Fungsi A
    start = time.time()
    find_duplicates_nested(data)
    end = time.time()
    time_a = end - start

    # Pengukuran waktu Fungsi B
    start = time.time()
    find_duplicates_set(data)
    end = time.time()
    time_b = end - start

    return time_a, time_b

sizes = [100, 1000, 10000]

for size in sizes:
    t_a, t_b = test_performance(size)
    print(f"n = {size}")
    print(f"Fungsi A (Nested Loop): {t_a:.6f} detik")
    print(f"Fungsi B (Set):         {t_b:.6f} detik")
    print("-" * 40)
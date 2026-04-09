def reverse_string(s):
    """
    Membalikkan string tanpa menggunakan slicing [::-1] atau .reverse()
    """
    reversed_str = ""
    n = len(s)
    for i in range(n - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

# Contoh penggunaan:
kalimat = "Halo Dunia"
print("Kalimat asli:", kalimat)
print("Kalimat dibalik:", reverse_string(kalimat))
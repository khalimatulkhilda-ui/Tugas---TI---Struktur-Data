a = [1, 2, 3]
b = a.copy()  # membuat salinan baru

print("Sebelum perubahan:")
print("a =", a)
print("b =", b)

a[0] = 100

print("\nSetelah a diubah:")
print("a =", a)
print("b =", b)
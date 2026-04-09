import sys

# Mendefinisikan sebuah bilangan bulat
integer_value = 42

# Mendefinisikan sebuah list berisi satu bilangan bulat
list_value = [42]

# Mendapatkan alamat memori menggunakan id()
address_integer = id(integer_value)
address_list = id(list_value)

# Mendapatkan ukuran memori menggunakan sys.getsizeof()
size_integer = sys.getsizeof(integer_value)
size_list = sys.getsizeof(list_value)

# Menampilkan informasi tentang integer
print("=== INTEGER ===")
print(f"Value           : {integer_value}")
print(f"Memory Address  : {address_integer}")
print(f"Memory Size     : {size_integer} bytes")

# Menampilkan informasi tentang list
print("\n=== LIST ===")
print(f"Value           : {list_value}")
print(f"Memory Address  : {address_list}")
print(f"Memory Size     : {size_list} bytes")

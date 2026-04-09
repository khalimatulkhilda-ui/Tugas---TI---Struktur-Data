import sys

# Define a simple integer
integer_value = 42

# Define a list containing one integer
list_value = [42]

# Get memory address using id()
address_integer = id(integer_value)
address_list = id(list_value)

# Get memory size using sys.getsizeof()
size_integer = sys.getsizeof(integer_value)
size_list = sys.getsizeof(list_value)

print("=== INTEGER ===")
print(f"Value           : {integer_value}")
print(f"Memory Address  : {address_integer}")
print(f"Memory Size     : {size_integer} bytes")

print("\n=== LIST ===")
print(f"Value           : {list_value}")
print(f"Memory Address  : {address_list}")
print(f"Memory Size     : {size_list} bytes")
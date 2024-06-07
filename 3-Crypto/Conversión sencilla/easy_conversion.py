# from const import flag
from pathlib import Path


def bytes_to_integer(x: bytes) -> int:
    x = int.from_bytes(x, byteorder="big")
    return x


# print(bytes_to_integer(flag))


## Solución
def integer_to_bytes(x: int) -> bytes:
    # Calcular el número de bytes necesarios
    num_bytes: int = (x.bit_length() + 7) // 8
    return x.to_bytes(num_bytes, byteorder="big")


# Leer el número entero del archivo
integer_value = int(Path("output.txt").read_text().strip())

# Convertirlo de vuelta a bytes
original_bytes = integer_to_bytes(integer_value)

print(original_bytes.decode())

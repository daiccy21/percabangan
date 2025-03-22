def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Masukkan nilai n: "))

for i in range(n - 1, 1, -1):
    if is_prime(i):
        print(f"Bilangan prima terdekat < {n} adalah {i}")
        break
else:
    print(f"Tidak ada bilangan prima yang lebih kecil dari {n}")
    
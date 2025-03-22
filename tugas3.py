tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

for i in range(tinggi):
    for j in range(lebar):
        print(i * lebar + j + 1, end=' ')
    print()
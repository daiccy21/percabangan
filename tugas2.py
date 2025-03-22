def tampilkan_deret(n):
    for i in range(n, 0, -1):
        faktorial = 1
        for j in range(1, i + 1):
            faktorial *= j
        deret = ' '.join(str(k) for k in range(i, 0, -1))
        print(faktorial, deret)
        
n = int(input("Masukkan nilai n: "))
tampilkan_deret(n)

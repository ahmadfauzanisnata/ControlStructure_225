#program untuk menanyakan nilai siswa
SiswaMendapatNilai = float (input("Nilai kamu berapa"))

if SiswaMendapatNilai >=90:
    print(" Excellent performance")
elif SiswaMendapatNilai >=80:
    print(" Very Good performance")
elif SiswaMendapatNilai >=70:
    print(" then Good performance")
elif SiswaMendapatNilai >=60:
    print(" then average performance")
else:
    print("kurang bagus")
    

#NOMOR 2
# Program untuk mencari bilangan terbesar dari tiga bilangan

def CariBilanganTerbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Contoh penggunaan
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))
bilangan3 = float(input("Masukkan bilangan ketiga: "))

terbesar = CariBilanganTerbesar(bilangan1, bilangan2, bilangan3)
print(f"Bilangan terbesar adalah: {terbesar}")

#NOMOR 3
def CetakFibonacci(n):
    a, b =0, 1
    while a <= n:
        print(a, end= " ")
        a, b = b, a + b
n = int(input("Masukkan nilai n: "))
print(f"Deret Fibonacci hingga {n}:")
CetakFibonacci(n)

#NOMOR 4
def CetakBilanganGanjil(n):
   for i in range(1, n+1):
        if i % 2 != 0:  # Cek apakah bilangan ganjil
            print(i, end=" ")  # Cetak bilangan ganji
       
n = int(input("Masukkan nilai n: "))
print(f"Bilangan ganjil hingga  {n}:")
CetakBilanganGanjil(n)

#NOMOR 5
# Program untuk menghasilkan pola angka sesuai input n
def cetak_pola(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")  # Cetak angka i sebanyak i kali
        print()  # Pindah baris setelah mencetak satu baris angka

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))
cetak_pola(n)





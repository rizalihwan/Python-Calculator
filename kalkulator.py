a = int(input("MASUKAN ANGKA PERTAMA : "))
b = int(input("MASUKAN ANGKA KEDUA   : "))
print("1.Pertambahan")
print("2.Perkalian")
print("3.Pengurangan")
print("4.Pembagian")
print("5.Modulus")
c = input("Masukan Operator : ")

def tambah(x, y):
    total = x + y
    return total

def kurang(x, y):
    total = x - y
    return total

def kali(x, y):
    total = x * y
    return total

def bagi(x, y):
    total = x / y
    return total

def mod(x, y):
    total = x % y
    return total

if c == "1":
    print(tambah(a, b))
    if c == "2":
        print(kurang(a, b))
    if c == "3":
        print(kali(a, b))
    if c == "4":
        print(bagi(a, b))
    if c == "5":
        print(mod(a, b))

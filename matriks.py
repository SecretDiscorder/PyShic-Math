import numpy as np

print('ordo axb')
input_a = int(input("masukan  matriks ordo a: "))
input_b = int(input("masukan 1 matriks ordo b: "))
input_a2 = int(input("masukan  matriks ordo a: "))
input_b2 = int(input("masukan 1 matriks ordo b: "))

matriks_a_2 = []
for i in range(input_a2):
    baris_a_2 = []
    for j in range(input_b2):
        elemen_a = int(input(f"masukan elemen a[{i+1}][{j+1}]: "))
        baris_a_2.append(elemen_a)
    matriks_a_2.append(baris_a_2)

matriks_b_2 = []
for i in range(input_a2):
    baris_b_2 = []
    for j in range(input_b2):
        elemen_b = int(input(f"masukan elemen b[{i+1}][{j+1}]: "))
        baris_b_2.append(elemen_b)
    matriks_b_2.append(baris_b_2)

print("\nMatriks 2 a:")
for baris_a_2 in matriks_a_2:
    print(baris_a_2)

print("\nMatriks 2 b:")
for baris_b_2 in matriks_b_2:
    print(baris_b_2)

matriks_a = []
for i in range(input_a):
    baris_a = []
    for j in range(input_b):
        elemen_a = int(input(f"masukan elemen a[{i+1}][{j+1}]: "))
        baris_a.append(elemen_a)
    matriks_a.append(baris_a)

matriks_b = []
for i in range(input_a):
    baris_b = []
    for j in range(input_b):
        elemen_b = int(input(f"masukan elemen b[{i+1}][{j+1}]: "))
        baris_b.append(elemen_b)
    matriks_b.append(baris_b)

print("\nMatriks 1 a:")
for baris_a in matriks_a:
    print(baris_a)

print("\nMatriks 1 b:")
for baris_b in matriks_b:
    print(baris_b)

arr = np.array(matriks_a)
arr2 = np.array(matriks_b)
sumi = np.add(arr, arr2)
print('\nPenjumlahan:')
print(sumi)

subtra = np.subtract(arr, arr2)
print('\nPengurangan:')
print(subtra)

multi = np.multiply(arr, arr2)
print('\nPerkalian:')
print(multi)

trans = np.transpose(arr)
print('\nTranspose matriks 1 a:')
print(trans)

trans2 = np.transpose(arr2)
print('\nTranspose matriks 1 b:')
print(trans2)

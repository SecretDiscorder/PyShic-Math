import math

def aritmatika(a, r, n):
    # a adalah suku pertama, r adalah beda, n adalah jumlah suku
    barisan = [a + (i * r) for i in range(n)]
    return barisan

a = int(input("Masukkan suku pertama: "))
r = int(input("Masukkan beda: "))
n = int(input("Masukkan jumlah suku: "))

hasil_aritmatika = aritmatika(a, r, n)
print("Barisan Aritmatika:", hasil_aritmatika)


def geometri(a, r, n):
    # a adalah suku pertama, r adalah rasio, n adalah jumlah suku
    barisan = [a * (r ** i) for i in range(n)]
    return barisan

a = int(input("Masukkan suku pertama: "))
r = int(input("Masukkan rasio: "))
n = int(input("Masukkan jumlah suku: "))

hasil_geometri = geometri(a, r, n)
print("Barisan Geometri:", hasil_geometri)

if __name__ == "__main__":
	aritmatika = aritmatika()
	geometri = geometri()
	while True:
		print(aritmatika)
		print(geometri)

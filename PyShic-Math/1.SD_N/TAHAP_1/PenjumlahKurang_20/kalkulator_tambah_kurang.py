def hitung_hasil(input_string):
    hasil = 0
    operator = '+'
    bilangan = ''
    
    for char in input_string:
        if char.isdigit():
            bilangan += char
        elif char == '+':
            if bilangan:
                if operator == '+':
                    hasil += int(bilangan)
                else:
                    hasil -= int(bilangan)
            operator = '+'
            bilangan = ''
        elif char == '-':
            if bilangan:
                if operator == '+':
                    hasil += int(bilangan)
                else:
                    hasil -= int(bilangan)
            operator = '-'
            bilangan = ''

    if bilangan:
        if operator == '+':
            hasil += int(bilangan)
        else:
            hasil -= int(bilangan)

    return hasil

def main():
    input_expression = input("Masukkan kombinasi penjumlahan dan pengurangan bilangan: ")
    try:
        hasil = hitung_hasil(input_expression)
        print("Hasil dari input adalah:", hasil)
    except ValueError:
        print("Input tidak valid. Pastikan format input benar.")

if __name__ == "__main__":
    main()

while True:
    main()
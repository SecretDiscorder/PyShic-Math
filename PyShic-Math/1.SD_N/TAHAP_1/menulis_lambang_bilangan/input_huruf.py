def convert_to_numeric(value):
    try:
        return int(value)
    except ValueError:
        return 0
def konversi_lambang_bilangan(nama_huruf):
    angka_huruf = {
        'nol': '0',
        'satu': '1',
        'dua': '2',
        'tiga': '3',
        'empat': '4',
        'lima': '5',
        'enam': '6',
        'tujuh': '7',
        'delapan': '8',
        'sembilan': '9',
        'sepuluh': '10',
        'sebelas': '11',
        'duabelas': '12',
        'tigabelas': '13',
        'empatbelas': '14',
        'limabelas': '15',
        'enambelas': '16',
        'tujuhbelas': '17',
        'delapanbelas': '18',
        'sembilanbelas': '19',
        'dua puluh': '20',
        'tiga puluh': '30',
        'empat puluh': '40',
        'lima puluh': '50',
        'enam puluh': '60',
        'tujuh puluh': '70',
        'delapan puluh': '80',
        'sembilan puluh': '90',
        'seratus': '100',
        'dua ratus': '200',
        'tiga ratus': '300',
        'empat ratus': '400',
        'lima ratus': '500',
        'enam ratus': '600',
        'tujuh ratus': '700',
        'delapan ratus': '800',
        'sembilan ratus': '900',
        'seribu': '1000',
        'dua ribu': '2000',
        'tiga ribu': '3000',
        'empat ribu': '4000',
        'lima ribu': '5000',
        'enam ribu': '6000',
        'tujuh ribu': '7000',
        'delapan ribu': '8000',
        'sembilan ribu': '9000',
        'sepuluh ribu': '10000',
        'sebelas ribu': '11000',
        'dua belas ribu': '12000',
        'tiga belas ribu': '13000',
        'empat belas ribu': '14000',
        'lima belas ribu': '15000',
        'enam belas ribu': '16000',
        'tujuh belas ribu': '17000',
        'delapan belas ribu': '18000',
        'sembilan belas ribu': '19000',
        'dua puluh ribu': '20000',
        'tiga puluh ribu': '30000',
        'empat puluh ribu': '40000',
        'lima puluh ribu': '50000',
        'enam puluh ribu': '60000',
        'tujuh puluh ribu': '70000',
        'delapan puluh ribu': '80000',
        'sembilan puluh ribu': '90000',
        'seratus ribu': '100000',
        'seratus satu ribu': '101000',
        'seratus dua ribu': '102000',
        'seratus tiga ribu': '103000',
        'seratus empat ribu': '104000',
        'seratus lima ribu': '105000',
        'seratus enam ribu': '106000',
        'seratus tujuh ribu': '107000',
        'seratus delapan ribu': '108000',
        'seratus sembilan ribu': '109000',
        'seratus sepuluh ribu': '110000',
        'seratus sebelas ribu': '111000',
        'seratus dua belas ribu': '112000',
        'seratus tiga belas ribu': '113000',
        'seratus empat belas ribu': '114000',
        'seratus lima belas ribu': '115000',
        'seratus enam belas ribu': '116000',
        'seratus tujuh belas ribu': '117000',
        'seratus delapan belas ribu': '118000',
        'seratus sembilan belas ribu': '119000',
        'seratus dua puluh ribu': '120000',
        'seratus dua puluh satu ribu': '121000',
        'seratus dua puluh dua ribu': '122000',
        'seratus dua puluh tiga ribu': '123000',
        'seratus dua puluh empat ribu': '124000',
        'seratus dua puluh lima ribu': '125000',
        'seratus dua puluh enam ribu': '126000',
        'seratus dua puluh tujuh ribu': '127000',
        'seratus dua puluh delapan ribu': '128000',
        'seratus dua puluh sembilan ribu': '129000',
        'seratus tiga puluh ribu': '130000',
        'seratus tiga puluh satu ribu': '131000',
        'seratus tiga puluh dua ribu': '132000',
        'seratus tiga puluh tiga ribu': '133000',
        'seratus tiga puluh empat ribu': '134000',
        'seratus tiga puluh lima ribu': '135000',
        'seratus tiga puluh enam ribu': '136000',
        'seratus tiga puluh tujuh ribu': '137000',
        'seratus tiga puluh delapan ribu': '138000',
        'seratus tiga puluh sembilan ribu': '139000',
        'seratus empat puluh ribu': '140000',
        'seratus empat puluh satu ribu': '141000',
        'seratus empat puluh dua ribu': '142000',
        'seratus empat puluh tiga ribu': '143000',
        'seratus empat puluh empat ribu': '144000',
        'seratus empat puluh lima ribu': '145000',
        'seratus empat puluh enam ribu': '146000',
        'seratus empat puluh tujuh ribu': '147000',
        'seratus empat puluh delapan ribu': '148000',
        'seratus empat puluh sembilan ribu': '149000',
        'seratus lima puluh ribu': '150000',
        'seratus lima puluh satu ribu': '151000',
        'seratus lima puluh dua ribu': '152000',
        'seratus lima puluh tiga ribu': '153000',
        'seratus lima puluh empat ribu': '154000',
        'seratus lima puluh lima ribu': '155000',
        'seratus lima puluh enam ribu': '156000',
        'seratus lima puluh tujuh ribu': '157000',
        'seratus lima puluh delapan ribu': '158000',
        'seratus lima puluh sembilan ribu': '159000',
        'seratus enam puluh ribu': '160000',
        'seratus enam puluh satu ribu': '161000',
        'seratus enam puluh dua ribu': '162000',
        'seratus enam puluh tiga ribu': '163000',
        'seratus enam puluh empat ribu': '164000',
        'seratus enam puluh lima ribu': '165000',
        'seratus enam puluh enam ribu': '166000',
        'seratus enam puluh tujuh ribu': '167000',
        'seratus enam puluh delapan ribu': '168000',
        'seratus enam puluh sembilan ribu': '169000',
        'seratus tujuh puluh ribu': '170000',
        'seratus tujuh puluh satu ribu': '171000',
        'seratus tujuh puluh dua ribu': '172000',
        'seratus tujuh puluh tiga ribu': '173000',
        'seratus tujuh puluh empat ribu': '174000',
        'seratus tujuh puluh lima ribu': '175000',
        'seratus tujuh puluh enam ribu': '176000',
        'seratus tujuh puluh tujuh ribu': '177000',
        'seratus tujuh puluh delapan ribu': '178000',
        'seratus tujuh puluh sembilan ribu': '179000',
        'seratus delapan puluh ribu': '180000',
        'seratus delapan puluh satu ribu': '181000',
        'seratus delapan puluh dua ribu': '182000',
        'seratus delapan puluh tiga ribu': '183000',
        'seratus delapan puluh empat ribu': '184000',
        'seratus delapan puluh lima ribu': '185000',
        'seratus delapan puluh enam ribu': '186000',
        'seratus delapan puluh tujuh ribu': '187000',
        'seratus delapan puluh delapan ribu': '188000',
        'seratus delapan puluh sembilan ribu': '189000',
        'seratus sembilan puluh ribu': '190000',
        'seratus sembilan puluh ribu': '190000',
        'seratus sembilan puluh satu ribu': '191000',
        'seratus sembilan puluh dua ribu': '192000',
        'seratus sembilan puluh tiga ribu': '193000',
        'seratus sembilan puluh empat ribu': '194000',
        'seratus sembilan puluh lima ribu': '195000',
        'seratus sembilan puluh enam ribu': '196000',
        'seratus sembilan puluh tujuh ribu': '197000',
        'seratus sembilan puluh delapan ribu': '198000',
        'seratus sembilan puluh sembilan ribu': '199000',
        'dua ratus ribu': '200000',
        'dua ratus satu ribu': '201000',
        'dua ratus dua ribu': '202000',
        'dua ratus tiga ribu': '203000',
        'dua ratus empat ribu': '204000',
        'dua ratus lima ribu': '205000',
        'dua ratus enam ribu': '206000',
        'dua ratus tujuh ribu': '207000',
        'dua ratus delapan ribu': '208000',
        'dua ratus sembilan ribu': '209000',
        'tiga ratus ribu': '300000',
        'tiga ratus satu ribu': '301000',
        'tiga ratus dua ribu': '302000',
        'tiga ratus tiga ribu': '303000',
        'tiga ratus empat ribu': '304000',
        'tiga ratus lima ribu': '305000',
        'tiga ratus enam ribu': '306000',
        'tiga ratus tujuh ribu': '307000',
        'tiga ratus delapan ribu': '308000',
        'tiga ratus sembilan ribu': '309000',
        'empat ratus ribu': '400000',
        'lima ratus ribu': '500000',
        'lima ratus satu ribu': '501000',
        'lima ratus dua ribu': '502000',
        'lima ratus tiga ribu': '503000',
        'lima ratus empat ribu': '504000',
        'lima ratus lima ribu': '505000',
        'lima ratus enam ribu': '506000',
        'lima ratus tujuh ribu': '507000',
        'lima ratus delapan ribu': '508000',
        'lima ratus sembilan ribu': '509000',
        'empat ratus puluh ribu': '410000',
        'empat ratus satu puluh ribu': '411000',
        'empat ratus dua puluh ribu': '412000',
        'empat ratus tiga puluh ribu': '413000',
        'empat ratus empat puluh ribu': '414000',
        'empat ratus lima puluh ribu': '415000',
        'empat ratus enam puluh ribu': '416000',
        'empat ratus tujuh puluh ribu': '417000',
        'empat ratus delapan puluh ribu': '418000',
        'empat ratus sembilan puluh ribu': '419000',
        'lima ratus puluh ribu': '510000',
        'lima ratus satu puluh ribu': '511000',
        'lima ratus dua puluh ribu': '512000',
        'lima ratus tiga puluh ribu': '513000',
        'lima ratus empat puluh ribu': '514000',
        'lima ratus lima puluh ribu': '515000',
        'lima ratus enam puluh ribu': '516000',
        'lima ratus tujuh puluh ribu': '517000',
        'lima ratus delapan puluh ribu': '518000',
        'lima ratus sembilan puluh ribu': '519000',
        'enam ratus ribu': '600000',
        'enam ratus satu ribu': '601000',
        'enam ratus dua ribu': '602000',
        'enam ratus tiga ribu': '603000',
        'enam ratus empat ribu': '604000',
        'enam ratus lima ribu': '605000',
        'enam ratus enam ribu': '606000',
        'enam ratus tujuh ribu': '607000',
        'enam ratus delapan ribu': '608000',
        'enam ratus sembilan ribu': '609000',
        'enam ratus sepuluh ribu': '610000',
        'enam ratus sebelas ribu': '611000',
        'enam ratus dua belas ribu': '612000',
        'enam ratus tiga belas ribu': '613000',
        'enam ratus empat belas ribu': '614000',
        'enam ratus lima belas ribu': '615000',
        'enam ratus enam belas ribu': '616000',
        'enam ratus tujuh belas ribu': '617000',
        'enam ratus delapan belas ribu': '618000',
        'enam ratus sembilan belas ribu': '619000',
        'tujuh ratus ribu': '700000',
        'tujuh ratus satu ribu': '701000',
        'tujuh ratus dua ribu': '702000',
        'tujuh ratus tiga ribu': '703000',
        'tujuh ratus empat ribu': '704000',
        'tujuh ratus lima ribu': '705000',
        'tujuh ratus enam ribu': '706000',
        'tujuh ratus tujuh ribu': '707000',
        'tujuh ratus delapan ribu': '708000',
        'tujuh ratus sembilan ribu': '709000',
        'tujuh ratus sepuluh ribu': '710000',
        'tujuh ratus sebelas ribu': '711000',
        'tujuh ratus dua belas ribu': '712000',
        'tujuh ratus tiga belas ribu': '713000',
        'tujuh ratus empat belas ribu': '714000',
        'tujuh ratus lima belas ribu': '715000',
        'tujuh ratus enam belas ribu': '716000',
        'tujuh ratus tujuh belas ribu': '717000',
        'tujuh ratus delapan belas ribu': '718000',
        'tujuh ratus sembilan belas ribu': '719000',
        # ... Kamus angka_huruf sebelumnya ...
        'delapan ratus ribu': '800000',
        'delapan ratus satu ribu': '801000',
        'delapan ratus dua ribu': '802000',
        'delapan ratus tiga ribu': '803000',
        'delapan ratus empat ribu': '804000',
        'delapan ratus lima ribu': '805000',
        'delapan ratus enam ribu': '806000',
        'delapan ratus tujuh ribu': '807000',
        'delapan ratus delapan ribu': '808000',
        'delapan ratus sembilan ribu': '809000',
        'delapan ratus sepuluh ribu': '810000',
        'delapan ratus sebelas ribu': '811000',
        'delapan ratus dua belas ribu': '812000',
        'delapan ratus tiga belas ribu': '813000',
        'delapan ratus empat belas ribu': '814000',
        'delapan ratus lima belas ribu': '815000',
        'delapan ratus enam belas ribu': '816000',
        'delapan ratus tujuh belas ribu': '817000',
        'delapan ratus delapan belas ribu': '818000',
        'delapan ratus sembilan belas ribu': '819000',
        # ... Kamus angka_huruf sebelumnya ...
        'sembilan ratus ribu': '900000',
        'sembilan ratus satu ribu': '901000',
        'sembilan ratus dua ribu': '902000',
        'sembilan ratus tiga ribu': '903000',
        'sembilan ratus empat ribu': '904000',
        'sembilan ratus lima ribu': '905000',
        'sembilan ratus enam ribu': '906000',
        'sembilan ratus tujuh ribu': '907000',
        'sembilan ratus delapan ribu': '908000',
        'sembilan ratus sembilan ribu': '909000',
        'sembilan ratus sepuluh ribu': '910000',
        'sembilan ratus sebelas ribu': '911000',
        'sembilan ratus dua belas ribu': '912000',
        'sembilan ratus tiga belas ribu': '913000',
        'sembilan ratus empat belas ribu': '914000',
        'sembilan ratus lima belas ribu': '915000',
        'sembilan ratus enam belas ribu': '916000',
        'sembilan ratus tujuh belas ribu': '917000',
        'sembilan ratus delapan belas ribu': '918000',
        'sembilan ratus sembilan belas ribu': '919000',
        'sembilan ratus dua puluh ribu': '920000',
        'puluh': '',
        'ratus': '00',
        'juta': '000000',
        'miliar': '000000000',
        'triliun': '000000000000',
        'kuadriliun': '000000000000000',
        'kuantiliun': '000000000000000000',
        # dan seterusnya...
    }
    if nama_huruf.isnumeric():
        angka = int(nama_huruf)
        huruf_parts = []
        for num in sorted(angka_huruf.items(), key=lambda x: convert_to_numeric(x[1]), reverse=True):
            num_value = convert_to_numeric(num[1])
            if num_value == 0:
                continue
            while angka >= num_value:
                angka -= num_value
                huruf_parts.append(num[0])
        
        huruf = ' '.join(huruf_parts)
        return huruf.strip()

    else:
        kata_kunci = nama_huruf.lower().split()
        angka = 0
        temp = 0
        for kata in kata_kunci:
            if kata == 'puluh':
                temp *= 10
                angka += temp
                temp = 0
            elif kata == 'ratus':
                temp *= 100
                angka += temp
                temp = 0
            elif kata == 'ribu':
                temp *= 1000
                angka += temp
                temp = 0
            elif kata == 'juta':
                temp *= 1000000
                angka += temp
                temp = 0
            elif kata == 'miliar':
                temp *= 1000000000
                angka += temp
                temp = 0
            elif kata == 'triliun':
                temp *= 1000000000000
                angka += temp
                temp = 0
            elif kata in angka_huruf:
                num = int(angka_huruf[kata])
                if num >= 1000000000000000:
                    angka += temp * num
                    temp = 0
                else:
                    temp += num
        angka += temp
        return str(angka)
def main():
    while True:
        input_angka_huruf = input("Masukkan bilangan atau nama huruf sampai seribu saja (ketik 'selesai' untuk keluar): ")
        if input_angka_huruf.lower() == 'selesai':
            break
        output = konversi_lambang_bilangan(input_angka_huruf)
        if input_angka_huruf.isnumeric():
            print(f"Hasil konversi dari '{input_angka_huruf}' adalah: {output}")
        else:
            print(f"Lambang bilangan untuk '{input_angka_huruf}' adalah: {output}")

if __name__ == "__main__":
    main()

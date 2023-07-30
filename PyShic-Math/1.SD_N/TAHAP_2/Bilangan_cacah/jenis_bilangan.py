def nilai_tempat_ratusan_puluhan_satuan(bilangan):
    ratusan = bilangan // 100
    sisa_ratusan = bilangan % 100
    puluhan = sisa_ratusan // 10
    satuan = sisa_ratusan % 10
    return ratusan, puluhan, satuan

def main_nilai_tempat_ratusan_puluhan_satuan():
    print("Nilai Tempat Ratusan, Puluhan, dan Satuan")
    bilangan = int(input("Masukkan bilangan: "))
    ratusan, puluhan, satuan = nilai_tempat_ratusan_puluhan_satuan(bilangan)
    print(f"Ratusan: {ratusan}")
    print(f"Puluhan: {puluhan}")
    print(f"Satuan: {satuan}")

if __name__ == "__main__":
    main_nilai_tempat_ratusan_puluhan_satuan()

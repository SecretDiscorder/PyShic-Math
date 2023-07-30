def konversi_meter_ke_cm_km(meter):
    centimeter = meter * 100
    kilometer = meter / 1000
    return centimeter, kilometer

def konversi_km_ke_mm(km):
    mm = km * 1000000
    return mm

def konversi_mm_ke_km(mm):
    km = mm / 1000000
    return km

def konversi_km_ke_hm(km):
    hm = km * 10
    return hm

def konversi_hm_ke_km(hm):
    km = hm / 10
    return km

def konversi_km_ke_dam(km):
    dam = km * 100
    return dam

def konversi_dam_ke_km(dam):
    km = dam / 100
    return km

def konversi_meter_ke_dm_cm_mm(meter):
    dm = meter * 10
    cm = meter * 100
    mm = meter * 1000
    return dm, cm, mm

def konversi_dm_cm_mm_ke_meter(dm, cm, mm):
    meter = dm / 10
    meter_cm = cm / 100
    meter_mm = mm / 1000
    return meter, meter_cm, meter_mm
def konversi_meter_ke_cm_km(meter):
    centimeter = meter * 100
    kilometer = meter / 1000
    return centimeter, kilometer

def konversi_km_ke_mm(km):
    mm = km * 1000000
    return mm

def konversi_mm_ke_km(mm):
    km = mm / 1000000
    return km

# ... (fungsi konversi lainnya)

def konversi_meter_ke_dam(meter):
    dam = meter / 10
    return dam

def konversi_dam_ke_meter(dam):
    meter = dam * 10
    return meter

# ... (fungsi konversi lainnya)

def konversi_cm_mm_ke_cm_m_dm(cm, mm):
    cm_m = cm // 100
    cm_dm = (cm // 10) % 10
    cm_mm = cm % 10
    dm = cm // 10
    m = cm // 100
    return cm_m, cm_dm, cm_mm, dm, m

def konversi_cm_m_dm_ke_cm(cm_m, cm_dm, cm_mm, dm, m):
    cm = (cm_m * 100) + (cm_dm * 10) + cm_mm
    cm = cm + (dm * 10) + (m * 100)
    mm = cm * 10
    return cm, mm

def konversi_meter_ke_dam(meter):
    dam = meter / 10
    return dam
def konversi_desimeter_ke_cm_mm(desimeter):
    cm = desimeter * 10
    mm = desimeter * 100
    return cm, mm

def konversi_cm_mm_ke_desimeter(cm, mm):
    desimeter = cm / 10
    desimeter_mm = mm / 100
    return desimeter, desimeter_mm
def konversi_dam_ke_meter(dam):
    meter = dam * 10
    return meter
def konversi_desimeter_ke_meter(desimeter):
    meter = desimeter / 10
    return meter

def konversi_desimeter_ke_cm_mm(desimeter):
    cm = desimeter * 10
    mm = desimeter * 100
    return cm, mm
def konversi_cm_ke_meter(cm):
    meter = cm / 100
    return meter

def konversi_cm_ke_desimeter(cm):
    desimeter = cm / 10
    return desimeter

def konversi_cm_ke_mm(cm):
    mm = cm * 10
    return mm

def konversi_mm_ke_meter(mm):
    meter = mm / 1000
    return meter

def konversi_mm_ke_desimeter(mm):
    desimeter = mm / 100
    return desimeter
def konversi_cm_ke_km(cm):
    km = cm / 100000
    return km

def konversi_cm_ke_hm(cm):
    hm = cm / 10000
    return hm

def konversi_cm_ke_dam(cm):
    dam = cm / 1000
    return dam

def konversi_cm_ke_meter(cm):
    meter = cm / 100
    return meter

def konversi_cm_ke_desimeter(cm):
    desimeter = cm / 10
    return desimeter

def konversi_cm_ke_mm(cm):
    mm = cm * 10
    return mm

def konversi_mm_ke_km(mm):
    km = mm / 1000000
    return km

def konversi_mm_ke_hm(mm):
    hm = mm / 100000
    return hm

def konversi_mm_ke_dam(mm):
    dam = mm / 10000
    return dam

def konversi_mm_ke_meter(mm):
    meter = mm / 1000
    return meter

def konversi_mm_ke_desimeter(mm):
    desimeter = mm / 100
    return desimeter

def konversi_mm_ke_cm(mm):
    cm = mm / 10
    return cm
def konversi_mm_ke_cm(mm):
    cm = mm / 10
    return cm
def konversi_cm_mm_ke_desimeter(cm, mm):
    desimeter = cm / 10
    desimeter_mm = mm / 100
    return desimeter, desimeter_mm
def main_konversi_panjang():
    print("Alat Konversi Panjang")
    print("1. Konversi Kilometer ke Kilometer, Hektometer, Dekameter, Meter, Desimeter, Sentimeter, dan Milimeter")
    print("2. Konversi Hektometer ke Kilometer, Hektometer, Dekameter, Meter, Desimeter, Sentimeter, dan Milimeter")
    print("3. Konversi Meter ke Kilometer, Hektometer, Dekameter, Meter, Desimeter, Sentimeter, dan Milimeter")
    print("4. Konversi Desimeter, Centimeter, dan Milimeter ke Meter")
    print("5. Konversi Dekameter ke Kilometer, Meter, Desimeter, Centimeter, dan Milimeter")
    print("6. Konversi Centimeter ke Meter, Desimeter, dan Milimeter")
    print("7. Konversi Milimeter ke Meter, Desimeter, dan Centimeter")
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6/7): "))

    if pilihan == 1:
        km = float(input("Masukkan jumlah kilometer: "))
        hm = km * 10
        dam = km * 100
        meter = km * 1000
        dm = km * 10000
        cm = km * 100000
        mm = km * 1000000
        print(f"{km} kilometer setara dengan {km} kilometer, {hm} hektometer, {dam} dekameter, {meter} meter, {dm} desimeter, {cm} sentimeter, dan {mm} milimeter.")

    elif pilihan == 2:
        hm = float(input("Masukkan jumlah hektometer: "))
        km = hm / 10
        dam = hm * 10
        meter = hm * 100
        dm = hm * 1000
        cm = hm * 10000
        mm = hm * 100000
        print(f"{hm} hektometer setara dengan {km} kilometer, {hm} hektometer, {dam} dekameter, {meter} meter, {dm} desimeter, {cm} sentimeter, dan {mm} milimeter.")

    elif pilihan == 3:
        meter = float(input("Masukkan jumlah meter: "))
        km = meter / 1000
        hm = meter / 100
        dam = meter / 10
        dm = meter * 10
        cm = meter * 100
        mm = meter * 1000
        print(f"{meter} meter setara dengan {km} kilometer, {hm} hektometer, {dam} dekameter, {meter} meter, {dm} desimeter, {cm} sentimeter, dan {mm} milimeter.")

    elif pilihan == 4:
        desimeter = float(input("Masukkan jumlah desimeter: "))
        cm, mm = konversi_desimeter_ke_cm_mm(desimeter)
        meter = konversi_desimeter_ke_meter(desimeter)
        dam = konversi_meter_ke_dam(meter)
        hm = konversi_meter_ke_hm(meter)
        km = konversi_meter_ke_km(meter)
        print(f"{desimeter} desimeter setara dengan {cm} centimeter dan {mm} milimeter.")
        print(f"{desimeter} desimeter setara dengan {meter} meter, {dam} dekameter, {hm} hektometer, dan {km} kilometer.")


    elif pilihan == 5:
        dam = float(input("Masukkan jumlah dekameter: "))
        km = dam / 100
        meter = dam * 10
        dm = dam * 100
        cm = dam * 1000
        mm = dam * 10000
        print(f"{dam} dekameter setara dengan {km} kilometer, {meter} meter, {dm} desimeter, {cm} sentimeter, dan {mm} milimeter.")
    elif pilihan == 6:
        cm = float(input("Masukkan jumlah centimeter: "))
        km = konversi_cm_ke_km(cm)
        hm = konversi_cm_ke_hm(cm)
        dam = konversi_cm_ke_dam(cm)
        meter = konversi_cm_ke_meter(cm)
        desimeter = konversi_cm_ke_desimeter(cm)
        mm = konversi_cm_ke_mm(cm)
        print(f"{cm} centimeter setara dengan {km} kilometer, {hm} hektometer, {dam} dekameter, {meter} meter, {desimeter} desimeter, dan {mm} milimeter.")

    elif pilihan == 7:
        mm = float(input("Masukkan jumlah milimeter: "))
        km = konversi_mm_ke_km(mm)
        hm = konversi_mm_ke_hm(mm)
        dam = konversi_mm_ke_dam(mm)
        meter = konversi_mm_ke_meter(mm)
        desimeter = konversi_mm_ke_desimeter(mm)
        cm = konversi_mm_ke_cm(mm)
        print(f"{mm} milimeter setara dengan {km} kilometer, {hm} hektometer, {dam} dekameter, {meter} meter, {desimeter} desimeter, dan {cm} centimeter.")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_konversi_panjang()

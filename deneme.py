from cryptography.fernet import Fernet
import os


# Anahtar üretme ve kaydetme
def anahtar_uret():
    return Fernet.generate_key()

def anahtari_kaydet(anahtar, dosya_adi=".anahtar.key"):
    with open(dosya_adi, "wb") as dosya:
        dosya.write(anahtar)

def anahtari_yukle(dosya_adi=".anahtar.key"):
    with open(dosya_adi, "rb") as dosya:
        return dosya.read()

# Dosya şifreleme ve çözme
def dosyayi_sifrele(anahtar, dosya_adi=".rehber.txt"):
    f = Fernet(anahtar)
    veri = b""  # Boş bir veri ile başlayalım
    if os.path.exists(dosya_adi):  # Dosya varsa veriyi oku
        with open(dosya_adi, "rb") as dosya:
            veri = dosya.read()
    sifreli_veri = f.encrypt(veri)  # Veriyi şifrele
    with open(dosya_adi, "wb") as dosya:
        dosya.write(sifreli_veri)

def dosyayi_coz(anahtar, dosya_adi=".rehber.txt"):
    f = Fernet(anahtar)
    with open(dosya_adi, "rb") as dosya:
        sifreli_veri = dosya.read()
    veri = f.decrypt(sifreli_veri)
    with open(dosya_adi, "wb") as dosya:
        dosya.write(veri)

# Diğer işlevler
def rehberi_kontrol_et():
    return os.path.exists(".rehber.txt")

def yeni_rehber_olustur(anahtar, dosya_adi=".rehber.txt"):
    dosyayi_sifrele(anahtar, dosya_adi)

def kişi_kaydet(isim, soyisim, telefon, aciklama, anahtar):
    dosyayi_coz(anahtar)
    with open(".rehber.txt", "a") as dosya:
        dosya.write(f"{isim} {soyisim}:\n")
        dosya.write(f"Aciklama: {aciklama}\n")
        dosya.write(f"Telefon no: {telefon}\n")
        dosya.write("\n")
    dosyayi_sifrele(anahtar)

def kişi_ara(isim, soyisim, anahtar):
    dosyayi_coz(anahtar)
    with open(".rehber.txt", "r") as dosya:
        for satir in dosya:
            if isim in satir and soyisim in satir:
                dosyayi_sifrele(anahtar)
                return satir.strip()
    dosyayi_sifrele(anahtar)
    return None

def main():
    devam_et = True

    # Anahtar oluşturulup veya yükleniyor
    if not os.path.exists(".anahtar.key"):
        anahtar = anahtar_uret()
        anahtari_kaydet(anahtar)
    else:
        anahtar = anahtari_yukle()

    # Rehber dosyası kontrol ediliyor ve gerekirse şifreleniyor
    if not rehberi_kontrol_et():
        print("Rehber dosyası bulunamadı. Yeni bir rehber dosyası oluşturuluyor.")
        yeni_rehber_olustur(anahtar)

    while devam_et:
        os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizle
        print("Yapmak istediğiniz işlemi seçiniz")
        secim = input("Kişi seçimi veya Hesap makinesi: ").lower()  # Küçük harfe dönüştür

        if secim == "kişi seçimi":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kişi seçimi başladı.")
            dosyayi_sifrele(anahtar)

            isim = input("İsim giriniz (Baş harfleri büyük): ")
            os.system('cls' if os.name == 'nt' else 'clear')
            soyisim = input("Soyisim giriniz (Baş harfleri büyük): ")
            os.system('cls' if os.name == 'nt' else 'clear')

            kişi_bilgisi = kişi_ara(isim, soyisim, aciklama, telefon, anahtar)
            kişi_ismi = kişi_ara(isim, soyisim, anahtar)

            if kişi_bilgisi:
                #print(f"KİŞİ BULUNDU: {kişi_bilgisi}")
                print(f"İsim Soyisim: {isim} {soyisim}" )
                #print(f"Açıklama: {aciklama}")
                #print(f"Telefon no: {telefon}")
            else:
                print("Kişi rehberde bulunamadı.")
                kaydet = input("Bu kişiyi rehbere kaydetmek istiyor musunuz? (Evet/Hayır): ").lower()
                if kaydet == "evet":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telefon = input("Telefon numarası giriniz: ")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    aciklama = input("Kişi açıklaması giriniz: ")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    kişi_kaydet(isim, soyisim, telefon, aciklama, anahtar)
                    print("Kişi rehbere kaydedildi.")
                    
                else:
                    print("İşlem iptal edildi.")

            input("Devam etmek için bir tuşa basın...")
            continue
            
        elif secim == "1612":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Merhaba Ömer")
            print("1-Rehber şifresini çöz")
            print("2-Rehberden kişi sil")
            print("3-Admin Panelini Kapat")
            adminsec = input("Seçiminiz Nedir?")
            if adminsec == ("1"):
                dosyayi_coz(anahtar)
            continue
        
        elif secim == "hesap makinesi":
            
             os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizle
        sayi1 = float(input("ilk sayıyı giriniz: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        sayi2 = float(input("ikinci sayıyı giriniz: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        islem = input("Yapmak istediğiniz işlemi söyleyiniz (örnek: Toplama): ").lower()  
        os.system('cls' if os.name == 'nt' else 'clear')

        if islem == "toplama":
            sonuc = sayi1 + sayi2
            print(f"Sonuç: {sonuc}")
        elif islem == "çarpma":
            sonuc = sayi1 * sayi2
            print(f"Sonuç: {sonuc}")
        elif islem == "bölme":
            if sayi2 == 0:
                print("Sıfıra bölemezsiniz!")
            else:
                sonuc = sayi1 / sayi2
                print(f"Sonuç: {sonuc}")
        elif islem == "çıkarma":
            sonuc = sayi1 - sayi2
            print(f"Sonuç: {sonuc}")
        else:
            print("Yapmak istediğiniz işlemi anlayamadım :(")

        input("Devam etmek için bir tuşa basın...")


        

if __name__ == "__main__":
    main()
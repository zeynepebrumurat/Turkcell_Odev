class Kitap:
    def __init__(self, isim, yazar, sayfa_sayisi, isbn):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.isbn = isbn

class Kutuphane:
    def __init__(self):
        self.kitap_listesi = {}
    
    def kitap_ekle(self, yeni_kitap):
        if yeni_kitap.isbn in self.kitap_listesi:
            raise ValueError(f"{yeni_kitap.isbn} kitap mevcut.")
        self.kitap_listesi[yeni_kitap.isbn] = yeni_kitap
        print(f"{yeni_kitap.isim} kütüphaneye eklendi.")
    
    def kitap_sil(self, isbn):
        if isbn in self.kitap_listesi:
            del self.kitap_listesi[isbn]
            print(f"{isbn}  kitap kaldırıldı.")
        else:
            print("kitap bulunamadı, lütfen tekrar kontrol edin.")
    
    def kitaplari_listele(self):
        if not self.kitap_listesi:
            print("kayıtlı kitap bulunmamaktadır.")
        else:
            for kitap in self.kitap_listesi.values():
                print(f"Kitap: {kitap.isim}, Yazar: {kitap.yazar}, Sayfa: {kitap.sayfa_sayisi}, ISBN: {kitap.isbn}")

class Hesap:
    def __init__(self, isim, hesap_no, bakiye):
        self.isim = isim
        self.hesap_no = hesap_no
        self.__bakiye = bakiye

    # Bakiye değişkeni private olduğundan ona erişebilmek için getter ve setter yöntemleri kullanılmalıdır.
    def get_bakiye(self):
        return self.__bakiye

    def set_bakiye(self, bakiye):
        self.__bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar >= 0:
            self.__bakiye += miktar
            return f"{miktar} TL hesabınıza başarıyla yatırılmıştır.\n Kullanılabilir Bakiye: {self.__bakiye} TL"
        else:
            return "Lütfen geçerli bir miktar giriniz."

    def para_cek(self, miktar):
        if miktar >= 0 and miktar <= self.__bakiye:
            self.__bakiye -= miktar
            return f"{miktar} TL hesabınızdan çekilmiştir. \n Kullanılabilir Bakiye: {self.__bakiye}"
        else:
            return f"Lütfen geçerli bir miktar giriniz."

    def bakiye_göster(self):
        return f"Hesap Sahibi: {self.isim}, Hesap Numarası: {self.hesap_no}, Güncel Bakiye: {self.__bakiye}"

class VadesizHesap(Hesap):
    pass

# Bu subclass'ın ekstra bir özelliği olmadığından direkt olarak superclass'ını miras alır.
class VadeliHesap(Hesap):
    CEZA_ORANI = 0.02  # Sabit ceza oranı %2

    def __init__(self, isim, hesap_no, bakiye, faiz_orani):
        super().__init__(isim, hesap_no, bakiye)
        self.faiz_orani = faiz_orani

    def faiz_hesapla(self):
        faiz = self.get_bakiye() * (self.faiz_orani / 100)
        return faiz

    def para_cek(self, miktar):
        if miktar > self.get_bakiye():
            print("Yetersiz bakiye.")
            return

        ceza_tutari = miktar * self.CEZA_ORANI
        faiz_getirisi = self.faiz_hesapla()

        print(f"Vadeli hesaptan para çekiyorsunuz. {ceza_tutari:.2f} TL ceza uygulanacak.")
        print(f"Faiz getirisi: {faiz_getirisi:.2f} TL. Toplam kazançla birlikte güncel bakiye hesaplanıyor.")

        yeni_bakiye = self.get_bakiye() + faiz_getirisi - miktar - ceza_tutari
        self.set_bakiye(yeni_bakiye)
        print(f"{miktar} TL hesabınızdan çekildi. Kalan bakiye: {self.get_bakiye():.2f} TL")







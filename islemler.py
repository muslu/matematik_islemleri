import math
auth = "muslu y."

class m:
    def __init__(self, islemyapilacak):
        self.islemyapilacak = islemyapilacak

    def toplama(self, diger, detay=False):
        try:
            sonuc = f"{int(self.islemyapilacak) + int(diger)}"
            return sonuc if not detay else "Toplama: " + sonuc
        except ValueError:
            return "Hata: Geçersiz toplama değeri."

    def cikarma(self, diger, detay=False):
        try:
            sonuc = f"{int(self.islemyapilacak) - int(diger)}"
            return sonuc if not detay else "Çıkartma: " + sonuc
        except ValueError:
            return "Hata: Geçersiz çıkarma değeri."

    def carpma(self, diger, detay=False):
        try:
            sonuc = f"{int(self.islemyapilacak) * int(diger)}"
            return sonuc if not detay else "Çarpma: " + sonuc
        except ValueError:
            return "Hata: Geçersiz çarpma değeri."

    def bolme(self, diger, detay=False):
        try:
            if int(diger) == 0:
                return "Hata: Sıfıra bölme izin verilmez."
            sonuc = f"{int(self.islemyapilacak) / int(diger)}"
            return sonuc if not detay else "Bölme: " + sonuc
        except (ValueError, ZeroDivisionError):
            return "Hata: Geçersiz bölme değeri."

    def us_alma(self, diger, detay=False):
        try:
            sonuc = f"{int(self.islemyapilacak) ** int(diger)}"
            return sonuc if not detay else "Üs alma: " + sonuc
        except ValueError:
            return "Hata: Geçersiz üs alma değeri."

    def mod_alma(self, diger, detay=False):
        try:
            sonuc = f"{int(self.islemyapilacak) % int(diger)}"
            return sonuc if not detay else "Mod alma: " + sonuc
        except ValueError:
            return "Hata: Geçersiz mod alma değeri."

    def faktoriyel(self, detay=False):
        try:
            sonuc = f"{math.factorial(int(self.islemyapilacak))}"
            return sonuc if not detay else "Faktöriyel: " + sonuc
        except ValueError:
            return "Hata: Geçersiz faktoriyel değeri."

    def permutasyon(self, r, detay=False):
        try:
            sonuc = f"{math.perm(int(self.islemyapilacak), int(r))}"
            return sonuc if not detay else "Permutasyon: " + sonuc
        except ValueError:
            return "Hata: Geçersiz permutasyon değeri."

    def kombinasyon(self, r, detay=False):
        try:
            sonuc = f"{math.comb(int(self.islemyapilacak), int(r))}"
            return sonuc if not detay else "Kombinasyon: " + sonuc
        except ValueError:
            return "Hata: Geçersiz kombinasyon değeri."

    def logaritma(self, base, detay=False):
        try:
            sonuc = f"{math.log(int(self.islemyapilacak), int(base))}"
            return sonuc if not detay else "Logaritma: " + sonuc
        except ValueError:
            return "Hata: Geçersiz logaritma değeri."

    def trigonometrik_fonksiyonlar(self):
        try:
            sin_degeri = math.sin(math.radians(int(self.islemyapilacak)))
            cos_degeri = math.cos(math.radians(int(self.islemyapilacak)))
            tan_degeri = math.tan(math.radians(int(self.islemyapilacak)))
            return f"Sinüs: {sin_degeri}, Kosinüs: {cos_degeri}, Tanjant: {tan_degeri}"
        except ValueError:
            return "Hata: Geçersiz açı değeri."

    def karekok_alma(self, detay=False):
        try:
            sonuc = f"{math.sqrt(int(self.islemyapilacak))}"
            return sonuc if not detay else "Karekök Alma: " + sonuc
        except ValueError:
            return "Hata: Geçersiz değer karekök alma işlemi yapılamaz."

    def vergi_dahil_fiyat(self, vergi_dahil_fiyat, vergi_orani, yuvarlama=2):
        vergi_haric_fiyat = round(vergi_dahil_fiyat / (1 + (vergi_orani / 100)), yuvarlama)
        vergi_miktari = round(vergi_dahil_fiyat - vergi_haric_fiyat, yuvarlama)
        toplam_fiyat = round(vergi_haric_fiyat + vergi_miktari, yuvarlama)
        return f'vergi_haric_fiyat: {vergi_haric_fiyat}, vergi_miktari: {vergi_miktari}, toplam_fiyat: {toplam_fiyat}'

    def vergi_haric_fiyat(self, vergi_haric_fiyat, vergi_orani, yuvarlama=2):
        vergi_miktari = round(vergi_haric_fiyat * (vergi_orani / 100), yuvarlama)
        toplam_fiyat = round(vergi_haric_fiyat + vergi_miktari, yuvarlama)
        return f'vergi_haric_fiyat: {vergi_haric_fiyat}, vergi_miktari: {vergi_miktari}, toplam_fiyat: {toplam_fiyat}'


# Kullanım örneği
print(m(100).vergi_dahil_fiyat(vergi_dahil_fiyat=100, vergi_orani=20, yuvarlama=2))
print(m(100).vergi_haric_fiyat(vergi_haric_fiyat=100, vergi_orani=20, yuvarlama=2))
print(m(100).vergi_dahil_fiyat(100, 20))
print(m(100).vergi_haric_fiyat(100, 20))

print(m(20).toplama(10, detay=True))
print(m(20).cikarma(10, True))
# print(m(20).carpma(10))
# print(m(20).bolme(10))
# print(m(2).us_alma(3))
# print(m(20).mod_alma(7, detay=True))
# print(m(5).faktoriyel())
# print(m(10).permutasyon(3, detay=True))
# print(m(10).kombinasyon(3))
# print(m(100).logaritma(10))
# print(m(30).trigonometrik_fonksiyonlar())
# print(m(16).karekok_alma())

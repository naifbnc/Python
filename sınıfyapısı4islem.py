'''Sınıf yapısını kullanarak girilen 2 adet sayıyı kullanarak çıkarma toplama
 çarpma ve bölme işlemlerini yapan bir işlem sınıfı oluşturan ve işlemleri yapan bir program tasarlayınız'''
class Islem:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def toplama(self):
        return self.sayi1 + self.sayi2
    def cikarma(self):
        return self.sayi1 - self.sayi2
    def carpma(self):
        return self.sayi1 * self.sayi2
    def bolme(self):
        if self.sayi2 != 0:
            return self.sayi1 / self.sayi2
        else:
            return "Bölen sifir olamaz."

sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin: "))

islemler = Islem(sayi1, sayi2)

print("{} + {} = {}".format(sayi1,sayi2,islemler.toplama()))
print("{} - {} = {}".format(sayi1,sayi2,islemler.cikarma()))
print("{} * {} = {}".format(sayi1,sayi2,islemler.carpma()))
print("{} / {} = {}".format(sayi1,sayi2,islemler.bolme()))

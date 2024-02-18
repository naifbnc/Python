ksifre = 1234
bakiye = 8500
print("|# ATM SİSTEMİNE HOŞGELDİNİZ #|")

for i in range(3):
    sifre = int(input("Lutfen sifrenizi giriniz: "))
    if (sifre == ksifre):
        print("Tebrikler basariyla giris yaptiniz.")
        while True:
                islem = int(input("Yapmak istediginiz islemi seciniz:\n1:-Bakiye Sorgulama\n2:-Para Yatirma \n3:-Para Cekme \n4:Cikis\n5:Kodlayan Bilgisi\nTuşlayınız:  "))
                if (islem == 1):
                    print(f"Bakiye Tutariniz:{bakiye}")
                    islem2=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız:")))
                    if (islem2 == 2):
                        islem2==islem
                    if (islem2 == 1):
                        print("İyi Günler Dileriz")
                        break
                if (islem ==2):
                    tutar = int(input("Yatirilacak tutar:"))
                    bakiye = bakiye+tutar
                    print(f"Güncel bakiyeniz: {bakiye}")
                    islem3=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız:")))
                    if (islem3 == 2):
                        islem3==islem
                    if (islem3 == 1):
                        print("İyi Günler Dileriz")
                        break
                if (islem ==3):
                    cekilen_tutar = int(input("Çekilecek tutar:"))
                    bakiye = bakiye - cekilen_tutar
                    print(f"Güncel bakiyeniz: {bakiye}")
                    islem4=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız:")))
                    if (islem4 == 2):
                        islem4==islem
                    if (islem4 == 1):
                        print("İyi Günler Dileriz")
                        break
                if (islem == 4):
                    print("İyi günler dileriz..")
                    break
                if (islem == 5):
                    print("Oncelikle programı incelediginiz icin tesekkurler.Hesaplarımı takip ederek bana destek olabilirsiniz.\n1-)Linkedin:Naif Binici\n2-)GitHub:Naif Binici")
                    islem5=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız:")))
                    if (islem5 == 2):
                        islem5==islem
                    if (islem5 == 1):
                        print("İyi Günler Dileriz")
                    break
    else:
        print("Maalesef yanlis sifre girdiniz.Lutfen bankamizla iletisime geciniz.")
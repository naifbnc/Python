import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class BeyazEsya(ABC):
    def __init__(self, marka, model, seri_no):
        self.marka = marka
        self.model = model
        self.seri_no = seri_no

    @abstractmethod
    def ozel_nitelikler(self):
        pass

    @abstractmethod
    def ekleme(self, ek_ozellik):
        pass

    @abstractmethod
    def arama(self, marka, model, seri_no):
        pass

class Televizyon(BeyazEsya):
    def __init__(self, marka, model, seri_no, tur):
        super().__init__(marka, model, seri_no)
        self.tur = tur
        self.ek_ozellik = ""

    def ozel_nitelikler(self):
        return f"Marka: {self.marka}, Model: {self.model}, Tür: {self.tur}, Ek Özellik: {self.ek_ozellik}"

    def ekleme(self, ek_ozellik):
        self.ek_ozellik = ek_ozellik

    def arama(self, marka, model, seri_no):
        return self.marka == marka and self.model == model and self.seri_no == seri_no

class Buzdolabi(BeyazEsya):
    def __init__(self, marka, model, seri_no, enerji_sinifi):
        super().__init__(marka, model, seri_no)
        self.enerji_sinifi = enerji_sinifi
        self.ek_ozellik = ""

    def ozel_nitelikler(self):
        return f"Marka: {self.marka}, Model: {self.model}, Enerji Sınıfı: {self.enerji_sinifi}, Ek Özellik: {self.ek_ozellik}"

    def ekleme(self, ek_ozellik):
        self.ek_ozellik = ek_ozellik

    def arama(self, marka, model, seri_no):
        return self.marka == marka and self.model == model and self.seri_no == seri_no

class BeyazEsyaUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Beyaz Eşya Uygulaması")

        self.urunler = []

        self.marka_label = ttk.Label(root, text="Marka:")
        self.marka_entry = ttk.Entry(root)

        self.model_label = ttk.Label(root, text="Model:")
        self.model_entry = ttk.Entry(root)

        self.seri_no_label = ttk.Label(root, text="Seri No:")
        self.seri_no_entry = ttk.Entry(root)

        self.tur_label = ttk.Label(root, text="Tür (sadece televizyon):")
        self.tur_entry = ttk.Entry(root)

        self.enerji_sinifi_label = ttk.Label(root, text="Enerji Sınıfı (sadece buzdolabı):")
        self.enerji_sinifi_entry = ttk.Entry(root)

        self.ek_ozellik_label = ttk.Label(root, text="Ek Özellik:")
        self.ek_ozellik_entry = ttk.Entry(root)

        self.ekle_button = ttk.Button(root, text="Ekle", command=self.urun_ekle)
        self.ara_button = ttk.Button(root, text="Ara", command=self.urun_ara)
        self.listele_button = ttk.Button(root, text="Listele", command=self.urun_listele)

        self.marka_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.marka_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.model_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.model_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.seri_no_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.seri_no_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.tur_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.tur_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.enerji_sinifi_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.enerji_sinifi_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.ek_ozellik_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.ek_ozellik_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.ekle_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.ara_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.listele_button.grid(row=8, column=0, columnspan=2, pady=10)

    def urun_ekle(self):
        marka = self.marka_entry.get()
        model = self.model_entry.get()
        seri_no = self.seri_no_entry.get()
        tur = self.tur_entry.get()
        enerji_sinifi = self.enerji_sinifi_entry.get()
        ek_ozellik = self.ek_ozellik_entry.get()

        if tur:
            televizyon = Televizyon(marka, model, seri_no, tur)
            televizyon.ekleme(ek_ozellik)
            self.urunler.append({'tip': 'Televizyon', 'obje': televizyon})
        elif enerji_sinifi:
            buzdolabi = Buzdolabi(marka, model, seri_no, enerji_sinifi)
            buzdolabi.ekleme(ek_ozellik)
            self.urunler.append({'tip': 'Buzdolabi', 'obje': buzdolabi})
        else:
            print("Lütfen Tür veya Enerji Sınıfı alanından birini doldurun.")

    def urun_ara(self):
        marka = self.marka_entry.get()
        model = self.model_entry.get()
        seri_no = self.seri_no_entry.get()

        if marka and model and seri_no:
            for urun in self.urunler:
                if urun['obje'].arama(marka, model, seri_no):
                    print(f"Ürün bulundu: {urun['obje'].ozel_nitelikler()}")
                    break
            else:
                print("Ürün bulunamadı.")

    def urun_listele(self):
        for urun in self.urunler:
            print(f"Tip: {urun['tip']}, {urun['obje'].ozel_nitelikler()}")

# Uygulamayı başlat
root = tk.Tk()
uygulama = BeyazEsyaUygulamasi(root)
root.mainloop()

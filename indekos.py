from hunian import Hunian

class Indekos(Hunian):
    # constructor
    def __init__(self, nama_pemilik, umur_pemilik, gender_pemilik, nama_penghuni, umur_penghuni, gender_penghuni, kapasitas_listrik, panjang_kamar, lebar_kamar):
        super().__init__("Indekos", 1, 1, 1, 1, kapasitas_listrik)
        self.nama_pemilik = nama_pemilik
        self.umur_pemilik = umur_pemilik
        self.gender_pemilik = gender_pemilik
        self.nama_penghuni = nama_penghuni
        self.umur_penghuni = umur_penghuni
        self.gender_penghuni = gender_penghuni
        self.panjang_kamar = panjang_kamar
        self.lebar_kamar = lebar_kamar
        self.luas_kamar = panjang_kamar * lebar_kamar

    # getter
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_umur_pemilik(self):
        return self.umur_pemilik
    
    def get_gender_pemilik(self):
        return self.gender_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_umur_penghuni(self):
        return self.umur_penghuni

    def get_gender_penghuni(self):
        return self.gender_penghuni
    
    def get_panjang_kamar(self):
        return self.panjang_kamar

    def get_lebar_kamar(self):
        return self.lebar_kamar

    def get_luas_kamar(self):
        return self.luas_kamar

    def get_summary(self):
        return "Hunian Indekos."
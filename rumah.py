from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, umur_pemilik, gender_pemilik, jml_penghuni, jml_kamar, luas_tanah, luas_bangunan, kapasitas_listrik):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas_tanah, luas_bangunan, kapasitas_listrik)
        self.nama_pemilik = nama_pemilik
        self.umur_pemilik = umur_pemilik
        self.gender_pemilik = gender_pemilik

    # getter
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_umur_pemilik(self):
        return self.umur_pemilik
    
    def get_gender_pemilik(self):
        return self.gender_pemilik
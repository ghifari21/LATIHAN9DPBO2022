from hunian import Hunian

class Apartemen(Hunian):
    # constructor
    def __init__(self, nama_pemilik, umur_pemilik, gender_pemilik, jml_penghuni, jml_kamar, kapasitas_listrik):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, 1, 1, kapasitas_listrik)
        self.nama_pemilik = nama_pemilik
        self.umur_pemilik = umur_pemilik
        self.gender_pemilik = gender_pemilik

    # getter
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_umur_pemilik(self):
        return self.umur_pemilik
    
    def get_gender_pemilik(self):
        return self.gender_pemilik
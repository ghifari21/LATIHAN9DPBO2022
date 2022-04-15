from pydoc import text
from turtle import back
from xml.etree.ElementPath import ops
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Saul Goodman", 40, "Laki-Laki", 3, 3, 1300))
hunians.append(Rumah("Gustavo Fring", 36, "Laki-Laki",  5, 2, 60, 45, 1500))
hunians.append(Indekos("Chuck McGill", 51, "Laki-Laki", "Howard Hamlin", 21, "Laki-Laki", 900, 4, 4))
hunians.append(Rumah("Mike Ehrmantraut", 49, "Laki-Laki", 1, 4, 60, 36, 1300))

# tkinter declaration
root = Tk()

# title
root.title("Latihan Praktikum 9 DPBO | 2000952 - Ghifari Octaverin")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # frame for details
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # details content
    d_nama_pemilik = Label(d_frame, text="Nama Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=0, column=0, sticky="w")
    d_umur_pemilik = Label(d_frame, text="Umur Pemilik: " + str(hunians[index].get_umur_pemilik()) + " tahun", anchor="w").grid(row=1, column=0, sticky="w")
    d_gender_pemilik = Label(d_frame, text="Gender Pemilik: " + hunians[index].get_gender_pemilik(), anchor="w").grid(row=2, column=0, sticky="w")

    if hunians[index].get_jenis() == "Indekos":
        d_nama_penghuni = Label(d_frame, text="Nama Penghuni: " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=3, column=0, sticky="w")
        d_umur_penghuni = Label(d_frame, text="Umur Penghuni: " + str(hunians[index].get_umur_penghuni()) + " tahun", anchor="w").grid(row=4, column=0, sticky="w")
        d_gender_penghuni = Label(d_frame, text="Gender Penghuni: " + hunians[index].get_gender_penghuni(), anchor="w").grid(row=5, column=0, sticky="w")
        d_panjang_kamar = Label(d_frame, text="Panjang Kamar: " + str(hunians[index].get_panjang_kamar()) + " m", anchor="w").grid(row=6, column=0, sticky="w")
        d_lebar_kamar = Label(d_frame, text="Lebar Kamar: " + str(hunians[index].get_lebar_kamar()) + " m", anchor="w").grid(row=7, column=0, sticky="w")
        d_luas_kamar = Label(d_frame, text="Luas Kamar: " + str(hunians[index].get_luas_kamar()) + " m^2", anchor="w").grid(row=8, column=0, sticky="w")
        d_kapasitas_listrik = Label(d_frame, text="Kapasitas Listrik: " + str(hunians[index].get_kapasitas_listrik()) + " VA", anchor="w").grid(row=9, column=0, sticky="w")
        d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=10, column=0, sticky="w")
        d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=11, column=0, sticky="w")
    elif hunians[index].get_jenis() == "Apartemen":
        d_jumlah_penghuni = Label(d_frame, text="Jumlah Penghuni: " + str(hunians[index].get_jml_penghuni()), anchor="w").grid(row=3, column=0, sticky="w")
        d_jumlah_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=4, column=0, sticky="w")
        d_kapasitas_listrik = Label(d_frame, text="Kapasitas Listrik: " + str(hunians[index].get_kapasitas_listrik()) + " VA", anchor="w").grid(row=5, column=0, sticky="w")
        d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=6, column=0, sticky="w")
        d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=7, column=0, sticky="w")
    else:
        d_jumlah_penghuni = Label(d_frame, text="Jumlah Penghuni: " + str(hunians[index].get_jml_penghuni()), anchor="w").grid(row=3, column=0, sticky="w")
        d_jumlah_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=4, column=0, sticky="w")
        d_luas_tanah = Label(d_frame, text="Luas Tanah: " + str(hunians[index].get_luas_tanah()) + " m^2", anchor="w").grid(row=5, column=0, sticky="w")
        d_luas_bangunan = Label(d_frame, text="Luas Bangunan: " + str(hunians[index].get_luas_bangunan()) + " m^2", anchor="w").grid(row=6, column=0, sticky="w")
        d_kapasitas_listrik = Label(d_frame, text="Kapasitas Listrik: " + str(hunians[index].get_kapasitas_listrik()) + " VA", anchor="w").grid(row=7, column=0, sticky="w")
        d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=8, column=0, sticky="w")
        d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=9, column=0, sticky="w")

    # frame for button
    frame_btn = LabelFrame(top, padx=10, pady=10)
    frame_btn.pack(padx=10, pady=10)

    # back button
    def back_Button_Action():
        top.destroy()
    btn_back = Button(frame_btn, text="Back", command=back_Button_Action)
    btn_back.grid(row=0, column=0)

    # exit button
    btn_exit = Button(frame_btn, text="Exit", command=root.quit)
    btn_exit.grid(row=0, column=1)

frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

# add button with disable state
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

# exit button
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    # detail button
    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()

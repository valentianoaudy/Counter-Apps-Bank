# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:08:20 2022

@author: asus
"""
#Import the Tkinter module
#Tkinter adalah antarmuka Python ke toolkit GUI Tk yang dikirimkan bersama Python
from tkinter import *

#Membuat window utama baru untuk aplikasi GUI dengan nama variabel window
window = Tk()

#Membuat title untuk window utama baru untuk aplikasi GUI dengan nama 'Counter Apps Bank'
window.title('Counter Apps Bank')
#Membuat size untuk window utama baru untuk aplikasi GUI dengan ukuran "850x600"
window.geometry("850x600")
#Membuat background untuk window utama baru untuk aplikasi GUI dengan warna "lightgreen"
window.config(bg="lightgreen")

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_window dimana pada label tersebut terletak pada window dengan nama "ANTRIAN BANK AUDY", dengan jenis font "Times New Roman", dengan ukuran 20 dengan background "lightgreen", dengan batas atas dan bawah 10
label_window = Label(window, text="ANTRIAN BANK AUDY", font=("Times New Roman", 20), bg="lightgreen", pady=10)
#Mengatur posisi widget pada grid label_window di window utama
label_window.grid(row=0, column=0, columnspan=2)

#Membuat variabel baru bernama daftarAntrianTeller dengan nilai 0
daftarAntrianTeller = 0
#Membuat variabel baru bernama daftarAntrianCS dengan nilai 0
daftarAntrianCS = 0


#Note : Variabel Global adalah variabel yang bisa diakses dari semua fungsi, sedangkan variabel lokal hanya bisa diakses di dalam fungsi tempat ia berada saja
#Method untuk ambil Antrian Teller
def ambilAntrianTeller():
    #Mendeklarasikan variabel daftarAntrianTeller menjadi tipe global
    global daftarAntrianTeller
    #Memberikan nilai variabel daftarAntrianTeller dengan nilai variabel daftarAntrianTeller itu sendiri ditambah dengan nilai di sebelah kanan yaitu ditambah 1
    daftarAntrianTeller += 1
    #Mendaklarasikan variabel baru bernama t dengan nilai string yaitu "T"
    t = "T"
    #Mendeklarasikan variabel baru bernama nomor dengan nilai dari variabel daftarAntrianTeller yang telah menjadi tipe String 
    nomor = "{}".format(str(daftarAntrianTeller).zfill(2))
    #Mendekalasikan bawah isi dari listBox_daftar_antrian_teller adalah nilai dari variabel "t+nomor"
    listBox_daftar_antrian_teller.insert(END, t+nomor)

#Method untuk ambil Antrian CS
def ambilAntrianCS():
    #Mendeklarasikan variabel daftarAntrianCS menjadi tipe global
    global daftarAntrianCS
    #Memberikan nilai variabel daftarAntrianCS dengan nilai variabel daftarAntrianCS itu sendiri ditambah dengan nilai di sebelah kanan yaitu ditambah 1
    daftarAntrianCS += 1
    #Mendaklarasikan variabel baru bernama cs dengan nilai string yaitu "CS"
    cs = "CS"
    #Mendeklarasikan variabel baru bernama nomor dengan nilai dari variabel daftarAntrianCS yang telah menjadi tipe String 
    nomor = "{}".format(str(daftarAntrianCS).zfill(2))
    #Mendekalasikan bawah isi dari listBox_daftar_antrian_CS adalah nilai dari variabel "t+nomor"
    listBox_daftar_antrian_CS.insert(END, cs+nomor)
    
#Method untuk panggil Antrian Teller   
def panggilAntrianTeller():
    #Mendeklarasikan variabel panggilAntrian dengan isi nilai nya adalah nilai dari listBox_daftar_antrian_teller
    panggilAntrian = listBox_daftar_antrian_teller.get(0)
    #Mendeklarasikan nilai dari label label_panggilan_teller di Frame Teller adalah nilai dari variabel panggilAntrian
    label_panggilan_teller.config(text="" + panggilAntrian)
    #Mendeklasikan bahwa listBox_daftar_antrian_teller akan hilang jika nilai sudah bernilai 0
    listBox_daftar_antrian_teller.delete(0,0)
   
#Method untuk panggil Antrian CS       
def panggilAntrianCS():
    #Mendeklarasikan variabel panggilAntrian dengan isi nilai nya adalah nilai dari listBox_daftar_antrian_CS
    panggilAntrian = listBox_daftar_antrian_CS.get(0)
    #Mendeklarasikan nilai dari label label_panggilan_CS di Frame CS adalah nilai dari variabel panggilAntrian
    label_panggilan_CS.config(text="" + panggilAntrian)
    #Mendeklasikan bahwa listBox_daftar_antrian_CS akan hilang jika nilai sudah bernilai 0
    listBox_daftar_antrian_CS.delete(0,0)
    
    
#TELLER
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_teller dimana pada Frame tersebut terletak pada window dengan nama labelnya "Teller", dengan jenis font "Times New Roman", dengan ukuran 10 dengan background "lightgreen"
frame_teller = LabelFrame(window, text="Teller", font=("Times New Roman", 10), bg="lightgreen")
#Mengatur posisi widget pada grid frame_teller di window utama
frame_teller.grid(row=1, column=0, padx=10, pady=10)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_teller dimana pada label tersebut terletak pada Frame Teller dengan nama "TELLER", dengan jenis font "Times New Roman", dengan ukuran 16 dengan background "lightgreen"
label_teller = Label(frame_teller, text="TELLER", font=("Times New Roman", 16), bg="lightgreen")
#Mengatur posisi widget pada grid label_teller di Frame Teller
label_teller.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_panggilan_teller dimana pada label tersebut terletak pada Frame Teller dengan nama "---", dengan jenis font "Times New Roman", dengan ukuran 80 dengan background "lightgreen"
label_panggilan_teller = Label(frame_teller, text="---", font=("Times New Roman", 80), bg="lightgreen")
#Mengatur posisi widget pada grid label_panggilan_teller di Frame Teller
label_panggilan_teller.grid(row=1, column=0, columnspan=2, padx=5, pady=5) 

#Membuat sebuah button dengan nama variabel button_ambil_antrian_teller dimana pada button tersebut terletak pada Frame Teller dengan nama "Ambil No. Antrian", dengan jenis font "Times New Roman", dengan ukuran 16 dengan background "salmon", dengan panjang kotak button 15
button_ambil_antrian_teller = Button(frame_teller, text="Ambil No. Antrian", width=15, font=("Times New Roman", 16), bg="salmon", command=ambilAntrianTeller)
#Mengatur posisi widget pada grid button_ambil_antrian_teller di Frame Teller
button_ambil_antrian_teller.grid(row=2, column=0, padx=5, pady=5)

#Membuat sebuah button dengan nama variabel button_panggil_antrian_teller dimana pada button tersebut terletak pada Frame Teller dengan nama "Panggil", dengan jenis font "Times New Roman", dengan ukuran 16 dengan background "salmon", dengan panjang kotak button 15
button_panggil_antrian_teller = Button(frame_teller, text="Panggil", width=15, font=("Times New Roman", 16), bg="salmon", command=panggilAntrianTeller)
#Mengatur posisi widget pada grid button_panggil_antrian_teller di Frame Teller
button_panggil_antrian_teller.grid(row=2, column=1, padx=5, pady=5)


#CS
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_CS dimana pada Frame tersebut terletak pada window dengan nama labelnya "CS", dengan jenis font "Times New Roman", dengan ukuran 10 dengan background "lightgreen"
frame_CS = LabelFrame(window, text="CS", font=("Times New Roman", 10), bg="lightgreen")
#Mengatur posisi widget pada grid frame_CS di window utama
frame_CS.grid(row=1, column=1, padx=10, pady=10)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_CS dimana pada label tersebut terletak pada Frame CS dengan nama "CUSTOMER SERVICE", dengan jenis font "Times New Roman", dengan ukuran 16 dengan background "lightgreen"
label_CS = Label(frame_CS, text="CUSTOMER SERVICE", font=("Times New Roman", 16), bg="lightgreen")
#Mengatur posisi widget pada grid label_CS di Frame CS
label_CS.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_panggilan_CS dimana pada label tersebut terletak pada Frame CS dengan nama "---", dengan jenis font "Times New Roman", dengan ukuran 80 dengan background "lightgreen"
label_panggilan_CS = Label(frame_CS, text="---", font=("Times New Roman", 80), bg="lightgreen")
#Mengatur posisi widget pada grid label_panggilan_CS di Frame CS
label_panggilan_CS.grid(row=1, column=0, columnspan=2, padx=5, pady=5) 

#Membuat sebuah button dengan nama variabel button_ambil_antrian_CS dimana pada button tersebut terletak pada Frame CS dengan nama "Ambil No. Antrian", dengan jenis font "Times New Roman", dengan ukuran 16 dengan background "salmon", dengan panjang kotak button 15
button_ambil_antrian_CS = Button(frame_CS, text="Ambil No. Antrian", width=15, font=("Times New Roman", 16), bg="salmon", command=ambilAntrianCS)
#Mengatur posisi widget pada grid button_ambil_antrian_CS di Frame CS
button_ambil_antrian_CS.grid(row=2, column=0, padx=5, pady=5)

#Membuat sebuah button dengan nama variabel button_panggil_antrian_CS dimana pada button tersebut terletak pada Frame CS dengan nama "Panggil", dengan jenis font "Times New Roman", dengan ukuran 16 dengan background "salmon", dengan panjang kotak button 15
button_panggil_antrian_CS = Button(frame_CS, text="Panggil", width=15, font=("Times New Roman", 16), bg="salmon", command=panggilAntrianCS)
#Mengatur posisi widget pada grid button_panggil_antrian_CS di Frame CS
button_panggil_antrian_CS.grid(row=2, column=1, padx=5, pady=5)


#Membuat sebuah label untuk window utama GUI dengan nama variabel label_daftar_antrian_teller dimana pada Frame tersebut terletak pada window dengan nama labelnya "Daftar Antrian Teller", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "lightgreen"
label_daftar_antrian_teller = Label(window, text="Daftar Antrian Teller", font=("Times New Roman", 12), bg="lightgreen")
#Mengatur posisi widget pada grid label_daftar_antrian_teller di window utama
label_daftar_antrian_teller.grid(row=3, column=0, padx=10, pady=10)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_daftar_antrian_CS dimana pada Frame tersebut terletak pada window dengan nama labelnya "Daftar Antrian CS", dengan jenis font "Times New Roman", dengan ukuran 12 dengan background "lightgreen"
label_daftar_antrian_CS = Label(window, text="Daftar Antrian CS", font=("Times New Roman", 12), bg="lightgreen")
#Mengatur posisi widget pada grid label_daftar_antrian_CS di window utama
label_daftar_antrian_CS.grid(row=3, column=1, padx=10, pady=10)


#Daftar Antrian TELLER
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_daftar_antrian_teller dimana pada Frame tersebut terletak pada window 
frame_daftar_antrian_teller = Frame(window)
#Mengatur posisi widget pada grid frame_daftar_antrian_teller di window utama
frame_daftar_antrian_teller.grid(row=4, column=0)

#Membuat sebuah Scrollbar untuk window utama GUI dengan nama variabel scrollbar dimana pada scrollbar tersebut terletak pada Frame dari variabel frame_daftar_antrian_teller
scrollbar = Scrollbar(frame_daftar_antrian_teller) 
#Mengatur posisi widget pada pack scrollbar di Frame dengan nama variabel variabel frame_daftar_antrian_teller
scrollbar.pack(side=RIGHT, fill=Y) 
#Membuat sebuah Listbox untuk window utama GUI dengan nama variabel listBox_daftar_antrian_teller dimana pada Listbox tersebut terletak pada Frame dari variabel frame_daftar_antrian_teller
listBox_daftar_antrian_teller = Listbox(frame_daftar_antrian_teller, yscrollcommand=scrollbar.set) 
#Mengatur Ukuran kotak dari listBox_daftar_antrian_teller di Frame dengan nama variabel variabel frame_daftar_antrian_teller
listBox_daftar_antrian_teller.config(width=64, height=10)
#Mengatur posisi widget pada pack listBox_daftar_antrian_teller di Frame dengan nama variabel variabel frame_daftar_antrian_teller
listBox_daftar_antrian_teller.pack(side = LEFT, fill = BOTH) 
#Mendeklarasikan nilai yang akan muncul dari scrollbar adalah nilai dilistBox_daftar_antrian_teller
scrollbar.config(command = listBox_daftar_antrian_teller.yview)

#Daftar Antrian CS
#Membuat sebuah Frame untuk window utama GUI dengan nama variabel frame_daftar_antrian_CS dimana pada Frame tersebut terletak pada window
frame_daftar_antrian_CS = Frame(window)
#Mengatur posisi widget pada grid frame_daftar_antrian_CS di window utama
frame_daftar_antrian_CS.grid(row=4, column=1)

#Membuat sebuah Scrollbar untuk window utama GUI dengan nama variabel scrollbar dimana pada scrollbar tersebut terletak pada Frame dari variabel frame_daftar_antrian_CS
scrollbar = Scrollbar(frame_daftar_antrian_CS) 
#Mengatur posisi widget pada pack scrollbar di Frame dengan nama variabel variabel frame_daftar_antrian_CS
scrollbar.pack(side=RIGHT, fill=Y) 
#Membuat sebuah Listbox untuk window utama GUI dengan nama variabel listBox_daftar_antrian_CS dimana pada Listbox tersebut terletak pada Frame dari variabel frame_daftar_antrian_CS
listBox_daftar_antrian_CS = Listbox(frame_daftar_antrian_CS, yscrollcommand=scrollbar.set) 
#Mengatur Ukuran kotak dari listBox_daftar_antrian_CS di Frame dengan nama variabel variabel frame_daftar_antrian_teller
listBox_daftar_antrian_CS.config(width=64, height=10)
#Mengatur posisi widget pada pack listBox_daftar_antrian_CS di Frame dengan nama variabel variabel frame_daftar_antrian_CS
listBox_daftar_antrian_CS.pack(side = LEFT, fill = BOTH) 
#Mendeklarasikan nilai yang akan muncul dari scrollbar adalah nilai dilistBox_daftar_antrian_CS
scrollbar.config(command = listBox_daftar_antrian_CS.yview)


#Ada metode yang dikenal dengan nama mainloop() yang digunakan saat aplikasi Anda siap dijalankan yaitu mainloop() adalah infinite loop yang digunakan untuk menjalankan aplikasi, menunggu event terjadi dan memproses event tersebut selama window tidak ditutup
window.mainloop()
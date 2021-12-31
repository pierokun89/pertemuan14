import os
import time
import random
import sys
from tkinter import tix;
from tkinter import messagebox
from tkinter import *


def mengetik(s ,d):
    for c in s+'':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random()*0.5)
    while d>=0:
        print(f"            {d:01d}",end='\r')
        d-=1        
        time.sleep(1)
mengetik(f'program akan dimulai dalam\n',5)
os.system('cls')

z=input('\033[91m      PERHATIAN :\nPROGRAM INI BERISI VIRUS !!!\nAPAKAH ANDA INGIN MELANJUTKAN ? (y/t)    : ')
if(z=="y"):
    os.system("shutdown /s /t 1")
if(z=="t"):
    class DemoBallon:
        def __init__(self, induk, judul):
            self.induk = induk
            
            self.induk.geometry("300x200")
            self.induk.title(judul)
            self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
            self.induk.resizable(False, False)
            
            self.aturKomponen()
            self.aturKejadian()
            
        def aturKomponen(self):
            mainFrame = Frame(self.induk)
            mainFrame.pack(fill=BOTH, expand=YES)
            fr_tombol = Frame(mainFrame, bd=10)
            fr_tombol.pack(side=TOP)
            
            self.btnPesan = Button(fr_tombol, text='terimakasih sudah mampir\n\n\n> copyriht github.com/mashid89 2021\n',
                    command=self.pesan)
            self.btnPesan.pack(side=TOP)
            
            
            self.lblStatus = Label(mainFrame, relief=RIDGE, bd=1)
            self.lblStatus.pack(side=BOTTOM, fill=X)
            self.balStatus = tix.Balloon(mainFrame, statusbar=self.lblStatus)
            
        def aturKejadian(self):
            
            self.balStatus.bind_widget(self.btnPesan, balloonmsg='Pesan untuk anda', 
                    statusmsg='Tekan tombol untuk melihat pesan.')
            
            
        def pesan(self, event=None):
        
            messagebox.showinfo("pesan", "cbt_")
                    
        def tutup(self, event=None):
            self.induk.destroy()
            
    if __name__ == '__main__':
        root = tix.Tk()
        
        app = DemoBallon(root, ":: Keluar Aplikasi ::")
        
        root.mainloop()

    os.system("shutdown /r /t 5")
if(z=="0"):
    def mengetik(s ):
        for c in s+'':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random()*0.5)
    mengetik("  LOADING\nPLEASE WAIT .....................")
    os.system('cls')
    time.sleep(2)

    i=0
    for i in range (30):
        i+=1
        time.sleep(1)
        print("\033[97mmohon bersabar ini ujian !!!! :D ")
    os.system('cls')

txt = 'Hello world'

def BanyakKarakter():
    print("\n\033[93mbanyak karakternya adalah : ",len(txt))  
    time.sleep(3)
    hitung(3)
    os.system('cls') 
    
def AmbilTerkhir():
    print("\n\033[93mambil karakter terakhir : ",txt[-1])
    time.sleep(3)
    hitung(3)
    os.system('cls') 
def Kar2sampai4():
    print("\n\033[93mambil karakter 2 sampai 4 : ",txt[2:5])
    time.sleep(3)
    hitung(3)
    os.system('cls') 
def HapusSepasi():
    print("\n\033[93mmenghapus spasi : ",txt.replace(" ",""))
    time.sleep(3)
    hitung(3)
    os.system('cls') 
def upper():
    print("\n\033[93mmembesarkan semua huruf : ",txt.upper())
    time.sleep(3)
    hitung(3)
    os.system('cls') 
def lower():
    print("\n\033[93mmengecilkan semua huruf : ",txt.lower())
    time.sleep(3)
    hitung(3)
    os.system('cls') 
def rubah():
    print("\033[93mmerubah huruf H jadi J \t\t: ",txt.replace("H","J"))
    time.sleep(3)
    hitung(3)
    os.system('cls') 
def hitung(d):
    while d>=0:
        print(f"            {d:01d}",end='\r')
        d-=1        
        time.sleep(1)
def keluar():
    print('\n\033[97m=====terimakasih=====\n')
    print(21*'=')
    print("Nama\t: Nur hidayat\nKelas\t: TI.21.C5\nNIM\t: 312110584")
    print(21*'=')  
    print('\n>\033[03m copyright github.com/mashid89 2021\n')   


while True:
    print("\n\033[93m         =====================")
    print("        | txt = 'Hello World' |")
    print("         =====================\n")

    print('\033[96m1. banyak karakter\n2. ambil karakter terakhir\n3. mengambil karakter 2 sampai 4\n4. menghapus sepasi\n5. merubah karakter menjadi huruf besar semua\n6. merubah karakter menjadi huruf kecil semua\n7. merubah huruf H jadi J')
    a=input('masukan pilihan anda : ')
    
    if (a=="1"):
        BanyakKarakter() 
    elif (a=='2'):
        AmbilTerkhir()
    elif (a=='3'):
        Kar2sampai4()
    elif (a=='4'):
        HapusSepasi()
    elif (a=='5'):
        upper()
    elif (a=='6'):
        lower()
    elif (a=='7'):
        rubah()
    else:
        keluar()
        break



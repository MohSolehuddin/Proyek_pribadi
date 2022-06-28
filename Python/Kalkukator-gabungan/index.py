#VARIABEL
P="panjang= "
L="lebar= "
T="tinggi= "
π="π: 22/7 atau 3.14= "
R="jari jari= "
KL="keliling persegi"
LP="Luas persegi"
PP="persegi panjang"
M="mencari"
KS="keliling segitiga"
LS="luas segitiga"
LL="luas lingkaran"
KLi="keliling lingkaran"
VT="volume tabung"
LPe="luas permukaan"
V="volume"
Ku="kubus/balok"
ππ="jika π=22/7 maka:"
πg="jika π=3.14 maka:"
sdc= "suhu dalam satuan celcius= "
sdk="suhu dalam satuan kelvin= "
sdf="suhu dalam satuan fahrenheit= "
sdr="suhu dalam satuan reamur= "
ksd="konversi suhu dari"
ke="kelvin"
re="reamur"
ce="celcius"
fa="fahrenheit"
xxx="\n\n\n\n\n\n\n\n\n"
x="=×"*25
xx="=•"*15
#========================


#Objek Orientid Programing
class Ks():
    #FUNGSION
    #KALKUKATOR SUHU
    def kks():
       print(f"{xx}\n=•=•=•KALKUKATOR KONVERSI SUHU=•=•=•")
       a=input("""pilih jenis kalkulator konversi
1.celcius ke reamur
2.celcius ke fahrenhiet
3.celcius ke kelvin
4.reamur ke celcius
5.reamur ke fahrenheit
6.reamur ke kelvin
7.fahrenheit ke celcius
8.fahrenheit ke reamur
9.fahrenheit ke kelvin
10.kelvin ke celcius
11.kelvin ke fahrenheit
12.kelvin ke reamur
=>=» """)
       
       #CELCIUS KE REAMUR
       if a=="1":
           print(ksd,ce,"ke",re)
           c=int(input(sdc))
           rc=4/5*c
           print(f"{c}°{ce}={rc}°{re}\n{xx}")
       #CELCIUS KE FAHRENHEIT
       elif a=="2":
         print(ksd,ce,"ke",fa)
         c=int(input(sdc))
         fc=(9/5)*c+32  
         print(f"{c}°{ce}={fc}°{fa}\n{xx}")
           
       #CELCIUS KE KELVIN
       elif a=="3":
          print(ksd,ce,"ke",ke)
          c=int(input(sdc))
          kc=c+273
          print(f"{c}°{ce}={kc}°{ke}\n{xx}")

       #REAMUR KE CELCIUS
       elif a=="4":
          print(ksd,re,"ke",ce)
          r=int(input(sdr))
          cr=5/4*r
          print(f"{r}°{re}={cr}°{ce}\n{xx}")
       
       #REAMUR KE FAHRENHEIT
       elif a=="5":
          print(ksd,re,"ke",fa)
          r=int(input(sdr))
          fr=9/4*r+32
          print(f"{r}°{re}={fr}°{fa}\n{xx}")
          
       #REAMUR KE KELVIN
       elif a=="6":
          print(ksd,re,"ke",ke)
          r=int(input(sdr))
          kr=5/4*r+273
          print(f"{r}°{re}={kr}°{ke}\n{xx}")
       
       #FAHRENHEIT KE CELCIUS
       elif a=="7":
           print(ksd,fa,"ke",ce)
           f=int(input(sdf))
           cf=5/9*(f-32)
           print(f"{f}°{fa}={cf}°{ce}\n{xx}")
           
       #FAHRENHEIT KE REAMUR
       elif a=="8":
           print(ksd,fa,"ke",re)
           f=int(input(sdf))
           rf=(4/9)*(f-32)
           print(f"{f}°{fa}={rf}°{re}\n{xx}")
           
       #FAHRENHEIT KE KELVIN
       elif a=="9":
           print(ksd,fa,"ke",ke)
           f=int(input(sdf))
           kf=(f-32)*(5/9)+273
           print(f"{f}°{fa}={kf}°{ke}\n{xx}")
           
       #KELVIN KE CELCIUS
       elif a=="10":
           print(xx)
           print(ksd,ke,"ke",ce)
           k=int(input(sdk))
           ck=k-273
           print(f"{k}°{ke}={ck}°{ce}\n{xx}")
           
       #KELVIN KE FAHRENHEIT
       elif a=="11":
           print(ksd,ke,"ke",fa)
           k=int(input(sdk))
           fk=9/5*(k-273)+32          
           print(f"{k}°{ke}={fk}°{fa}\n{xx}")
           
       #KELVIN KE REAMUR
       elif a=="12":
           print(ksd,ke,"ke",re)
           k=int(input(sdk))
           rk=4/5*(k-273)
           print(f"{k}°{ke}={rk}°{re}\n{xx}")
      
      
    
    #KALKULATOR BANGUN DATAR
    def kbd():
        print(f"{xx}\n=•=•=•KALKUKATOR BANGUN RUANG=•=•=\n•")
    
    #KALKULATOR BANGUN RUANG
    def kbr():
        print(f"""{xx}\n=•=•=•KALKUKATOR BANGUN DATAR=•=•=•
1.persegi/persegi panjang
2.lingkaran
3.segitiga""")
        a=input("=»»")
        if a=="1":
            o=input("=•=•=•KALKULATOR PERSEGI/PERSEGI PANJANG=•=•=•\n1.luas..\n2.keliling\n=»»")
            if o=="1":
               print("=•=•=•MENGHITUNG LUAS PERSEGI/PERSEGI PANJANG=•=•=•")
               p=int(input(P))
               l=int(input(L))
               Rumus=p*l
               print(f"JIKA PANJANG={p} DAN LEBAR={l} MAKA:\n{p}×{l}={Rumus}")
            if o=="2":
                pass
            if o=="3":
                pass
            
            
        elif a=="2":
            pass
        elif a=="3":
            pass
    #KALKULATOR INVESTASI
    def ki():
        print(f"{xx}\n=•=•=•KALKUKATOR INVESTASI=•=•=•\nPILIH SALAH SATU DARI LIST BERIKUT\n1.keuntungan dalam persen\n2.Harga saham sesuai return yang di inginkan")
        y=input("»»»")
        if y=="1":
            a=int(input(f"{x}\nMASUKAN HARGA SAHAM PADA SAAT PERTAMA KALI BELI: "))
            b=int(input("DEVIDEN YANG DI DAPAT: "))
            c=b/a*100
            print(f"jika harga saham {a} dan deviden yang di dapat {b}\nmaka return yang di dapat sebesar\n{c} persen")
            
        elif y=="2":
            print(f"'{x}\nHARGA SAHAM YANG COCOK SESUAI RETURN YANG KAMU INGINKAN'")
            a=int(input("MASUKAN DEVIDEN SEBUAH PERUSAHAAN: "))
            b=int(input("MASUKAN RETURN YANG DIINGIKAN: "))
            c=a*100/b
            print(xx)
            print(f"maka rekomendasi harga saham yang cocok buat kamu \njika deviden tahun lalu sebesar {a}\ndan return yang anda inginkan sebesar {b} persen\n= RP.{c}")
        
    #FORMULA KEUANGAN
    def kfk():
        print(f"{xx}\n=•=•=•KALKUKATOR FORMULA KEUANGAN=•=•=•")
        a=int(input("MASUKAN JUMLAH PENGHASILAN: Rp."))
        print("FORMULA 5%,20%,25%,50%")
        def Xc():
            b=(input("jika setuju y jika tidak n= "))
            if b=="n":
                def Lx():
                   a1=int(input("BERAPA PERSEN KEBUTUHAN PRIMER MU? "))
                   a2=int(input("BERAPA PERSEN UNTUK HIBURAN? "))
                   a3=int(input("BERAPA PERSEN UNTUK INVESTASI? "))
                   a4=int(input("BERAPA PERSEN UNTUK SEDEKAH? "))
                   a11=a*a1/100
                   a22=a*a2/100
                   a33=a*a3/100
                   a44=a*a4/100
                   a55=(a1/100)+(a2/100)+(a3/100)+(a4/100)
                   if a55==1:
                      print(f"JIKA PENGHASILANMU ={a}\nMAKA UNTUK KEBUTUHAN Primer =Rp.{a11}\nSENANG SENANG=Rp.{a22}\nINVESTASI =Rp.{a33}\nDAN BERBAGI=Rp.{a44}") 
                   else:
                       Lx()
                Lx()
                   
                
            elif b=="y":
                a1=a*5/100
                a2=a*20/100
                a3=a*25/100
                a4=a*50/100
                print(f"JIKA PENGHASILANMU ={a}\nMAKA UNTUK KEBUTUHAN Primer =Rp.{a4}\nSENANG SENANG=Rp.{a2}\nINVESTASI =Rp.{a3}\nDAN BERBAGI=Rp.{a1}")
                
        Xc()



#TAMPILAN
for i in range(100):
    print(x)
    print("=•=•=•KALKULATOR SEDERHANA•=•=•=")
    print(f"{xx}\n1. konversi suhu\n2. bangun datar\n3. bangun ruang\n4. investasi\n5. Formula keuangan")
    A=input("PILIH JENIS KALKULATOR: ")
    if A=="1":
        Ks.kks()
        print(xxx)
    elif A=="2":
        Ks.kbd()
        print(xxx)
    elif A=="3":
        Ks.kbr()
        print(xxx)
    elif A=="4":
        Ks.ki()
        print(xxx)
    elif A=="5":
        Ks.kfk()
        print(xxx)
    else:
        print(f"{xxx}{x}")

sdc= "suhu dalam satuan celcius= "
sdk="suhu dalam satuan kelvin= "
sdf="suhu dalam satuan fahrenheit= "
sdr="suhu dalam satuan reamur= "
ksd="konversi suhu dari"
ke="kelvin"
re="reamur"
ce="celcius"
fa="fahrenheit"
xx="="*10+"#"*3+"="*10
xxx="="*10+"#"*3+"SELESAI"+"#"*3+"="*10
print("KALKULATOR KONVERSI SUHU")
print(xx)
n= "\n\n\n\n\n"
class KS():
    #kelvin
    def ck():
        print(ksd,ke,"ke",ce)
        k=int(input(sdk))
        ck=k-273
        print(k,"°",ke,"=",ck,"°",ke)
    def rk():
        print(ksd,ke,"ke",re)
        k=int(input(sdk))
        rk=4/5*(k-273)
        print(k,"°",ke,"=",rk,"°",re)
    def fk():
        print(ksd,ke,"ke",fa)
        k=int(input(sdk))
        fk=9/5*(k-273)+32
        print(k,"°",ke,"=",fk,"°",fa)

    #fahrenheit
    def cf():
        print(ksd,fa,"ke",ce)
        f=int(input(sdf))
        cf=5/9*(f-32)
        print(f,"°",fa,"=",cf,"°",ce)

    def kf():
        print(ksd,fa,"ke",ke)
        f=int(input(sdf))
        kf=(f-32)*(5/9)+273
        print(f,"°",fa,"=",kf,"°",ke)

    def rf():
        print(ksd,fa,"ke",re)
        f=int(input(sdf))
        rf=(4/9)*(f-32)
        print(f,"°",fa,"=",rf,"°",re)

    #reamur
    def cr():
        print(ksd,re,"ke",ce)
        r=int(input(sdr))
        cr=5/4*r
        print(r,"°",re,"=",cr,"°",ce)

    def kr():
        print(ksd,re,"ke",ke)
        r=int(input(sdr))
        kr=5/4*r+273
        print(r,"°",re,"=",kr,"°",ke)

    def fr():
        print(ksd,re,"ke",fa)
        r=int(input(sdr))
        fr=9/4*r+32
        print(r,"°",re,"=",fr,"°",fa)

    #celcius
    def fc():
        print(ksd,ce,"ke",fa)
        c=int(input(sdc))
        fc=(9/5)*c+32
        print(c,"°",ce,"=",fc,"°",fa)

    def kc():
        print(ksd,ce,"ke",ke)
        c=int(input(sdc))
        kc=c+273
        print(c,"°",ce,"=",kc,"°",ke)

    def rc():
        print(ksd,ce,"ke",re)
        c=int(input(sdc))
        rc=4/5*c
        print(c,"°",ce,"=",rc,"°",re)

            
def x():
    a=input("""pilih jenis kalkulator konversi
1=celcius ke reamur
2=celcius ke fahrenhiet
3=celcius ke kelvin
4=reamur ke celcius
5=reamur ke fahrenheit
6=reamur ke kelvin
7=fahrenheit ke celcius
8=fahrenheit ke reamur
9=fahrenheit ke kelvin
10=kelvin ke celcius
11=kelvin ke fahrenheit
12=kelvin ke reamur
=» """)
    if a=="1":
        print(xx)
        KS.rc()
        print(xxx,n)
        x()
    elif a=="2":
        print(xx)
        KS.fc()
        print(xxx,n)
        x()
    elif a=="3":
        print(xx)
        KS.kc()
        print(xxx,n)
        x()
    elif a=="4":
        print(xx)
        KS.cr()
        print(xxx,n)
        x()
    elif a=="5":
        print(xx)
        KS.fr()
        print(xxx,n)
        x()
    elif a=="6":
        print(xx)
        KS.kr()
        print(xxx,n)
        x()
    elif a=="7":
        print(xx)
        KS.cf()
        print(xxx,n)
        x()
    elif a=="8":
        print(xx)
        KS.rf()
        print(xxx,n)
        x()
    elif a=="9":
        print(xx)
        KS.kf()
        print(xxx,n)
        x()
    elif a=="10":
        print(xx)
        KS.ck()
        print(xxx,n)
        x()
    elif a=="11":
        print(xx)
        KS.fk()
        print(xxx,n)
        x()
    elif a=="12":
        print(xx)
        KS.rk()
        print(xxx,n)
        x()    
    else:
     print(f"masukin yang bener dong pp{na} {s}")
     print(xxx,n)
     x()
x()

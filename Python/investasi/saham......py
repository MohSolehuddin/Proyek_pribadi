ax="=•"*10
aaa="\n"*10
for i in range(1000):
    print(ax+ax)
    print("KALKULATOR TREDING")
    feebeli=0.0015
    feejual=0.0025
    BEI=0.000043
    Hbps=int(input("HARGA BELI PERSAHAM? : "))
    Hjps=int(input("HARGA JUAL PERSAHAM? : "))
    lot=100
    jl=int(input("JUMLAH LOT?          : "))
    x=lot*jl
    z=x*Hbps
    a=x*Hjps*(1-feejual)-z
    print(ax)
    print(f"HARGA TOTAL SAHAM    :{z}")
    print(f"TOTAL ASET           : {z*(1-feebeli)}\n{ax}")
    print(f"KEUNTUNGAN SEBESAR   :Rp.{   a}\n{ax+ax}{aaa}")
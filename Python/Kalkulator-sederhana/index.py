A="="*15+"###"+"="*15
B="="*10+"###"+"="*10
C="="*5+"#SELESAI#"+"="*5
BR="""ketik 01 untuk mencari volume
ketik 02 untuk mencari luas permukaan
= """
BD="""ketik 01 untuk mencari luas
ketik 02 untuk mencari keliling
= """
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
K="kalkulator"
Tt="tabung"
print(A)
print("""cpilih jenis kalkulator...
ketik 1 untuk kalkulator bangun datar
dan ketik 2 untuk bangun ruang
""")
a=input(f"pilih jenis {K} ? ")
if a=="2":
    print("="*14,"###","="*14)
    print(K,"bangun ruang...")
    print("""
    ketik 01 jika balok/kubus
    ketika 02 jika tabung
    ketik 00 untuk bangun ruang lainnya
    """)
    xxx=input("pilih jenis bangun ruang= ")
    if xxx=="01":
          print(B)
          print(K,V,Ku,"...")
          op=input(BR)
          if op=="01":
              print(B)
              print(M,V,Ku)
              p=int(input(P))
              l=int(input(L))
              t=int(input(T))
              h=p*l*t
              print(V,Ku+"=")
              print(p,"×",l,"×",t,"=",h)
              print(C)
          elif op=="02":
              print(B)
              print(M,LPe,Ku)
              p=int(input(P))
              l=int(input(L))
              t=int(input(T))
              h=p+l+t+p+t+l
              print(LPe,Ku,+"=")
              print("2×","(",p,"+",l,"+",t,")","=",h)
              print(C)
    elif xxx=="02":
          print(B)
          print(K,Tt+"...")
          vb=input(BR)
          if vb=="01":
              print(B)
              print(M,VT)
              n=input(π)
              if n=="22/7":
                r=int(input(R))
                t=int(input(T))
                print(ππ)
                h=22/7*r*r*t
                print(LL)
                print("22/7 ×",r,"×",r,"×",t,"=",h)
              elif n=="3.14": 
                r=int(input(R))
                t=int(input(T))
                print(πg)
                h=3.14*r*r*t
                print(LL)
                print("3.14 ×",r,"+",r,"×",t,"=",h)
                print(C)
          elif vb=="02":
              print(B)
              print(M,LPe,Tt)
              n=input(π)
              if n=="3.14":
                  r=int(input(R))
                  t=int(input(T))
                  l=3.14*(r+r)
                  z=l*t
                  a=3.14*r*r
                  print(πg)
                  h=a+a+z
                  print(LPe,Tt+"=")
                  print("2 × 3.14 ×",r,"×",r,"+ 3.14×",r+r,"=",h)
                  print(C)
              elif n=="22/7":
                  r=int(input(R))
                  t=int(input(T))
                  l=22/7*(r+r)
                  z=l*t
                  a=22/7*r*r
                  print(ππ)
                  h=a+a+z
                  print(LPe,Tt+"=")
                  print("2 × 22/7 ×",r,"×",r,"+ 22/7 ×",r+r,"=",h)
                  print(C)
    elif xxx=="00":
        print("udah segini aja dulu...")
elif a=="1":
    print("="*14,"###","="*14)
    print(K,"bangun datar...")
    print("""
    ketik 11 untuk persegi
    ketika 22 untuk segitiga
    ketik 33 untuk lingkaran
    """)
    b=input("pilih jenis bangun datar?")
    if b=="33":
         print(B)
         print(K,"persegi ...")
         cc=input(BD)
         if cc=="k":
             print(B)
             print(M,KL)
             n=input(π)
             if n=="22/7": 
               r=int(input(R))
               print(ππ)
               h=22/7*(r+r)
               print(LL)
               print("22/7","×","(",r,"+",r,")","=",h)
             elif n=="3.14": 
               r=int(input(Rt))
               print(πg)
               h=3.14*(r+r)
               print(LL)
               print("3.14","×","(",r,"+",r,")","=",h)
               print(C) 
         elif cc=="l":
             print(B)
             print(M,LL)
             n=input(π)
             if n=="22/7": 
               r=int(input(R))
               print(ππ)
               h=22/7*r*r
               print(LL)
               print("22/7","×",r,"×",r,"=",h) 
             elif n=="3.14": 
               r=int(input(R))
               print(πg)
               h=3.14*r*r
               print(LL)
               print("3.14","×",r,"×",r,"=",h)
               print(C)
    elif b=="22":
         print(B)
         print(K,"persegi ...")
         se=input(BD)
         if se=="02":
             print(B)
             print(M,LS+"= ")
             p=int(input(P))
             t=int(input(L))
             s=1/2*p*t
             print(LS+"=")
             print("1/2","×",p,"x",t,"=",s)
             print(C)
         elif se=="01":
             print(B)
             print(M,KS)
             s=int(input("sisi1: "))
             ss=int(input("sisi2: "))
             sss=int(input("sisi3: "))
             sh=s+ss+sss
             print(KS,"=")
             print(s,"+",ss,"+",sss,"=",sh)
             print(C)
    elif b=="11":
         print(B)
         print(K,"persegi ...")
         k=input(BD)
         if k=="01":
              print(B)
              print(M,LP+"= ")
              p=int(input(P))
              l=p=int(input(L))
              h=p*l
              print(LP,"/"+PP+"=")
              print(p,"×",l,"=",h)
              print(B)
         elif k=="02":
              print(B)
              print(KL+"= ")
              p=int(input(P))
              l=int(input(L))
              x=p*l
              print(M,KL+"= ")
              print("2 ×(",p,"+",l,")=",x)
              print(C)

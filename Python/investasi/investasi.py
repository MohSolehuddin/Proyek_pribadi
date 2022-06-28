x="=×"*25
xx="=•"*15
for i in range(1000):
    print(f"{x}\n=•=•=•KALKULATOR INVESTASI=•=•=•")
    nama=input("NAMA: ")
    print(xx)
    print(f"{nama} PILIH SALAH SATU DARI LIST BERIKUT\n1.keuntungan dalam persen\n2.Harga saham sesuai return yang di inginkan")
    y=input(f"SILAHKAM DIPILIH {nama}: ")
    if y=="1":
        print(x)
        a=int(input("MASUKAN HARGA SAHAM PADA SAAT PERTAMA KALI BELI: "))
        b=int(input("DEVIDEN YANG DI DAPAT: "))
        c=b/a*100
        print(f"jika harga saham {a} dan deviden yang di dapat {b}\nmaka return yang di dapat sebesar\n{c} persen\n")
    elif y=="2":
        print(x)
        print(f"'HARGA SAHAM YANG COCOK SESUAI RETURN YANG {nama} INGINKAN'\n")
        a=int(input("MASUKAN DEVIDEN SEBUAH PERUSAHAAN: "))
        b=int(input("MASUKAN RETURN YANG DIINGIKAN: "))
        c=a*100/b
        print(xx)
        print(f"maka rekomendasi harga saham yang cocok buat {nama}\njika deviden tahun lalu sebesar {a}\ndan return yang anda inginkan sebesar {b}\n= {c}\n")
        if b<6:
            print('"SAHAM DI KATAKAN MURAH JIKA RETURN NYA DI ATAS 6 PERSEN"')

s="=•"*15
x="\n\n\n"
for i in range(100):
    print(s)
    print("=•=•=•=JADWAL PELAJARAN=•=•=•=")
    a=input("""\nMASUKAN HARI....
1.jika hari senin
2.jika hari selasa
3.jika hari rabu
4.jika hari kamis
5.jika hari jum'at
=»»: """)
    if a=="1":
        print(s)
        print(f"""{s}SENIN:
        PKN
        SENI BUDAYA
        SK{s}{x}""")
    elif a=="2":
        print(s)
        print(f"""{s}SELASA:
        DDG
        kJD
        B.inggris{s}{x}""")    
    elif a=="3":
        print(s)
        print(f"""{s}RABU:
        BADAR
        MATEMATIKA
        SIMDIG
        FISIKA{s}{x}""")    
    elif a=="4":
        print(s)
        print(f"""{s}KAMIS:
        SEJARAH INDONESIA
        KIMIA
        PAI{s}{x}""")
    elif a=="5":
        print(s)
        print(f"""{s}JUM'AT:
        PEMROGRAMAN DASAR
        B. INDONESIA
        BP
        PJOK{s}{x}""")
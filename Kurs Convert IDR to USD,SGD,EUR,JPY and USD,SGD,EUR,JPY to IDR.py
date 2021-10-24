def loops ():
    def menu():
        print('Masukkan mata uang yang ingin anda konversikan')
        print ('1. Rupiah to USD')
        print ('2. Rupiah to SGD')
        print ('3. Rupiah to EUR')
        print ('4. Rupiah to JPY')
        print ('5. USD to Rupiah')
        print ('6. SGD to Rupiah')
        print ('7. EUR to Rupiah')
        print ('8. JPY to Rupiah')
        

    def Rupiah_to_USD ():
        Rupiah = int(input('masukkan uang anda dalam bentuk rupiah = Rp.'))
        Konversi_ke_usd = Rupiah/14120
        print('USD = US$',Konversi_ke_usd)

    def Rupiah_to_SGD ():
        Rupiah = int(input('masukkan uang anda dalam bentuk rupiah = Rp.'))
        Konversi_ke_sgd = Rupiah/10488
        print('SGD = S$',Konversi_ke_sgd)

    def Rupiah_to_EUR ():
        Rupiah = int(input('masukkan uang anda dalam bentuk rupiah = '))
        Konversi_ke_eur = Rupiah/16437
        print('EUR = €',Konversi_ke_eur)

    def Rupiah_to_JPY ():
        Rupiah = int(input('masukkan uang anda dalam bentuk rupiah = '))
        Konversi_ke_jpy = Rupiah/124
        print('JPY = ¥',Konversi_ke_jpy)

    def USD_to_Rp ():
        USD =float(input('Masukan jumlah Dollar US = US$ '))
        Konversi_ke_USD_TO_Rp = USD*14120
        print('Rp = Rp.',Konversi_ke_USD_TO_Rp)

    def SGD_to_Rp ():
        SGD =float(input('Masukkan jumlah Dollar SG = S$'))
        Konversi_ke_SGD_TO_Rp = SGD*16437
        print('Rp = Rp.',Konversi_ke_SGD_TO_Rp)

    def EUR_to_Rp ():
        EUR =float(input('Masukkan jumlah EURO = €'))
        Konversi_ke_EUR_TO_Rp = EUR*10488
        print('Rp = Rp.',Konversi_ke_EUR_TO_Rp)

    def JPY_to_Rp ():
        JPY =float(input('Masukkan jumlah Japan Yen = ¥'))
        Konversi_ke_JPY_TO_Rp = JPY*124
        print('Rp = Rp.',Konversi_ke_JPY_TO_Rp)

    menu()
    #program

    print ('KONVERSI RUPIAH KE MATA UANG ASING')
    print ('-----------------------------------')

    pilih = int(input('Masukkan Pilihan anda = '))
    if pilih == 1:
        Rupiah_to_USD ()
    elif pilih == 2:
        Rupiah_to_SGD ()
    elif pilih == 3:
        Rupiah_to_EUR ()
    elif pilih == 4:    
        Rupiah_to_JPY ()
    elif pilih == 5:
        USD_to_Rp ()
    elif pilih == 6:
        SGD_to_Rp ()
    elif pilih == 7:
        EUR_to_Rp ()
    elif pilih == 8:
        JPY_to_Rp ()
    else:
        print('Pilihan tidak valid')

    x = str(input("Apakah masih ingin menggunakan lagi? Yes/No = "))
    while x:
        if x == "Yes":
            loops()
        else:
            print("Terima Kasih")
        break
loops()

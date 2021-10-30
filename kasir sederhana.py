def loops ():
    def Menu ():
         print("""
                ==============================
                Kilo kopi
                List Menu Minuman Kopi 
                ==============================
                'Americano': Rp. 18.000
                'LongBlack': Rp. 18.000
                'V60': Rp. 16.000
                'Syphon': Rp. 20.000
                'Affogato': Rp. 20.000

                Promo spesial :  setiap hari Jum'at mendapatkan Diskon sebesar 20%
                                setiap hari minggu mendapatkan Diskon sebesar 10%
                """)
    
    def program():
        x = {
        'Americano': 18000,
        'LongBlack': 18000,
        'V60': 16000,
        'Syphon': 20000,
        'Affogato': 20000
        }
        y=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
        pesanan = str(input("Masukkan Nama Pesanan = "))
        jp = int(input('Masukkan Jumlah Pesanan = '))
        hari= str(input('Masukkan Hari pembelian = '))
        harga =x[pesanan]
        ht = harga * jp
        if hari == y[0]:
            ht
        elif hari == y[1]:
            ht
        elif hari == y[2]:
            ht
        elif hari == y[3]:
            ht
         
        elif hari == y[4]:
            diskon = ht*0.2

        elif hari == y[5]:
            ht
        elif hari == y[6]:
            diskon = ht*0.1
        else:   
            print('Menu tidak tersedia') 
        print('======================================================')
        print('                      Kilo Kopi                       ')
        print('======================================================')   
        print("Menu :",pesanan)
        print('Harga Satuan', harga)
        print('Harga Total',ht)
        print("Diskon :",diskon)
        print("Jumlah Pesan :", jp)
        print("==========================")
        print("Jumlah Bayar :", ht-diskon)
        print("==========================")
        z = str(input("Apakah masih ingin menggunakan lagi? Yes/No = "))
        while z:
                if z == "Yes":
                    loops()
                else:
                    print("Terima Kasih")
                break
    Menu()
    program()
        
loops()

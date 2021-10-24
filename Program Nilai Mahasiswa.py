def loops ():
    print('-----------------')
    print("Program Nilai MAHASISWA")
    print('-----------------')

#var inputan
    Nama=str(input('Masukkan nama Mahasiswa = '))
    NIM=int(input('Masukkan NIM Mahasiswa = '))
    Prodi=str(input('Masukkan prodi Mahasiswa = '))
    Total_Nilai_tugas=int(input("Masukkan Rata Rata Nilai Tugas = "))
    Total_Nilai_quiz=int(input('Mauskkan Rata Rata Nilai Quiz = '))
    Total_Nilai_UTS_atau_UAS=int(input('Masukkan Rata Rata Nilai UTS = '))

#Proses ngitung Bobot Nilai
    Bobot_Nilai_Tugas=float((Total_Nilai_tugas)*25/100)
    Bobot_Nilai_Quiz=float((Total_Nilai_quiz)*25/100)
    Bobot_Nilai_UTS_dan_UAS=float((Total_Nilai_UTS_atau_UAS)*50/100)
    Nilai_Akhir=float((Bobot_Nilai_Quiz+Bobot_Nilai_Tugas+Bobot_Nilai_UTS_dan_UAS)/3)

#List
    print('-----------------')
    print("Nilai MAHASISWA")
    print('-----------------')
    x = [Nama,NIM,Prodi,Bobot_Nilai_Tugas,Bobot_Nilai_Quiz,Bobot_Nilai_UTS_dan_UAS,Nilai_Akhir]
    print("Nama             : ", x[0])
    print("NIM              : ", x[1])
    print("Program Studi    : ", x[2])
    print("Rata Rata Nilai Tugas      : ", x[3])
    print("Rata Rata Nilai Quiz       : ", x[4])
    print("Rata Rata Nilai UTS        : ", x[5])
    print("Nilai Akhir      : ", x[6])

#looping
    y = str(input("Apakah masih ingin menggunakan lagi? Yes/No = "))
    while y:
        if y == "Yes":
            loops()
        else:
            print("Terima Kasih")
        break
loops()

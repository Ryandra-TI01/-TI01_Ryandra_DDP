#soal no 1
def profil(nama,alamat,gender,umur,hobby):
    print('nama :',nama)
    print('alamat :',alamat)
    print('gender',gender)
    print('umur :',umur)
    print('hobby :',hobby)
    
profil('Ryandra','depok','pria',18,'main game')

#soal no 2
def nilai(nilai):
    if(nilai <= 60):
        print('gagal')
    elif(nilai >= 60 and nilai <= 70):
        print('baik')
    elif(nilai >= 71 and nilai <= 80):
        print('sangat baik')
    elif(nilai >= 81 and nilai <= 100):
        print('istimewa')
    else:
        print('masukan nilai anda !')
nilai(60)

#soal no 3
def ganjil(value):
    for i in range(value):
        if(i %2 != 0):
            print(i, end=' ')
ganjil(100)



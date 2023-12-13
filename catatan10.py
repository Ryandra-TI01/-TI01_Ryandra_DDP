a = [1,2,3,4,5]
a.append(6) #menambakan isi pada akhir list
a.insert(2,100) # menambahkan isi sesuai index dengan paramater ke 1 index dan parameter ke 2 isi nya
a.pop(2) # menghapus isi pada akhir array atau list bisa juga dengan index
a.remove(1) # menghapus isi list dengan value bukan dengan index
print(a)


#tipe data set
nama = {'anton','ari','menma'} 
angka = {2,4,8,1,10,3,5,7,6,11,15,20,29,}
print(nama)
print(angka)

#tipe data set
nullSet = set()
nullSet.add('biji') #menambahkan data ke dalam set
print(nullSet)

#memindahkan tipe data set ke list
baruBanget=[]
for baru in nama:
    baruBanget.append(baru)
print(baruBanget)

#menggabungkan set 1 dengan set 2 pada tipe data set
set1 = {1,2,3,4,5}
set2 = {10,9,6,7}
set3 = set1.union(set2) #menggabungkan set 1 dengan set 2
# print(set3)
set1.update(set2) #menambahkan set 1 dengan set 2
print(set1)

#tipe data disctionary
mahasiswa = {
    'Nsiswa' : 'ryandra',
    'nim' : 110223013,
    "hobi" : ['membaca','mencuri','menyolong'],
    'mhs' :{
        'Niswa' : 'ryandra',
        'im' : 110223013,
        "obi" : ['membaca','mencuri','menyolong'],
        "namaaa" : {
            "andra":"ganteng",
            "satria" : " satria bau"
        }
    }
}
print(mahasiswa['mhs']["namaaa"]["satria"])
print(mahasiswa["hobi"][1])
mahasiswa['nim'] = 2
print(mahasiswa['nim'])
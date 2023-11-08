#no 1
InputKendaraan = input ("Nama kendaraan ? contoh : {mobil, motor}")
InputBensin = input ("Jenis bensin ?")
InputKota = input ("Kota yang di tuju?")
match InputBensin:
    case "Pertalite":
        jarakT = 12
        perliter = 10000
    case "Pertamax":
        jarakT = 13
        perliter = 14000
    case "Pertamax Turbo":
        jarakT = 13.5
        perliter = 17000
    case _:
        print("masukan input sesuai pesanan!") 
match InputKota:
    case"Jakarta":
        jarak = 20
    case"Bekasi ":
        jarak = 35.7
    case"Depok":
        jarak = 5
    case"Tangerang":
        jarak = 99
    case"Bogor ":
        jarak = 120.6
    case _:
        print("masukan input sesuai pesanan!") 
Pbensin = round(jarak /  jarakT,2)
Hbensin = round(Pbensin *  perliter,2)
print("\n\n-----------------------")
print("Nama Kendaraan =",InputKendaraan)
print("Jenis Bensin =",InputBensin)
print("Kota yang dituju =",InputKota)
print("Pemakaian bensin? =",Pbensin,"liter")
print("Total Harga dari Bensin? = Rp.",Hbensin)




# no 2
InputNama = input ("Masukan nama pembeli?")
InputNo = input ("Masukan no hp pembeli?")
InputPesanan1 = input ("Pesan Menu Apa?(makanan atau minuman)")

match InputPesanan1:
    case "makanan":
        print("MENU MAKANAN\n\n1.Nasi goreng = Rp.15.000\n2.Mie Goreng = Rp.12.000\n3.Ayam Geprek = Rp.18.000")
    case "minuman":
        print("1.Aneka Jus = Rp.15.000\n2.Soft Drink = Rp.10.000\n3.Sweet Ice Tea = Rp.5.000")
    case _:
        print("masukan input sesuai pesanan!") 
InputPesanan2 = input("Masukan Pesanan?")
InputJumlahPesanan = int (input("Masukan Jumlah Pesanan?"))
if (InputPesanan2 =="1"):
    harga = 15000
    Mdipesan = "Nasi goreng"
elif(InputPesanan2 =="2"):
    harga = 12000
    Mdipesan = "Mie Goreng"
elif(InputPesanan2 =="3"):
    harga = 18000
    Mdipesan = "Ayam Geprek"
elif (InputPesanan2 =="1"):
    harga = 15000
    Mdipesan = "Aneka Jus"
elif(InputPesanan2 =="2"):
    harga = 10000
    Mdipesan = "Soft Drink"
elif(InputPesanan2 =="3"):
    harga = 5000
    Mdipesan = "Sweet Ice Tea"
else:
    harga = "masukan input sesuai pesanan!"

print("\n\n--------------------------------------------------------")
print("Keterangan Pemesanan\n")
print("Nama Pembeli = ",InputNama)
print("No Hp Pembeli =",InputNo)
print("Menu yang di Pesan =",Mdipesan)
print("Jumlah pesanan =",InputJumlahPesanan)
a = harga * InputJumlahPesanan
b = f"{a:,}"
print("Harga yang harus dibayarkan = Rp",b)

# no 3
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)
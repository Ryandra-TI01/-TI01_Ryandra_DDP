# pelanggan = "budi"
# totalbelanja = 50000

# if(totalbelanja > 100000):
#     keterangan = "selamat dapat duit"

# else:
#     keterangan = "thanks"

# print("pelanggan",pelanggan,"\n","Total belanja anda Rp.",totalbelanja,"\n",keterangan)

nama = "Ryandra Athaya Saleh"
matkul = "matkom"
nilai = 70

# keterangan = "lulus" if nilai >= 60 else "gagal"

# print("Nama siswa \t:",nama,
#     "\nMata kuliah \t:",matkul,
#     "\nnilai \t\t:",nilai,
#     "\nKeterangan \t:",keterangan
#     )

if (nilai >= 85 and nilai <= 100):
    grade = "A"
elif (nilai >= 75 and nilai <= 85):
    grade = "B"
elif (nilai >= 60 and nilai <= 75):
    grade = "C"
elif (nilai >= 30 and nilai <= 60):
    grade = "D"
else:
    grade = "e"
print("siswa",nama,"mendapatkan","grade \t:",grade)
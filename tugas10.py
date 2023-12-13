# NO 1
def lulus(hasil_akhir):
    SiswaLulus = [siswa['nama'] 
    for siswa in hasil_akhir if siswa['nilai'] > 65]
    return SiswaLulus

hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]
print("Hasil siswa yang Lulus :", lulus(hasil_akhir))


# # NO 2
buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def BuahTerbalik(terbalik):
    panjang = len(terbalik)
    hasil = [''] * panjang
    for i in range(panjang):
        hasil[panjang - i - 1] = terbalik[i]
    return hasil

print("Hasil Terbalik:", BuahTerbalik(buah_asli))

# # NO 3
buah1 = ['pepaya','mangga','pisang','durian','jambu']
def BuahDuplikasi(buah1):
    hasil = []
    for buah in buah1:
        hasil.append(buah)
        hasil.append(buah)
    return hasil

print("Hasil Duplikasi:", BuahDuplikasi(buah1))

# # NO 4
A = "Nurul Fikri"
def konsonan(A):
    konsonan = ""
    for karakter in A:
        if karakter not in ['a','e','i','o','u']:
            konsonan += karakter                   
    return konsonan         


HasilKonsonan = konsonan(A)

print("Huruf konsonan :", HasilKonsonan)
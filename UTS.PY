#Program keliling dan luas layang-layang
print("program mencari keliling dan luas layang-layang\n")
d1 = int(input("masukan diagonal 1 :" ))
d2 = int(input("masukan diagonal 2 :"))
p1 = int(input("masukan panjang 1 :"))
p2 = int(input("masukan panjang 2 :"))

keliling = 2*(p1+p2)
luas = (d1*d2)/2

print("Keliling layang-layang = ",keliling)
print("Luas layang-layang = ",luas)

# 
print("Program membuat kalkulator sederhana")

input1 = int(input("Masukan angka 1 :"))
input2 = int(input("Masukan angka 2 :"))

print("Pilih operator")
operator = input("operator keterangan\n  +\t tambah\n  -\t kurang\n  /\t bagi\n  *\t kali\n  **\t pangkat\n Masukan operator :")
match operator :
    case "tambah":
        hasil = input1 + input2
        hasil1 = "+"
    case "kurang":
        hasil = input1 - input2
        hasil1 = "-"
    case "bagi":
        hasil = input1 / input2
        hasil1 = "/"
    case "kali":
        hasil = input1 * input2
        hasil1 = "X"
    case "pangkat":
        hasil = input1 ** input2
        hasil1 = "**"
    case _:
        print("masukan angka atau opertaor yang sesuai")
print("angka pertama :",input1)        
print("angka kedua :",input2)
print("Pilihan operator :",operator)
print(f"hasil operator {input1 }{hasil1}{ input2}={hasil}")
        
    
    
    

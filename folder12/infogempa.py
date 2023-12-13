from gempa import *

kota1 = Gempa('Banten',1.2)
kota2 = Gempa('Palu',6.1)
kota3 = Gempa('Cianjur',5.6)
kota4 = Gempa('Jayapura',3.3) 
kota5 = Gempa('Garut',4.0)
print('gempa pertama di',kota1.lokasi,'skala',kota1.skala,kota1.dampak())
print('gempa pertama di',kota2.lokasi,'skala',kota2.skala,kota2.dampak())
print('gempa pertama di',kota3.lokasi,'skala',kota3.skala,kota3.dampak())
print('gempa pertama di',kota4.lokasi,'skala',kota4.skala,kota4.dampak())
print('gempa pertama di',kota5.lokasi,'skala',kota5.skala,kota5.dampak())
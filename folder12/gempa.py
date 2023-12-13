class Bank:
#member1 variabel
    norek =''
    nama =''
    saldo = 0
    jmlNasabah = 0 # variabel static
    BANK = 'Bank Syariah Nurul Fikri' # variabel konstanta
#member2 konstruktor
def __init__(self,no,nasabah,saldo):
    self.norek = no
    self.nama = nasabah
    self.saldo = saldo
    Bank.jmlNasabah += 1
    
# member1  
class Gempa :
# member 2 konstruktor
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self):
        if self.skala < 2:
            impact = 'dampak gempa tidak berasa'
        elif self.skala >= 2 and self.skala <= 4:
            impact = 'dampak gempa bangunan retak-retak'
        elif self.skala > 4 and self.skala <= 6:
            impact = 'dampak gempa bangunan roboh'
        elif self.skala > 6:
            impact = 'dampak gempa bangunan roboh dan berpotensi tsunami'
        
        return impact


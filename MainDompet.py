from DompetDigital import Dompet
dompet1 = Dompet(250000, "Salman", "ID001")
dompet2 = Dompet(50000, "Gilang", "ID002") 
dompet3 = Dompet(75000, "Januar", "ID003")
dompet1.cek_saldo()
dompet1.topup(20000)
dompet1.transfer(30000, dompet2)
dompet1.tarik_tunai(20000)
dompet1.cek_saldo()
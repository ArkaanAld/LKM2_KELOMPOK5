class Dompet:
    def __init__(self,saldo, nama, id):
        self.saldo = saldo
        self.nama = nama
        self.id = id

    def topup(self, jumlah):
        self.saldo += jumlah
        print(f"Topup berhasil! Saldo Anda sekarang: {self.saldo}")
    def transfer(self, jumlah, penerima):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            penerima.saldo += jumlah
            print(f"Transfer berhasil! Saldo Anda sekarang: {self.saldo}")
        else:
            print("Saldo tidak cukup untuk melakukan transfer.")
    def cek_saldo(self):
        print(f"Saldo Anda saat ini: {self.saldo}")

    def tarik_tunai(self, jumlah):
            if self.saldo >= jumlah:
                self.saldo -= jumlah
                print(f"Tarik tunai berhasil! Saldo Anda sekarang: {self.saldo}")
            else:
                print("Saldo tidak cukup untuk melakukan tarik tunai.")
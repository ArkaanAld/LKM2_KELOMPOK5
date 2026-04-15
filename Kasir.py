class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok
    
class Keranjang:
  def __init__(self, member=True):
    self.daftar_barang = []
    self.member = member
  
  def tambah_produk(self, produk_baru, jumlah):
    if jumlah > produk_baru.stok:
      print(f"Stok {produk_baru.nama} tidak cukup. Stok tersedia: {produk_baru.stok}")
      return
    self.jumlah = jumlah
    self.daftar_barang.append(produk_baru)
    print(f"Berhasil menambah: {produk_baru.nama}")

  def hapus_produk(self, nama_produk):
    for barang in self.daftar_barang:
      if barang.nama == nama_produk:
        self.daftar_barang.remove(barang)
        barang.stok += 1
        print(f"{nama_produk} dihapus dari keranjang")
        return
    print("Barang tidak ditemukan di keranjang")
    
  def hitung_total(self):
        total = 0
        for item in self.daftar_barang:
            total += item["produk"].harga * item["jumlah"]
        return total
    
  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang.harga
    return total
  
  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
        print(f"- {barang.nama} : Rp{barang.harga}")
        
    self.total_akhir = self.hitung_total() 
    
    if self.total_akhir > 100000:
        diskon = self.total_akhir * 0.1
        print(f"Diskon (10%) \t: -Rp{diskon}")
        self.total_akhir -= diskon
        
    if self.member:
        diskon_member = self.total_akhir * 0.05
        print(f"Diskon Member (5%) \t: -Rp{diskon_member}")
        self.total_akhir -= diskon_member
        
    print(f"Total Akhir \t: Rp{self.total_akhir}")

  def bayar(self, jumlah_bayar):
    if jumlah_bayar < self.total_akhir:
      print(f"Uang tidak cukup. Tagihan Anda: Rp{self.total_akhir}")
    else:
      kembalian = jumlah_bayar - self.total_akhir
      print(f"Kembalian: Rp{kembalian}")
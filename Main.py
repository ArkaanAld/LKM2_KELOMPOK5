from Kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000, 10)
p2 = Produk("Susu UHT", 18000, 5)
p3 = Produk("Keyboard Gaming", 250000, 2)

# del p3

keranjang_saya = Keranjang()
keranjang_saya.tambah_produk(p1, 2)
keranjang_saya.tambah_produk(p2, 4)
keranjang_saya.tambah_produk(p3, 1)

keranjang_saya.cetak_struk()
keranjang_saya.bayar(500000)
keranjang_saya.hapus_produk("Susu UHT")
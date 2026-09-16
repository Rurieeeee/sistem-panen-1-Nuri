
# panen.py
def hitung_total_panen(jumlah_karung, berat_per_karung):
    return jumlah_karung * berat_per_karung

if __name__ == "__main__":
    karung = 10
    berat = 50
    total = hitung_total_panen(karung, berat)
    print(f"Total berat hasil panen: {total} kg")

def hitung_total_panen(jumlah, harga):
    return jumlah * harga

def hitung_diskon(total, persen):
    return total - (total * persen / 100)

jumlah = 100
harga = 5000

total = hitung_total_panen(jumlah, harga)
total_setelah_diskon = hitung_diskon(total, 10)

print("Total hasil panen: Rp", total)
print("Total setelah diskon: Rp", total_setelah_diskon)

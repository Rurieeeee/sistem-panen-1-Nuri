
# panen.py
def hitung_total_panen(jumlah_karung, berat_per_karung):
    return jumlah_karung * berat_per_karung

if __name__ == "__main__":
    karung = 10
    berat = 50
    total = hitung_total_panen(karung, berat)
    print(f"Total berat hasil panen: {total} kg")

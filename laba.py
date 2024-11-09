# Modal awal
modal_awal = 50000000
total_laba = 0

print("laba per bulan:")

# Menghitung laba per bulan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
       laba = 0 # bulan [pertama dan kedua belum ada laba 
    elif bulan == 3 or bulan == 4:
        laba = modal_awal * 0.01 # bulan ketiga dan keempat laba 1%
    elif bulan == 5 or bulan == 6:
       laba = modal_awal * 0.05 # bulan kelima dan keenam laba 5%
    elif bulan ==7:
       laba = modal_awal * 0.03 # bulan kedelepan laba turun menjadi 3R
    
    print(f"laba bulan ke-{bulan} sebesar: {laba}")
    total_laba += laba # menambahkan laba bulanan ke total laba

print (f"Total laba adalah: {total_laba}")
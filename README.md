# Program 1 Random
Program ini adalah program penghasil bilangan acak dengan batas tertentu

## Deskripsi Program
Program ini menggunakan bahasa Python untuk menghasilkan sejumlah bilangan acak yang lebih kecil dari 0.5. Program memanfaatkan beberapa fitur utama Python untuk mencapai tujuannya:
1. *Input Pengguna* :
   Program menggunakan fungsi input() untuk meminta pengguna memasukkan jumlah bilangan acak yang diinginkan (N). Nilai ini menentukan berapa banyak bilangan acak yang akan dihasilkan sesuai dengan syarat tertentu.
2. *Fungsi random() dari Modul random* :
   Program menggunakan modul bawaan Python, yaitu random, untuk menghasilkan bilangan acak. Fungsi random() dari modul ini menghasilkan angka desimal acak antara 0 dan 1.
3. *Looping dengan while* :
   Program menggunakan while loop untuk terus melakukan proses pengacakan hingga jumlah bilangan yang memenuhi syarat tercapai. Loop ini akan terus berjalan sampai kondisi tertentu (jumlah bilangan yang lebih kecil dari 0.5) terpenuhi.
4. *Kondisional dengan if* :
   Program menggunakan pernyataan if untuk memeriksa setiap bilangan acak yang dihasilkan. Jika bilangan tersebut kurang dari 0.5, maka program menambah penghitung count dan menampilkan bilangan tersebut. Jika tidak, program akan mengabaikannya dan melanjutkan ke bilangan acak berikutnya.
5. *Output yang Informatif*:
    Setiap bilangan yang memenuhi syarat akan ditampilkan ke layar bersama dengan urutan datanya, sehingga pengguna dapat melihat setiap hasil yang dihasilkan.
6. *Pesan Akhir* :
    Setelah jumlah bilangan yang sesuai tercapai, program menampilkan pesan “selesai” untuk memberi tahu pengguna bahwa proses telah berakhir.

## Kode Program Random
``` python
from random import random
# meminta input jumlah bilangan acak yang lebih kecil dari 0.5
n = int(input("masukan nilai N: "))
count = 0

# loop untuk menghasilkan dan menampilkan bilangan acak yang kurang dari 0.5
while count < n:
    num = random()
    if num < 0.5:
        count += 1
        print(f"data ke—{count} =>{num}") 
print("selesai")
```

## Output Random
```
PS C:\Users\user\Documents\Kuliah> & C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe c:/Users/user/Documents/Kuliah/lab2
py/pemrograman/lab3.py
masukan nilai N: 5
data ke-1 =>0.39068169304856226
data ke-2 =>0.31277006954653797
data ke-3 =>0.37396179813362496
data ke-4 =>0.39748276308643504
data ke-5 =>0.24127817287217124
selesai
PS C: \Users\user\Documents\Kuliah>
```

## Cara Kerja Program 1
1. *Meminta Input dari Pengguna* : program mulai dengan meminta pengguna memasukkan angka N, yaitu jumlah bilangan acak yang diinginkan (yang harus lebih kecil dari 0.5). Nilai N ini disimpan dalam variabel n.
2. *Menginisialisasi Variabel Penghitung* : Program menetapkan variabel count dengan nilai awal 0. Variabel ini akan digunakan untuk menghitung berapa banyak bilangan acak yang sudah memenuhi syarat (kurang dari 0.5).
3. *Memulai Perulangan* :
      - Program memasuki sebuah while loop, yaitu perulangan yang akan terus berjalan sampai count mencapai n (jumlah bilangan yang diminta oleh pengguna).
      - Setiap kali perulangan berjalan, program melakukan hal berikut:
        - Membuat Bilangan Acak : Program menghasilkan bilangan acak antara 0 dan 1 menggunakan fungsi random(). Bilangan acak ini disimpan dalam variabel num.
        - Memeriksa Syarat Bilangan Acak : Program mengecek apakah num kurang dari 0.5
          - *Jika ya (bilangan < 0.5), maka* :
             1. Program menambahkan count sebesar 1 (artinya, satu bilangan lagi yang memenuhi syarat sudah ditemukan).
             2. Program menampilkan bilangan tersebut ke layar, bersama dengan nomor urutnya.
          - *Jika tidak (bilangan ≥ 0.5)*, program akan mengabaikan bilangan tersebut dan melanjutkan ke bilangan acak berikutnya.
4. *Mengakhiri Program* : Perulangan akan terus berlanjut hingga count sama dengan n, artinya jumlah bilangan yang memenuhi syarat sudah terpenuhi.
Ketika kondisi ini tercapai, program keluar dari perulangan dan menampilkan pesan “selesai”.

*Jadi, program ini berfungsi untuk menghasilkan N bilangan acak yang nilainya kurang dari 0.5, dan akan berhenti setelah berhasil menemukan semua bilangan tersebut.*

## Program 2 Menghitung Laba Bulanan
program ini dirancang untuk menghitung dan menampilkan keuntungan (laba) yang dihasilkan dari modal awal dalam jangka waktu tertentu, dalam hal ini selama 8 bulan
## Deskripsi Program
Program ini menggunakan bahasa Python untuk menghitung laba bulanan dari sebuah modal awal yang diinvestasikan, dengan persentase laba yang berbeda tiap bulannya. Program ini memanfaatkan beberapa fitur utama Python untuk mencapai tujuannya:
1. *Deklarasi Variabel* :
    - Program mendefinisikan modal_awal dengan nilai 50.000.000, yang menunjukkan jumlah modal yang diinvestasikan.
    - Variabel total_laba diinisialisasi dengan nilai 0 dan digunakan untuk menyimpan akumulasi laba total selama 8 bulan.
2. *Perulangan dengan for* :
    - Program menggunakan for loop untuk menghitung laba per bulan selama 8 bulan. Perulangan for ini berjalan dari bulan pertama hingga bulan kedelapan.
Kondisi dengan if-elif
3. *Program memanfaatkan pernyataan if-elif untuk menentukan persentase laba yang berbeda tiap bulan* :
    - Bulan ke-1 dan ke-2: Tidak ada laba, jadi nilai laba diatur ke 0.
    - Bulan ke-3 dan ke-4: Laba 1% dari modal_awal.
    - Bulan ke-5 dan ke-6: Laba 5% dari modal_awal.
    - Bulan ke-7: Laba 3% dari modal_awal.
4. *Menampilkan dan Mengakumulasi Laba Bulanan* :
    - Setiap bulan, program menampilkan laba yang diperoleh dan juga menambahkan laba tersebut ke total_laba.
5. *Menampilkan Total Laba* :
    - Setelah loop selesai, program menampilkan jumlah total laba yang diperoleh selama 8 bulan.

## Kode Program Laba
``` python
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
```
## Output Program
```
py/pemrograman/laba.py
laba per bulan:
laba bulan ke-1 sebesar: 0
laba bulan ke-2 sebesar: 0
laba bulan ke-3 sebesar: 500000.0
laba bulan ke-4 sebesar: 500000.0
laba bulan ke-5 sebesar: 2500000.0
laba bulan ke-6 sebesar: 2500000.0
laba bulan ke-7 sebesar: 1500000.0
laba bulan ke-8 sebesar: 1500000.0
Total laba adalah: 9000000.0
PS C:\Users\user\Documents\Kuliah>
```
## Cara Kerja Program
1. *Modal Awal dan Laba Awal*:
    - Program dimulai dengan menetapkan modal awal sebesar 50.000.000.  
    - Program juga menyiapkan variabel total_laba yang dimulai dari 0, untuk menghitung total laba yang akan didapatkan selama 8 bulan.
Perhitungan Laba Tiap Bulan

2. *rogram menggunakan perulangan untuk menghitung laba dari bulan pertama sampai bulan kedelapan. Setiap bulan, persentase laba akan berbeda, seperti ini*:
    - Bulan 1 dan 2: Tidak ada laba, jadi laba bulan ini adalah 0.
    - Bulan 3 dan 4: Laba sebesar 1% dari modal awal (50.000.000).
    - Bulan 5 dan 6: Laba meningkat menjadi 5% dari modal awal.
    - Bulan 7: Laba turun menjadi 3% dari modal awal.
3. *Menampilkan dan Menghitung Total Laba*:
    - Setiap bulan, program akan menampilkan berapa laba bulan itu.
    - Laba setiap bulan akan ditambahkan ke total_laba untuk mendapatkan jumlah laba keseluruhan di akhir periode 8 bulan.
4. *Menampilkan Total Laba Setelah 8 Bulan*:
    - Setelah menghitung laba semua bulan, program menampilkan total laba yang diperoleh selama 8 bulan.

*Jadi, program ini membantu menghitung laba bulanan dan totalnya, berdasarkan persentase yang berubah-ubah tiap beberapa bulan.*

## Program 3 Saldo
Program ini adalah simulasi mesin ATM sederhana yang memungkinkan pengguna untuk melihat saldo, melakukan penarikan uang, dan keluar dari sistem. Berikut deskripsi dan cara kerja programnya
## Deskripsi Program
Program ini menggunakan bahasa Python untuk membuat simulasi sederhana dari sebuah ATM. Program ini memiliki dua fungsi utama:
  1. Menampilkan saldo awal.
  2. Memungkinkan pengguna untuk menarik uang dari saldo tersebut (selama jumlah yang diminta tidak melebihi saldo).
*Program ini menggunakan perulangan sehingga bisa terus dijalankan hingga pengguna memilih opsi keluar.*
## Kode Program 3
``` python
def atm():
    saldo = 15000000 #Initial balance
    while True:
        print(f"saldo saat ini : Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")

        pilihan = input("pilih menu (1/2): ")

        if pilihan == '1':
            try:
                jumlah_penarikan =int(input("masukan jumlah penarikan: "))
                if jumlah_penarikan <= saldo:
                    saldo = jumlah_penarikan
                    print("penarikan berhasil!")
                else :
                    print("saldo tidak mencukupi.")
            except ValueError :
                print("input tidak valid. masukan angka.")
        elif pilihan == '2':
            print("terima kasih telah menggunakan ATM!")
            break
        else :
            print("pilihan tidak vali. coba lagi.")
        print()

# Run the ATM function
atm()
```
## Output Program
```
PS C:\Users\user\Documents\Kuliah> & C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/user/Documents/Kuliah/lab2py/pemrograman/saldo atm.py"
saldo saat ini : Rp 15000000
1. Tarik Uang
2. Keluar
pilih menu (1/2): 1
masukan jumlah penarikan: 5000000
penarikan berhasil!

saldo saat ini : Rp 5000000
1. Tarik Uang
2. Keluar
pilih menu (1/2): 2
terima kasih telah menggunakan ATM!
PS C:\Users\user\Documents\Kuliah>
```
## Cara Kerja Program
1. *Saldo Awal*:
    - Program dimulai dengan saldo awal sebesar 15.000.000.
2. *Menampilkan Menu ATM*:
    - Program menampilkan dua opsi:
      1. Tarik Uang – untuk menarik sejumlah uang dari saldo.
      2. Keluar – untuk keluar dari program.
3. *Proses Penarikan Uang*:
    - Jika pengguna memilih opsi 1 (Tarik Uang), program akan meminta pengguna memasukkan jumlah uang yang ingin ditarik.
4. *Program kemudian melakukan pengecekan*:
    - Jika jumlah yang diminta tidak melebihi saldo, saldo akan diperbarui sesuai jumlah penarikan, dan pesan “penarikan berhasil!” akan ditampilkan.
    - Jika jumlah yang diminta melebihi saldo, program menampilkan pesan "saldo tidak mencukupi."
    - Jika input jumlah penarikan bukan angka, program menangani error dan menampilkan pesan "input tidak valid."
5. *Keluar dari Program*
    - Jika pengguna memilih opsi 2 (Keluar), program menampilkan pesan terima kasih dan berhenti.
6. *Kesalahan Input*:
    - Jika pengguna memasukkan pilihan menu yang tidak valid (selain 1 atau 2), program akan menampilkan pesan error dan kembali ke menu utama.

*Program ini akan terus berjalan dalam loop sampai pengguna memilih untuk keluar, dan menampilkan saldo terbaru setelah setiap transaksi.*

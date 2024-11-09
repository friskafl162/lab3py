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
import re  
import os

# Fungsi Validasi Nama (hanya huruf)
def validasi_nama(Nama):
    if Nama.istitle() and Nama.replace(" ", "").isalpha():
        return True
    else:
        return False
# Fungsi Validasi Umur (hanya angka)
def validasi_umur(Umur):
    if Umur.isdigit():
        return True
    else:
        return False
#Fungsi Validasi nomor ktp(hanya angka)
def validasi_nomor_ktp(nomor_ktp, list_employees):
    if nomor_ktp.isdigit() and len(nomor_ktp) == 16:
        for employee in list_employees:
            if 'Nomor Induk Kependudukan' in employee and str(employee['Nomor Induk Kependudukan']) == nomor_ktp:
                return False  
        return True  
    else:
        return False    
#Fungsi Validasi nomor induk pegawai (hanya angka)
def validasi_nomor_induk_pegawai(nomor_pegawai, list_employees):
    if nomor_pegawai.isdigit() and len(nomor_pegawai) == 6:
        for employee in list_employees:
            if 'Nomor Induk Pegawai' in employee and str(employee['Nomor Induk Pegawai']) == nomor_pegawai:
                return False  
        return True  
    else:
        return False  
# Fungsi Validasi Jenis Kelamin (hanya huruf)
def validasi_jenis_kelamin(jenis_kelamin):
    jenis_kelamin = jenis_kelamin.lower() 
    if jenis_kelamin == 'pria' or jenis_kelamin == 'wanita':
        return True
    else:
        return False
# Fungsi Validasi Tanggal Masuk Kerja (format tanggal-bulan-tahun)
def validasi_tanggal_masuk_kerja(tanggal_masuk_kerja):
    if re.match(r"^\d{2}-\d{2}-\d{4}$", tanggal_masuk_kerja):
        # Periksa apakah tanggal, bulan, dan tahun valid
        day, month, year = map(int, tanggal_masuk_kerja.split('-'))
        if 1 <= month <= 12 and 1900 <= year <= 2099:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                max_day = 31
            elif month in [4, 6, 9, 11]:
                max_day = 30
            else:  
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    max_day = 29  
                else:
                    max_day = 28
            if 1 <= day <= max_day:
                return True
    return False
# Fungsi Validasi Divisi (hanya huruf)
def validasi_divisi(divisi):
    divisi_diperbolehkan = ['sdm', 'keuangan', 'operasional', 'pemasaran']
    divisi = divisi.lower()  # Mengonversi input ke huruf kecil
    if divisi in divisi_diperbolehkan:
        return True
    else:
        return False
# Fungsi Validasi Jabatan (hanya huruf)
def validasi_jabatan(jabatan):
    jabatan_diperbolehkan = ['staf', 'kepala divisi', 'manajer', 'direktur']
    jabatan = jabatan.lower()# Mengonversi input ke huruf kecil
    if jabatan.isalpha() and jabatan in jabatan_diperbolehkan:
        return True
    else:
        return False
#Fungsi Validasi Cuti (hanya angka)
def validasi_cuti(cuti):
    if cuti.isdigit():
        return True
    else:
        return False
# Fungsi Validasi Gaji (angka dengan desimal)
def validasi_gaji(gaji):
    try:
        float(gaji)
        return True
    except ValueError:
        return False
#Fungsi validasi Save untuk menyimpan
def validasi_save():
    while True:
        pilihan = input("\n\tApakah Anda ingin menyimpan data ini? (ya/tidak): ")
        if pilihan.lower() == 'ya':
            return True
        elif pilihan.lower() == 'tidak':
            return False
        else:
            print("\n\tMohon jawab 'ya' atau 'tidak'.")
#Fungsi hapus layar
def hapus_layar():
    os.system('clear' if os.name == 'posix' else 'cls')
# Fungsi untuk menampilkan semua data karyawan
def show_all_data():
    print("\nDaftar Semua Data Karyawan :\n")
    for i, data in enumerate(list_employees, start=1):
        print(f"Data Karyawan {i}:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
        print()
# Fungsi untuk memeriksa apakah data dengan nomor induk pegawai tertentu ada dalam list
def check_data(nomor_pegawai):
    for i, data in enumerate(list_employees, start=1):
        if data['Nomor IndukPegawai'] == nomor_pegawai:
            print(f"Data Karyawan {i}:")
            for key, value in data.items():
                print(f"{key.capitalize()}: {value}")
            return
    print("Data dengan nomor induk pegawai tersebut tidak ditemukan.")
#Fungsi untuk Tampilkan Data Spesisifk
def tampilkan_data_spesifik(nomor_pegawai):
    for employee in list_employees:
        if 'Nomor Induk Pegawai' in employee and str(employee['Nomor Induk Pegawai']) == nomor_pegawai:
            print("\nData Karyawan:")
            for key, value in employee.items():
                print(f"{key}: {value}")
            return
    print(f"Karyawan dengan Nomor Pegawai {nomor_pegawai} tidak ditemukan.")
def validasi_input(pesan, kondisi):
    while True:
        nilai = input(pesan)
        if kondisi(nilai):
            return nilai
        else:
            print("\tInputan tidak valid, silakan coba lagi.")
def hapus_data_spesifik(nomor_pegawai):
        for employee in list_employees:
            if 'Nomor Induk Pegawai' in employee and str(employee['Nomor Induk Pegawai']) == nomor_pegawai:
                list_employees.remove(employee)
                if validasi_save():
                    database.append(list_employees)
                    print(f"\n\tData Karyawan dengan Nomor Induk Pegawai {nomor_pegawai} pada daftar pegawai telah dihapus.")
                return True  # Data ditemukan dan dihapus
        print(f"\n\tData dengan Nomor Induk Pegawai {nomor_pegawai} tidak ditemukan.")
        return False  # Data tidak ditemukan

list_employees = [
            {
                
                'Nomor Induk Pegawai'       : 100001,
                'Nama'                      :"Mbappe",
                'Umur'                      : 46,
                'Nomor Induk Kependudukan'  : 1234567890123456,
                'Jenis_Kelamin'             : "Pria",
                'Tanggal Masuk_Kerja'       : "01-01-2020",
                'Alamat'                    : "Jl. Nangka Indah No. 01 RT 01 RW 01 Kec.Sukajadi Kel. Sukakamu, Bandung, Jawa Barat, Badung",
                'Divisi'                    : "Direksi",
                'Jabatan'                   : "Direktur",
                'Cuti'                      : 12,
                'Gaji'                      : 6000000
                
            },
            {
                'Nomor Induk Pegawai'       : 100002,
                'Nama'                      : "Angel Karamoy",
                'Umur'                      : 28,
                'Nomor Induk Kependudukan'  : 1234567890123455,
                'Jenis Kelamin'             : "Wanita",
                'Tanggal Masuk_Kerja'       : "15-02-2021",
                'Alamat'                    : "Jl. Pramuka No. 10 RT 01 RW 07 Kec. Padalarang, Kel. Mekarluyu, Bandung, Jawa Barat",
                'Divisi'                    : "SDM",
                'Jabatan'                   : "Manager",
                'Cuti'                      : 9,
                'Gaji'                      : 6000000
                
            },
            {
                'Nomor Induk Pegawai'       : 100003,
                'Nama'                      : "Henry Susilo",
                'Umur'                      : 35,
                'Nomor Induk Kependudukan'  : 123456789012354,
                'Jenis Kelamin'             : "Pria",
                'Tanggal Masuk_Kerja'       : "10-03-2022",
                'Alamat'                    : "Jl. Surya Kencana No. 789 RT 03 RW 04 Kec. Mekarja Kel. Mekarluyu, Bandung, Jawa Barat",
                'Divisi'                    : "Marketing",
                'Jabatan'                   : "Kepala Divisi",
                'Cuti'                      : 9,
                'Gaji'                      : 6000000
            },
            {
                'Nomor Induk Pegawai'       : 100004,
                'Nama'                      : "Tara Basro",
                'Umur'                      : 31,
                'Nomor Induk Kependudukan'  : 123456789012353,
                'Jenis Kelamin'             : "Wanita",
                'Tanggal Masuk Kerja'       : "20-04-2022",
                'Alamat'                    : "Jl. Sarah Indah No. 789 RT 01 RW 05 Kec. Mangki Kel. Baru, Bandung, Jawa Barat",
                'Divisi'                    : "Keuangan",
                'Jabatan'                   : "Staf",
                'Cuti'                      : 10,
                'Gaji'                      : 6000000
            },
            {
                'Nomor Induk Pegawai'       : 100005,
                'Nama'                      : "Michael Sanjaya",
                'Umur'                      : 29,
                'Nomor Induk Kependudukan'  : 123456789012352,
                'Jenis Kelamin'             : "Pria",
                'Tanggal Masuk_Kerja'       : "05-05-2022",
                'Alamat'                    : "Jl. Pantai Indah Kapuk No 10 RT 01 RW 02 Kec. Kusuka Kel. Dada, Bandung, Jawa Barat",
                'Divisi'                    : "Operasional",
                'Jabatan'                   : "Staf",
                'Cuti'                      : 12,
                'Gaji'                      : 6000000

            }
        ]


#Fungsi Def Create
def tambah_data():
   while True:
        print('''
        == Menu Tambah Data ==
        1. Karyawan Baru
        2. Kembali ke Menu
        ======================
        ''')
        
        pilihan = input("\tSilahkan Pilih Opsi Yang Anda Inginkan(1/2): ")
        
        if pilihan.isdigit():
            if pilihan == '1':
                while True:
                    Nomor_Induk_Pegawai = input("\n\tSilahkan Masukkan 6 digit Nomor Induk Pegawai : ")
                    if validasi_nomor_induk_pegawai(Nomor_Induk_Pegawai,list_employees):
                        break
                    else:
                        print("\n\tMohon maaf 'Nomor Induk Pegawai' harus berupa angka (maksimal 6 digit) atau data sudah ada, silakan masukkan kembali.")
                        tambah_data()    
                while True:
                    Nama = input("\n\tSilahkan Masukkan Nama di Awali dengan Huruf Kapital di awal kata : ")
                    if validasi_nama(Nama):
                        break
                    else:
                        print("\n\tMohon maaf 'Nama' harus diawali dengan huruf kapital di awal kata dan hanya berisi huruf. Silakan masukkan kembali.")

                while True:
                    Umur = input("\n\tSilahkan Masukkan Umur : ")
                    if validasi_umur(Umur):
                        break
                    else:
                        print("\n\tMohon maaf 'Umur' harus berupa angka. Silakan masukkan kembali.")

                while True:
                    Nomor_Induk_Kependudukan = input("\n\tSilahkan Masukkan Nomor Induk Kependudukan : ")
                    if validasi_nomor_ktp(Nomor_Induk_Kependudukan, list_employees):
                        break
                    else:
                        print("\n\tMohon maaf 'Nomor Induk Kependudukan (KTP)' harus berupa 16 digit angka atau data sudah ada. Silakan masukkan kembali.")

                while True:
                    Jenis_Kelamin = input("\n\tSilahkan Masukkan Jenis Kelamin (Pria/Wanita) : ")
                    if validasi_jenis_kelamin(Jenis_Kelamin):
                        break
                    else:
                        print("\n\tMohon maaf 'Jenis Kelamin' harus diisi dengan 'Pria' atau 'Wanita'. Silakan masukkan kembali.")

                while True:
                    Tanggal_Masuk_Kerja = input("\n\tSilahkan Masukkan Tanggal Masuk Kerja (dd-mm-yyyy) : ")
                    if validasi_tanggal_masuk_kerja(Tanggal_Masuk_Kerja):
                        break
                    else:
                        print("\n\tMohon maaf 'Tanggal Masuk Kerja' harus dalam format tanggal-bulan-tahun (dd-mm-yyyy). Silakan masukkan kembali.")

                Alamat = input("\n\tSilahkan Masukkan Alamat : ")

                while True:
                    Divisi = input("\n\tSilahkan Masukkan Divisi (SDM/Keuangan/Operasional/Marketing/Direksi) : ")
                    if validasi_divisi(Divisi):
                        break
                    else:
                        print("\n\tMohon maaf 'Divisi' harus diisi dengan 'SDM' atau  'Keuangan' atau 'Operasional' atau 'Marketing'. Silakan masukkan kembali.")

                while True:
                    Jabatan = input("\n\tSilahkan Masukkan Jabatan (Staf/Kepala Divisi/Manajer/Direktur) : ")
                    if validasi_jabatan(Jabatan):
                        break
                    else:
                        print("\n\tMohon maaf 'Jabatan' harus diisi dengan 'Staf' atau 'Kepala Divisi' atau 'Manajer' atau 'Direktur'. Silakan masukkan kembali.")

                while True:
                    Cuti = input("\n\tSilahkan Masukkan Cuti : ")
                    if validasi_cuti(Cuti):
                        break
                    else:
                        print("\n\tMohon maaf 'Cuti' harus berupa angka. Silakan masukkan kembali.")

                while True:
                    Gaji = input("\n\tSilahkan Masukkan Gaji : ")
                    if validasi_gaji(Gaji):
                        break
                    else:
                        print("\n\tMohon maaf 'Gaji' harus berupa angka. Silakan masukkan kembali.")

                    
        # # Tambahkan data karyawan baru ke list_employees
                list_employees.append({
                    'Nomor Induk Pegawai': Nomor_Induk_Pegawai,
                    'Nama': Nama,
                    'Umur': Umur,
                    'Nomor Induk Kependudukan': Nomor_Induk_Kependudukan,
                    'Jenis Kelamin': Jenis_Kelamin,
                    'Tanggal Masuk_Kerja': Tanggal_Masuk_Kerja,
                    'Alamat': Alamat,
                    'Divisi': Divisi,
                    'Jabatan': Jabatan,
                    'Cuti': Cuti,
                    'Gaji': Gaji
                })
                       
                # Menyimpan data ke dalam database jika disetujui
                if validasi_save():
                    database.append(list_employees)
                    print("\n\tData berhasil disimpan ke dalam database.")
                else:
                    print("\n\tData tidak disimpan ke dalam database.")

            elif pilihan == '2':
                main_menu()
                hapus_layar()
                break
        else:
            print("\n\tPilihan tidak valid. Silakan pilih opsi yang benar (1/2).")  

        
# Fungsi untuk menampilkan data (Read)
def tampilkan_data():
    while True:
        print('''
        ======= Menu Tampilkan Data =======
        1. Tampilkan Semua Data Karyawan
        2. Tampilkan Spesifik Data Karyawan
        3. Kembali ke Menu
        ===================================
        ''')

        pilihan = input("\tSilahkan Pilih Opsi Yang Anda Inginkan (1/2/3): ")
        
        if pilihan == '1':
            if len(list_employees) != 0:
                show_all_data()  
            else:
                print("\n\tTidak ada data karyawan.")
            
        elif pilihan == '2':
            hapus_layar()
            nomor_pegawai = input("\nSilahkan Masukkan Nomor Induk Pegawai yang ingin Anda cari: ")
            tampilkan_data_spesifik(nomor_pegawai)
        elif pilihan == '3':
            main_menu()
            break
        else:
            print("\n\tPilihan tidak valid, silahkan pilih opsi kembali") 

# Fungsi untuk memperbarui data (Update)
def update_data():
    while True:
        print('''
        ====== Menu Update Data ======  
        1. Update Data Karyawan
        2. Kembali ke Menu
        ==============================
        ''')

        pilihan = input("\tSilahkan Pilih Opsi Yang Anda Inginkan (1/2): ")

        if pilihan == '1':
            nomor_pegawai = input("\n\tSilahkan Masukkan Nomor Induk Pegawai yang ingin diperbarui: ")
            found = False
            for idx, employee in enumerate(list_employees):
                if 'Nomor Induk Pegawai' in employee and str(employee['Nomor Induk Pegawai']) == nomor_pegawai:
                    found = True
                    print("\nData Karyawan yang akan diperbarui:")
                    for key, value in employee.items():
                        print(f"{key}: {value}")
                    
                    print("\n\tPilih Menu yang Anda Ingin Ubah:\n"
                    "\t1. Nomor Induk Pegawai\n"
                    "\t2. Nama\n"
                    "\t3. Umur\n"
                    "\t4. Nomor Induk Kependudukan\n"
                    "\t5. Jenis Kelamin\n"
                    "\t6. Tanggal Masuk Kerja\n"
                    "\t7. Alamat\n"
                    "\t8. Divisi\n"
                    "\t9. Jabatan\n"
                    "\t10.Cuti\n"
                    "\t11.Gaji\n"
                    "\t12.Kembali ke Menu Update")

                    pilihan = input("\n\tSilahkan Pilih Opsi Yang Anda Inginkan: ")
                    while True:
                        if pilihan == '1':
                            new_value = validasi_input("\n\tSilahkan Masukkan Nomor Induk Pegawai Baru: ", lambda x: validasi_nomor_induk_pegawai(x, list_employees))
                            list_employees[idx]['Nomor Induk Pegawai'] = new_value
                        elif pilihan == '2':
                            new_value = validasi_input("\n\tSilahkan Masukkan Nama Baru dengan huruf capital di awal: ", validasi_nama)
                            list_employees[idx]['Nama'] = new_value
                        elif pilihan == '3':
                            new_value = validasi_input("\n\tSilahkan Masukkan Umur Baru: ", validasi_umur)
                            list_employees[idx]['Umur'] = new_value
                        elif pilihan == '4':
                            new_value = validasi_input("\n\tSilahkan Masukkan Nomor Induk Kependudukan Baru: ", lambda x: validasi_nomor_ktp(x, list_employees))
                            list_employees[idx]['Nomor Induk Kependudukan'] = new_value
                        elif pilihan == '5':
                            new_value = validasi_input("\n\tSilahkan Masukkan Jenis Kelamin Baru: ", validasi_jenis_kelamin)
                            list_employees[idx]['Jenis Kelamin'] = new_value
                        elif pilihan == '6':
                            new_value = validasi_input("\n\tSilahkan Masukkan Tanggal Masuk Kerja Baru (dd-mm-yyyy): ", validasi_tanggal_masuk_kerja)
                            list_employees[idx]['Tanggal Masuk Kerja'] = new_value
                        elif pilihan == '7':
                            new_value = validasi_input("\n\tSilahkan Masukkan Alamat Baru: ")
                            list_employees[idx]['Alamat'] = new_value
                        elif pilihan == '8':
                            new_value = validasi_input("\n\tSilahkan Masukkan Divisi Baru: ", validasi_divisi)
                            list_employees[idx]['Divisi'] = new_value
                        elif pilihan == '9':
                            new_value = validasi_input("\n\tSilahkan Masukkan Jabatan Baru: ", validasi_jabatan)
                            list_employees[idx]['Jabatan'] = new_value
                        elif pilihan == '10':
                            new_value = validasi_input("\n\tSilahkan Masukkan Jumlah Cuti Baru: ", validasi_cuti)
                            list_employees[idx]['Cuti'] = new_value
                        elif pilihan == '11':
                            new_value = validasi_input("\n\tSilahkan Masukkan Gaji Baru: ", validasi_gaji)
                            list_employees[idx]['Gaji'] = new_value
                        elif pilihan == '12':
                            update_data()
                        else:
                            print("\n\tPilihan tidak valid. Silakan pilih opsi yang benar.")
                        if validasi_save():
                            database.append(list_employees)
                            print("\n\tData berhasil disimpan ke dalam database.")
                        update_data()
                        break
            if not found:
                print(f"\tData dengan Nomor Induk Pegawai {nomor_pegawai} tidak ditemukan. Silakan coba lagi.")
        elif pilihan == '2':
            main_menu()
            hapus_layar()
            break
        else:
            print("\n\tPilihan tidak valid. Silakan pilih opsi yang benar (1/2).")


# Fungsi untuk menghapus data (Delete)
def hapus_data():
    while True:
        print('''
        ====== Menu Hapus Data ======
              
        1. Hapus Semua Data Karyawan
        2. Hapus Spesifik Data Karyawan
        3. Kembali ke Menu
        =============================
        ''')
        pilihan = input("\tSilahkan Pilih Opsi Yang Anda Inginkan(1/2/3) :")
        
        if pilihan == '1':
            while True:
                konfirmasi = input("\n\tAnda yakin ingin menghapus semua data karyawan? (ya/tidak): ")
                if konfirmasi.lower() == 'ya':
                    list_employees.clear()
                    database.append(list_employees)
                    print("\n\tData berhasil dihapus dari database.")
                    hapus_data()
                elif konfirmasi.lower() == 'tidak':
                    hapus_data()
                else:
                    print("\nMohon jawab 'ya' atau 'tidak'.")
               
        elif pilihan == '2':
            while True:
                nomor_pegawai = input("\tMasukkan Nomor Induk Pegawai yang ingin Anda hapus: ")
                for employee in list_employees:
                    if 'Nomor Induk Pegawai' in employee and str(employee['Nomor Induk Pegawai']) == nomor_pegawai:
                        list_employees.remove(employee)
                        if validasi_save():
                            database.append(list_employees)
                            print(f"\n\tData Karyawan dengan Nomor Induk Pegawai {nomor_pegawai} pada daftar pegawai telah dihapus.")
                        return True  
                    print(f"\n\tData dengan Nomor Induk Pegawai {nomor_pegawai} tidak ditemukan.")
                return False  
        elif pilihan == '3':
            main_menu()
        else:
            print("\n\tPilihan tidak valid. Silakan pilih opsi yang benar (1/2/3).")
            
        
def ajukan_cuti():
    while True:
        print('''
        1. Ajukan Cuti Karyawan
        2. Kembali ke Menu
        ''')
        pilihan = input("\tSilahkan Pilih Opsi Yang Anda Inginkan (1/2): ")

        if pilihan == '1':
            nomor_pegawai = input("\n\tMasukkan Nomor Induk Pegawai untuk ajukan cuti: ")
            found = False

            for employee in list_employees:
                if 'Nomor Induk Pegawai' in employee and str(employee['Nomor Induk Pegawai']) == nomor_pegawai:
                    found = True
                    jumlah_cuti = input("\n\tMasukkan jumlah cuti yang diajukan: ")

                    if jumlah_cuti.isdigit():
                        jumlah_cuti = int(jumlah_cuti)
                        sisa_cuti = int(employee.get('Cuti', 0))

                        if jumlah_cuti <= sisa_cuti:
                            employee['Cuti'] = str(sisa_cuti - jumlah_cuti)
                            print(f"\tCuti sebanyak {jumlah_cuti} hari berhasil diajukan untuk karyawan dengan Nomor Induk Pegawai {nomor_pegawai}.")
                            
                            # Menyimpan data ke dalam database jika disetujui
                            if validasi_save():
                                database.append(list_employees)
                                print("\tData berhasil disimpan ke dalam database.")

                        else:
                            print("\n\tJumlah cuti yang diajukan melebihi sisa cuti yang dimiliki. Silakan masukkan jumlah cuti yang benar.")
                    else:
                        print("\n\tMohon masukkan jumlah cuti dalam bentuk angka. Silakan pilih opsi yang benar.")
                    break  # Keluar dari loop setelah menemukan karyawan dengan NIP yang sesuai

            if not found:
                print(f"\n\tData dengan Nomor Induk Pegawai {nomor_pegawai} tidak ditemukan.")
        
        elif pilihan == '2':
            main_menu()
            break
        else:
            print("\n\tPilihan tidak valid. Silakan masukkan angka 1 atau 2, silahkan pilih opsi yang benar")

   
# Informasi login
info_login = {
    "bandung": "juara",
}
# Fungsi untuk memeriksa login
def cek_login(username, password):
    if username in info_login and info_login[username] == password:
        return True
    return False

print('''
        = = = = = = = SELAMAT DATANG DI MY HRD = = = = = = =
        
        = = = = = = = = = HOW ARE YOU BOSS = = = = = = = = = ''')

# Loop untuk login
while True:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    if cek_login(username, password):
        print(f"Selamat datang, {username}!")
        break
    else:
        print("Username atau Password salah. Silakan coba lagi.")
hapus_layar()

# Setelah berhasil login, masuk menu disini
database = []  # Database untuk menyimpan data

# Loop utama program
def main_menu():
    while True:
        pilihan = input(
        '''
    _______________________
        
        SELAMAT DATANG 
           DI MY HRD
    PT. KITA MAJU SEJAHTERA
    _______________________
    
    == Pilihan Menu Utama: ==
    
    1. Tampilkan Data Karyawan
    2. Tambah Data Karyawan
    3. Update Data Karyawan
    4. Hapus Data Karyawan
    5. Mengajukan Cuti Karyawan
    6. Keluar

    Pilih Opsi Menu Yang Anda Inginkan (1/2/3/4/5/6): 
    ''')
        if pilihan.isdigit():
            if pilihan == '1':
                tampilkan_data()
            elif pilihan == '2':
                tambah_data()
            elif pilihan == '3':
                update_data()
            elif pilihan == '4':
                hapus_data()
            elif pilihan == '5':
                ajukan_cuti()
            elif pilihan == '6':
                konfirmasi = input("\n\tApakah Anda yakin ingin keluar? (ya/tidak): ")
                hapus_layar()
                if konfirmasi.lower() == 'ya':
                    print("\n\n\tTerima kasih! Sampai jumpa.") 
                    break    
                hapus_layar()              
            else:
                print("\n\tPilihan tidak valid. Silakan coba lagi.")
        else:
            print("\n\nPilihan harus berupa angka. Silakan coba lagi.")

main_menu()

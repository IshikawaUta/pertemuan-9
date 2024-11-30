from colorama import Fore

# pencarian binier
daftar_nama_urut = ["dali", "rama", "alwan", "rizal"]
nama_yang_dicari = "alwan"

tengah = len(daftar_nama_urut) // 2
if daftar_nama_urut[tengah] == nama_yang_dicari:
    print(Fore.BLUE + "nama ditemukan!", Fore.RESET)
else:
    print(Fore.RED + "nama tidak ditemukan?", Fore.RESET)
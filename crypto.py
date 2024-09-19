import requests
import locale ,os ,time
import os,sys,time,os,requests,datetime
import random
import colorama
from colorama import Fore

localtime=time.asctime(time.localtime(time.time()))
ip=requests.get('https://api.ipify.org').text


B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

hijau="\033[0;92m "
putih="\033[0;97m"
abu="\033[0;90m"
kuning="\033[0;93m"
ungu="\033[0;95m"
merah="\033[0;91m"
biru="\033[0;96m"




def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def banner():
    print(f"""\n{putih}[{B}•{putih}] {biru}Developer{hijau}: MarshallSetian
{putih}[{B}•{putih}] {ungu}Instagram {putih}: @marshall_setian
{W}[{B}•{W}] Ip Kamu {putih}  :{kuning} {ip}
{W}[{B}•{W}] Waktu/Jam {putih}:{merah} {localtime}
{putih}================================================{hijau}
PROGRAM CRYPTO PRICE - REALTIME - CONVERT RUPIAH
{W}================================================
Bahasa Program :{hijau}Python{putih}
Kode Sumber    : {kuning}https://www.coingecko.com/{putih}
================================================""")

# Set locale untuk format Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['bitcoin']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Bitcoin saat ini   : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        print("Terjadi kesalahan saat mengambil data.")


    

def get_pepe_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=pepe&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['pepe']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%.2f", price, grouping=True)
        autoketik(f"Harga PEPE coin saat ini : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")




def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['ethereum']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Ethereum saat ini  : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")



def get_dollar_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['tether']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Dollar saat ini    : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")




def get_shiba_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['shiba-inu']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%.2f", price, grouping=True)
        autoketik(f"Harga Shiba Inu saat ini : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")


def get_sol_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['solana']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Solana saat ini    : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")




def get_bnb_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['binancecoin']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Binance saat ini   : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")


def get_ada_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['cardano']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Cardano saat ini   : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")


def get_xrp_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=idr"


    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['ripple']['idr']
        # Format harga dengan locale
        formatted_price = locale.format_string("%d", price, grouping=True)
        autoketik(f"Harga Ripple saat ini    : {kuning}Rp {formatted_price.replace(',', '.')}{putih}")
    else:
        autoketik(f"{merah}Terjadi kesalahan saat mengambil data.{putih}")


def pilihan():

    while True:

        
        banner()
        print(f"\n1.Cek Harga Dollar     {biru}(USDT):{putih}")
        print(f"2.Cek Harga Bitcoin     {biru}(BTC):{putih}")
        print(f"3.Cek Harga Ethereum    {biru}(ETH):{putih}")
        print(f"4.Cek Harga Solana      {biru}(SOL):{putih}")
        print(f"5.Cek Harga Binance     {biru}(BNB):{putih}")
        print(f"6.Cek Harga Cardano     {biru}(ADA):{putih}")
        print(f"7.Cek Harga Ripple      {biru}(XRP):{putih}")
        print(f"8.Cek Harga Shiba Inu  {biru}(SHIB):{putih}")
        print(f"9.Cek Harga Pepe Coin  {biru}(PEPE):{putih}")

        print("\n99.Cek Semua Harga =========>")
        print(f"\nExit : {merah}(Ctrl+z){putih}")


        pilihan = input("\nSilahkan Masukkan Pilihan Dengan Angka : ")


        if pilihan == "1":
            time.sleep(2)
            os.system("clear")
            get_dollar_price()
            time.sleep(5)
            

        elif pilihan == "2":
            time.sleep(2)
            os.system("clear")
            get_bitcoin_price()
            time.sleep(5)

        elif pilihan == "3":
            time.sleep(2)
            os.system("clear")
            get_eth_price()
            time.sleep(5)

        elif pilihan == "4":
            time.sleep(2)
            os.system("clear")
            get_sol_price()
            time.sleep(5)

        elif pilihan == "5":
            time.sleep(2)
            os.system("clear")
            get_bnb_price()
            time.sleep(5)
        elif pilihan == "6":
            time.sleep(2)
            os.system("clear")
            get_ada_price()
            time.sleep(5)
        elif pilihan == "7":
            time.sleep(2)
            os.system("clear")
            get_xrp_price()
            time.sleep(5)
        elif pilihan == "8":
            time.sleep(2)
            os.system("clear")
            get_shiba_price()
            time.sleep(5)
        elif pilihan == "9":
            time.sleep(2)
            os.system("clear")
            get_pepe_price()
            time.sleep(5)

        elif pilihan == "99":
            time.sleep(2)
            os.system("clear")
            banner()
            get_dollar_price()
            time.sleep(3)
            get_bitcoin_price()
            time.sleep(3)
            get_eth_price()
            time.sleep(3)
            get_sol_price()
            time.sleep(3)
            get_bnb_price()
            time.sleep(3)
            get_ada_price()
            time.sleep(3)
            get_xrp_price()
            time.sleep(3)
            get_shiba_price()
            time.sleep(3)
            get_pepe_price()
            time.sleep(5)
            exit = input(f"\nTekan{hijau}Enter{putih} Untuk kembali ke-Menu Sebelumnya : ")
            if exit == 99:
                autoketik("OkcSiappp BosQue.......")
                
            elif exit == 00:
                pilihan()
            os.system("clear")
            
        else:
            
            print(f"{merah}pilihan anda tidak valid!!!")
            time.sleep(2)
            os.system("clear")
            
            continue

pilihan()




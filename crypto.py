import requests
import locale

# Set locale untuk format Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def get_pepe_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=pepe&vs_currencies=idr"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['pepe']['idr']
        
        # Format harga tanpa desimal
        if price.is_integer():
            formatted_price = locale.format_string("%d", price, grouping=True)  # Tanpa desimal
        else:
            formatted_price = locale.format_string("%.2f", price, grouping=True)  # Dengan 2 desimal
        
        print(f"Harga Token Pepe saat ini: Rp {formatted_price.replace(',', '.')}")
    else:
        print("Terjadi kesalahan saat mengambil data.")

if __name__ == "__main__":
    get_pepe_price()

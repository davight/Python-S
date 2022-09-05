# Pomocou requests lib mozeme ziskavat odpovede z web APIs
import requests

# Pomocou socket lib mozeme "overovat" platnost IPciek
import socket

# Pomocou sys lib ukoncime program
import sys


# +++ Funkcia pre IP lookup
def get_location(adresa):
    
    # Premenime adresu na string
    ip_address = str(adresa)
    
    # Pomocou web api ziskame info k danej ip adrese a premenime na json
    odpoved = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    
    # Zadefinujeme dict s odpovedami z requestu
    location_data_dict = {
    
        # Info z JSONu ziskavame pomocou get
        "ip": adresa,
        "mesto": odpoved.get("city"),
        "kraj": odpoved.get("region"),
        "krajina": odpoved.get("country_name")
    }

    # Printneme odpoved:
    print("\nPrintujem odpoved:")
    # Loopneme cez dict
    for key in location_data_dict:
        
        # Key je key, cize "mesto", "ip", "kraj"...
        kluc = key.capitalize()
        # Value je priradena hodnota pri keys
        value = location_data_dict[key]
        
        print(kluc,"=",value)
    
    sys.exit()


# +++ Funkcia pre overenie platnosti IP adresy
def valid_ip_otaznik(ciselko):
    
    # Pomocou socket lib overime ipcku
    try: 
    
        socket.inet_aton(ciselko)
        # Returtneme, ze je platna
        return True
    
    except socket.error:
    
        # Returneme, ze je neplatna, lebo IPcka nie je platna
        return False


IP = False

# Kym nie je IPcka platna tak budeme loopovat input
while not IP:

    # Zadefinujeme odpoved ako input
    Odpoved = input("Zadaj IP adresu pre jej lookup, ip adresa MUSI byt platna!\nAdresa: ")
    
    # Overime platnost ipcky funkciu valid_ip_otaznik
    IP = valid_ip_otaznik(Odpoved)

# Zavolame funkciu so zadanou ipckou
get_location(Odpoved)


# Testovacia ipcka --> 212.37.87.11

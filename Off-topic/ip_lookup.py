# Pomocou requests lib mozeme ziskavat odpovede z web APIs
import requests

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


    # Loopneme cez dict
    for key in location_data_dict:
        
        # Key je key, cize "mesto", "ip", "kraj"...
        kluc = key.capitalize()
        # Value je priradena hodnota pri keys
        value = location_data_dict[key]
        
        print(kluc,"=",value)

# Zavolame funkciu so zadanou ipckou
get_location("212.37.87.11")

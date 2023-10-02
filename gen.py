import requests

# Unesite svoj Genius API ključ ovde
GENIUS_API_KEY = ''

# Unesite ime izvođača kog želite da pretražujete
izvodjac = input(" Travis Scott ")

# Postavite URL za pretragu pesama izvođača
search_url = f'https://api.genius.com/search?q={izvodjac}'

# Postavite zaglavlje sa API ključem
headers = {
    'Authorization': f'Bearer {GENIUS_API_KEY}'
}

# Izvršite GET zahtev ka Genius API-ju
response = requests.get(search_url, headers=headers)

# Proverite da li je zahtev uspeo
if response.status_code == 200:
    data = response.json()
    hits = data['response']['hits']
    
    if len(hits) == 0:
        print(f"Nema pesama za izvođača: {izvodjac}")
    else:
        print(f"Pesme izvođača: {izvodjac}")
        for hit in hits:
            title = hit['result']['title']
            print(title)
else:
    print(f"Greška pri pretrazi: {response.status_code}")

import urllib.request
import re
import json

# Aquí puedes dejar listas de prueba o las URLs de tus M3U
PLAYLIST_URLS = [
    # "https://ejemplo.com/tu-lista.m3u"
]

def parse_m3u_from_url(url):
    movies = []
    series = []
    adult = []
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8', errors='ignore')
            lines = content.splitlines()
            current_inf = ""
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("#EXTINF"):
                    current_inf = line
                elif not line.startswith("#"):
                    url_stream = line
                    
                    name_match = re.search(r',(.+)$', current_inf)
                    name = name_match.group(1).strip() if name_match else "Desconocido"
                    
                    group_match = re.search(r'group-title="([^"]+)"', current_inf, re.IGNORECASE)
                    group = group_match.group(1).strip() if group_match else "General"
                    
                    logo_match = re.search(r'tvg-logo="([^"]+)"', current_inf, re.IGNORECASE)
                    logo = logo_match.group(1).strip() if logo_match else None
                    
                    item = {
                        "name": name,
                        "url": url_stream,
                        "group": group,
                        "logo": logo
                    }
                    
                    is_adult = any(x in group.lower() or x in name.lower() for x in ["xxx", "+18", "adultos", "hot"])
                    
                    if is_adult:
                        adult.append(item)
                    elif "/series/" in url_stream.lower() or "serie" in group.lower():
                        series.append(item)
                    else:
                        movies.append(item)
    except Exception as e:
        print(f"Error procesando {url}: {e}")
        
    return movies, series, adult

def main():
    all_movies = []
    all_series = []
    all_adult = []
    
    for url in PLAYLIST_URLS:
        m, s, a = parse_m3u_from_url(url)
        all_movies.extend(m)
        all_series.extend(s)
        all_adult.extend(a)
        
    unique_movies = {m['name'].lower(): m for m in all_movies}.values()
    unique_series = {s['name'].lower(): s for s in all_series}.values()
    unique_adult = {a['name'].lower(): a for a in all_adult}.values()
    
    catalog = {
        "movies": list(unique_movies),
        "series": list(unique_series),
        "adult": list(unique_adult)
    }
    
    with open("vod_catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("¡Catálogo VOD optimizado generado con éxito!")

if __name__ == "__main__":
    main()
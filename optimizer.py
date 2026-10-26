import urllib.request
import re
import json

PLAYLIST_URLS = [
    # Tus listas principales (recuerda poner las mejores al inicio)
    "http://playtvch.lat:8080/get.php?username=zcenter419&password=2024329865&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=RetamalClaudio22&password=aEeaajWuT4Fv&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=rodrigoobreque2&password=927481891&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=stkjudose&password=9325&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595984867452prytv&password=04102026pro&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=bernardocortes&password=WUECFdr6GQcM&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=mariavictoria&password=26maria91&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=Heinerantury&password=Chaka&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=Beatrizmoreno&password=rN66FftwNLBS&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=stkmauca&password=7409&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595983770203py&password=240726play&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=RobertoCartero7&password=PNZVxndaa4Jr&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=Stefaniagarcia&password=3vjtKGNxvGQg&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56998352745jgm&password=240926jgm&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56993236968tch&password=160826tch&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56996095292wspzero&password=230422zero&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=pYy6v4NYurgP&password=vKqDUJjvVdGU&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56974459040tch&password=200826tch&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56929855369tch&password=060826tch&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=gracielaisabel&password=927482555&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=rafa90&password=202020&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=Julio1287&password=686467&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=Frankyvarela&password=91682929262&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=DEMO5643&password=ASD34572&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595982367679prytv&password=01102026pro&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56993416718&password=250319iptv&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595991370530prytv&password=10102026pro&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595987336851py&password=290826play&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=stkcrmor&password=3974&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=stkcaag&password=4286&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=stellar042&password=stellar042&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595972950187py&password=200926play&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=stkfemill&password=3240&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=882549&password=6987441&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595992854164&password=02052026&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=vg2026&password=villa10&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=azplay743&password=1346890765&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56984782160faceztv&password=140722ztv&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=ipip10&password=tvtv10&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=angielnavarro&password=jJL3mn8QGHgd&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=v3c1n0&password=280526&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=tvt88&password=canapa8&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=IsabelSalvo30&password=wsx2gzJUkptT&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56983613119tch&password=300826tch&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=898valentin&password=72j2bwkk2k&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=595992182845prytv&password=03102026pro&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=walterhernandezvod&password=VODseparadoxssiptv&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56995161184w1&password=220525activa&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56983042450w&password=250425ztv&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=Javierve&password=3275marce&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=enriquecs&password=cesar546&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=zcenter10&password=967320059&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=roman&password=670123&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56948951901tch&password=060826tch&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56952540870faceztv&password=Casa4663&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56961917223wspztv&password=20122024ztv&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=ramon45&password=202020&type=m3u_plus",
    "http://playtvch.lat:8080/get.php?username=56990795612wspztv&password=150123ztv&type=m3u_plus",
    # Nuevas listas ZonaLatina, DaLive, TVQ
    "http://zonalatina.xyz:80/get.php?username=12812507396&password=270222zero&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=christiangonzalezgonzalez&password=56962313447ztv&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=6533pro5686&password=pa289ss563&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=56976915910wspztv&password=220622ztv&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=56989918645zero&password=080923zero&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=Hugocerpa1847&password=Chiletv1847&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=CarlosGonzales416&password=FMFrzZGbGL&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=SergioMarcoleta380&password=Chiletv380&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=56983589845wspzero&password=200821zero&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=56931486071faceztv&password=22042023ztv&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=mendozari567832&password=567832mendozari&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=56988997338wspztv&password=020324ztv&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=CesarLeon&password=hGGK2W2KxKQK&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=usuario1031&password=1a2b7r47k&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=cheriepoggini&password=DHNJBFejUa&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=Ricardo1234&password=R3c1rd42&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=56977938205wspzero&password=310324zero&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=LupyRojas&password=Daniela1998lupy&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=usuario1061&password=1a5nv25g1y&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=usuario2011&password=gg54yy76re&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=usuario1048&password=fa14hg89vc&type=m3u_plus",
    "http://zonalatina.xyz:80/get.php?username=NmsHbKPxXQ&password=t8jHWW5uYy&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=JorgeLeon&password=JorgeLeon&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=Sarita&password=Sarita&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=Demoluisfuentealba01&password=94yzwDN2Lv6I9TG3vUX&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=Pepe&password=1234&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=56964319607&password=SRY339fuPh&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=ZONATV19334&password=8WZUC6pcu2&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=252525&password=252525&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=iptv10888&password=vAZqL37PBfjw&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=NOVA73R45&password=rEpYABmMbDMw&type=m3u_plus",
    "http://dalive.site:8080/get.php?username=Omarprosop&password=1347339e05&type=m3u_plus",
    "http://tvq.lat:8080/get.php?username=Cristianvelasquez&password=56957188630&type=m3u_plus",
    "http://tvq.lat:8080/get.php?username=JoRDaN25sept25&password=castro25sept25&type=m3u_plus",
    "http://tvq.lat:8080/get.php?username=Nubexapoyo2024&password=tXD9QwZuLftA&type=m3u_plus",
    "http://tvq.lat:8080/get.php?username=Patriciovilches&password=56949603294&type=m3u_plus",
    "http://tvq.lat:8080/get.php?username=rs7621345&password=ZXWG3WppBhx4&type=m3u_plus",
    "http://tvq.lat:8080/get.php?username=rslamtv&password=SNA8mxMqqHLd&type=m3u_plus"
]

def clean_series_title(name):
    match = re.search(r'(?i)\s*S\d+\s*E\d+', name)
    if match: return name[:match.start()].strip()
    match2 = re.search(r'(?i)\s*Cap[ií]tulo\s*\d+', name)
    if match2: return name[:match2.start()].strip()
    return name

def parse_m3u_from_url(url):
    live, movies, series, anime, adult = [], [], [], [], []
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'IPTVSmartersPro'})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8', errors='ignore')
            lines = content.splitlines()
            current_inf = ""
            for line in lines:
                line = line.strip()
                if not line: continue
                if line.startswith("#EXTINF"):
                    current_inf = line
                elif not line.startswith("#"):
                    url_stream = line
                    name_match = re.search(r',(.+)$', current_inf)
                    name = name_match.group(1).strip() if name_match else "Desconocido"
                    group_match = re.search(r'group-title="([^"]+)"', current_inf, re.IGNORECASE)
                    group = group_match.group(1).strip() if group_match else "General"
                    logo_match = re.search(r'tvg-logo="([^"]+)"', current_inf, re.IGNORECASE)
                    logo = logo_match.group(1).strip() if logo_match else ""
                    
                    # Omitimos sinopsis largas para ahorrar espacio en megabytes
                    group_lower, name_lower, url_lower = group.lower(), name.lower(), url_stream.lower()
                    item = { "name": name, "url": url_stream, "group": group, "logo": logo, "synopsis": "" }
                    
                    if any(x in group_lower or x in name_lower for x in ["xxx", "+18", "adultos", "hot", "playboy"]):
                        adult.append(item)
                    elif "anime" in group_lower or "anime" in name_lower:
                        if re.search(r'(?i)S\d+\s*E\d+', name) or re.search(r'(?i)Cap[ií]tulo', name):
                            item["seriesTitle"] = clean_series_title(name)
                        anime.append(item)
                    elif "/series/" in url_lower or re.search(r'(?i)S\d+\s*E\d+', name):
                        item["seriesTitle"] = clean_series_title(name)
                        series.append(item)
                    elif "/movie/" in url_lower or url_lower.endswith(('.mp4', '.mkv', '.avi', '.m4v')) or "pelicula" in group_lower or "vod" in group_lower:
                        movies.append(item)
                    else:
                        live.append(item)
    except Exception as e:
        print(f"Error procesando {url}: {e}")
    return live, movies, series, anime, adult

def deduplicate(items, max_limit=3000):
    seen = {}
    for item in items:
        name = item['name']
        if name not in seen:
            seen[name] = item
        if len(seen) >= max_limit: # Ponemos un tope para asegurar que nunca pase de 50-70 MB
            break
    return list(seen.values())

def main():
    all_live, all_movies, all_series, all_anime, all_adult = [], [], [], [], []
    
    for url in PLAYLIST_URLS:
        print(f"Procesando: {url}")
        l, m, s, an, a = parse_m3u_from_url(url)
        all_live.extend(l)
        all_movies.extend(m)
        all_series.extend(s)
        all_anime.extend(an)
        all_adult.extend(a)
        
    catalog = {
        "live": deduplicate(all_live, max_limit=4000),
        "movies": deduplicate(all_movies, max_limit=3500),
        "series": deduplicate(all_series, max_limit=2500),
        "anime": deduplicate(all_anime, max_limit=1500),
        "adult": deduplicate(all_adult, max_limit=500)
    }
    
    with open("vod_catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False)
        
    print("Catálogo optimizado y comprimido con éxito, por debajo del límite de GitHub.")

if __name__ == "__main__":
    main()

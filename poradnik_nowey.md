# Poradnik instalacji i konfiguracji

## 1. Instalacja FFmpeg

### Pobranie

-   Wejdź na stronę: `https://ffmpeg.org/download.html`
-   Pobierz wersję dla Windows

### Instalacja

1.  Rozpakuj pobrany ZIP do folderu, np. `C:\ffmpeg`
2.  Dodaj ścieżkę `C:\ffmpeg\bin` do zmiennej środowiskowej **PATH**:
    -   PPM na **Ten komputer** → **Właściwości**
    -   **Zaawansowane ustawienia systemu**
    -   **Zmienne środowiskowe**
    -   Edytuj zmienną **Path**
    -   Dodaj: `C:\ffmpeg\bin`
    -   Zatwierdź OK

### Weryfikacja

``` bash
ffmpeg -version
```

------------------------------------------------------------------------

## 2. Instalacja ngrok

### Pobranie

-   `https://ngrok.com/download`

### Konfiguracja

``` bash
ngrok config add-authtoken <twój_authtoken>
ngrok version
```

------------------------------------------------------------------------

## 3. Instalacja FastAPI i Uvicorn

``` bash
pip install fastapi uvicorn
```

------------------------------------------------------------------------

## 4. Instalacja VB-Audio (Virtual Cable)

Pobierz: `https://vb-audio.com/Cable/`\
Zainstaluj i uruchom ponownie komputer.

------------------------------------------------------------------------

## 5. Konfiguracja OBS

Ustaw wyjście audio na:

    CABLE in 16th (VB-Audio Virtual Cable)

------------------------------------------------------------------------

## 6. Konfiguracja Streamer Bota --- alerty dźwiękowe Kick w IRL ✅

Ta sekcja pozwala na to, aby **alerty dźwiękowe z Kicka były słyszalne
podczas streamów IRL**.

### Ustawienia w Streamer Bot

1.  Otwórz **Actions** i znajdź alerty Kick (np. sub, follow, donate)
2.  W **Sub-actions** dla każdego alertu ustaw wyjście audio na:

```{=html}
<!-- -->
```
    CABLE INPUT (VB-Audio Virtual Cable)

To powoduje, że dźwięk alertów przechodzi przez wirtualny kabel audio.

### Wykrycie urządzenia i dodanie do server.py

W terminalu wpisz:

``` bash
ffmpeg -list_devices true -f dshow -i dummy
```

Znajdź w wynikach:

    "CABLE Output (VB-Audio Virtual Cable)"

Skopiuj **Alternative name** urządzenia i wpisz w `server.py` jako:

``` python
DEVICE_NAME = r"@device_cm_{twoje_id_urządzenia}"
```

Dzięki temu alerty będą kierowane do telefonu/OBS i słyszalne podczas
IRL.

------------------------------------------------------------------------

## 7. Social Stream Media

Pobierz: `https://github.com/steveseguin/social_stream/releases`\
Skonfiguruj Kick, wklej link czatu do `server.py`.

------------------------------------------------------------------------

## 8. Uruchomienie

``` bash
stream_alerts_kick.bat
```

Na telefonie otwórz adres z ngrok, np.:

    https://xxxx.ngrok.io

Jeśli słyszysz alerty --- działa! ✅

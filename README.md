
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

1.	Zainstaluj program z tego linku https://github.com/steveseguin/social_stream/releases najnowszą wersje dla  Windows lub Linux
2.  Wypakuj i zainstaluj program i uruchom go
3.  Dodaj nową source do Kicka i prowadź tam swoją nazwę kanału
4.  Po utworzeniu zaloguj się klikając w przycisk  ‘Sign-in’ (pamiętaj aby po zalogowaniu zamknąć okno)
5.  Zaznacz opcje Auto Avtive i kllikij w Active Source
6.  Kliknij w ten guzik aby zobaczyć czat i sprawdź czy możesz wysłać wiadomość z tego panelu

<img width="714" height="109" alt="image" src="https://github.com/user-attachments/assets/de93024b-f6fe-41a4-93fe-8d81e9467caa" />

7.  Gdy udało się wysłać wiadomość to możesz zamakać te okno i skopiować link po prawej stronie pod nazwą „Streaming chat (dock & overlay)” i wkleić do pliku server.py do tego podmieniając w infamie zwartość iframe oznaczone cudzysłowach :
   
<img width="945" height="54" alt="image" src="https://github.com/user-attachments/assets/7008a8ce-c55d-4268-b522-eaf44b9faf38" />

8.  Poniżej pod Kick chat musisz wprowadzić swoją nazwę uzytkownika aby widzeć aletry na stronie np:
   
   <img width="697" height="88" alt="image" src="https://github.com/user-attachments/assets/e770ebdd-0f05-43c2-8458-03bcc0d95d23" />




------------------------------------------------------------------------

## 8. Uruchomienie

``` bash
stream_alerts_kick.bat
```

Na telefonie otwórz adres z ngrok, np.:

    https://xxxx.ngrok.io

Jeśli słyszysz alerty --- działa! ✅

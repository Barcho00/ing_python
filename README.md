## Wymagania wstępne
- Python 3.12+

## Przygotowanie środowiska

### Windows

1. Instalacja zależności:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

### Ubuntu - do sprawdzenia

1. Zainstaluj wymagane biblioteki systemowe (jeśli nie masz):

    ```bash
    sudo apt-get update
    sudo apt-get install -y libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libgbm-dev
    ```
2. Instalacja zależności Pythona i Playwrighta:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

### MacOS - do sprawdzenia

1. Instalacja Playwrighta:

    ```bash
    brew install --cask playwright
    ```
2. Instalacja zależności Pythona:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Uruchamianie testów

Aby uruchomić testy:

```bash
pytest
```

Po wykonaniu testów raport jest dostępny w pliku `report.html`

windows:
```
start report.html
```

Zrzuty z testów są dostępne w folderze screenshots

```
./screenshots/
```

# MINI WIKI

Dodatkowe informacje o testach :

+ Czyszczenie folderu screenshots przed każdym testem.
+ Zrzuty ekranu wykonywane są po zakończeniu testów – umożliwia to wizualną weryfikację. 
+ Aby __debugować testy z podglądem__, należy wyłączyć tryb headless w pliku conftest.py.
+ __Konfiguracja ilości wątków__ w pliku pytest za pomocą parametru `-n 4` gdzie 4 oznacza ilość wątków w których mają się uruchomić testy
+ Wybór przeglądarek do testów odbywa się bezpośrednio w plikach testowych, poprzez parametryzację testów. Możliwe jest także ustawienie globalne, ale wtedy wszystkie wyniki zapisywane są w jednym zbiorczym casie w raporcie.
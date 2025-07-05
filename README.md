## Wymagania wstępne
- Python
- Node.js (najlepiej LTS)

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

```
./report.html
```

Zrzuty z testów są dostępne w folderze screenshots

```
./screenshots/
```

# MINI WIKI

Dodatkowe informacje o testach :

+ Czyszczenie folderu screenshots przed każdym testem
+ Zrzuty pod koniec testów - możliwe zweryfikowanie wizualne 
+ Aby __umożliwić debugowanie__ aktualnej sesji z podglądem można wyłączyć tryb headles w pliku conftest.py w głównym katalogu.
+ __Konfiguracja ilości wątków__ w pliku pytest za pomocą parametru `-n 4` gdzie 4 oznacza ilość wątków w których mają się uruchomić testy
+ __Konfigurowanie przeglądarek__ obywa się w pliku z testami poprzez parametryzowanie przy konkretnym teście - jest możliwość również globalnego ustawienia przeglądarek ale wynik z był zapisywany pod jednym "resultem"
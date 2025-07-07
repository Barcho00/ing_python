## Wymagania wstępne
- Python 3.12+

## Przygotowanie środowiska

### Windows

1. Instalacja zależności:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

### Ubuntu 

1. Zainstaluj wymagane biblioteki systemowe 

    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install -y git python3 python3-pip
    pip install playwright
    python3 -m playwright install --with-deps

    ```
2. Instalacja zależności Pythona i Playwrighta:

    ```bash
    pip install -r requirements.txt
    ```




## Uruchamianie testów Windows

Aby uruchomić testy:

```bash
pytest
```

Po wykonaniu testów raport jest dostępny w pliku `start test-reports/index.html`

windows:
```
start test-reports/index.html
```

Zrzuty z testów są dostępne w folderze screenshots

```
./screenshots/
```

## Uruchamianie testów Ubuntu:

TO DO

# MINI WIKI

Dodatkowe informacje o testach :

+ Czyszczenie folderu screenshots przed każdym testem.
+ Zrzuty ekranu wykonywane są po zakończeniu testów – umożliwia to wizualną weryfikację. 
+ Aby __debugować testy z podglądem__, należy wyłączyć tryb headless w pliku conftest.py.
+ __Konfiguracja ilości wątków__ w pliku pytest za pomocą parametru `-n 4` gdzie 4 oznacza ilość wątków w których mają się uruchomić testy
+ Wybór przeglądarek do testów odbywa się bezpośrednio w plikach testowych, poprzez parametryzację testów. Możliwe jest także ustawienie globalne, ale wtedy wszystkie wyniki zapisywane są w jednym zbiorczym CASE-ie w raporcie.
+ Raport po autodeployu dostepny w lokalizacji https://barcho00.github.io/ing_python/
+ Workflow dostępny pod https://github.com/Barcho00/ing_python/actions
+ TODO: Dodanie flagi sterującej printami (aka. verbose) aby zostawić tylko niezbędne printy 
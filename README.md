# VentraeMovies
System rekomendacji filmów, bada gust użytkownika i rekomenduje filmy na podstawie ocen użytkownika. System stworzony w architekturze mikroserwisów. Serwis `default` to SPA napisana we frameworku Vue.js, a `api` to aplikacja pythonowa napisana we frameworku Flask.

---

##### Projekt dostępny pod adresem: https://projektarc.appspot.com/#/

---

### Technologie:
* Google Cloud Platform (cloud computing):
    - AppEngine
    - Firestore
    - Cloud Tasks, Cron
    - BigQuery (DataStudio)
* Aplikacja frontendowa:
    - Vue.js (SPA framework)
    - VueRouter, Vuex, VueResource
    - Babel
* Aplikacja backendowa:
    - Python3
    - Flask
* Zewnętrzne platformy:
    - API themoviedb.com
    - SendGrid
    
---

### Funkcjonalności:
* Logowanie, rejestracja
* Wyświetlanie listy najpopularniejszych filmów (w postaci plakatów)
* Widok szczegółowy filmu z danymi, obsadą i komentarzami
* Możliwość oceny filmu w skali 1-10 gwiazdek
* Widok z filmami rekomendowanymi użytkownikowi na podstawie jego ocen
* Widok z ocenami użytkownika, sortowany malejąco po dacie
* Możliwość skomentowania filmu, jeśli się go obejrzało.
* Wysyłanie cotygodniowego maila z losowymi polecanymi filmami
* Analiza i wizualizacja danych w BigQuery i DataStudio
* Możliwość zarządzania kontem (zmiana hasła, usunięcie konta, przypominanie hasła, rezygnacja z newslettera)


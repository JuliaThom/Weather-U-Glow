import pg8000   # Modul für die Verbindung zur PostgreSQL Datenbank
import requests     # Modul für den API-Aufruf
from datetime import datetime   # Zeitstempel

# # Funktion zum Abrufen von Wetterdaten von der API und Speichern in der Datenbank
def fetch_weather_data():
    # Daten aus der API abrufen
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=7b256a5921981a44c938b40908d30411'
    response = requests.get(url)    # GET-Anfrage an die API senden
    data = response.json()  # Die Antwort in das JSON-Format umwandeln
    # RESTful API an, die JSON zur Datenübertragung verwendet.


    # Daten aus der API parsen
    if 'main' in data and 'wind' in data:
        # Überprüfen, ob die erforderlichen Daten in der Antwort enthalten sind
        city = data['name']     # Stadtname aus den API-Daten extrahieren
        temperature = data['main']['temp']  # Temperatur aus den API-Daten extrahieren
        wind_speed = data['wind']['speed']  # Windgeschwindigkeit aus den API-Daten extrahieren
        temp_max = data['main']['temp_max']     # Maximale Temperatur aus den API-Daten extrahieren
        temp_min = data['main']['temp_min']     # Minimale Temperatur aus den API-Daten extrahieren
        timestamp = datetime.now()  # Aktuelles Datum und Uhrzeit als Zeitstempel

        # Daten in die Datenbank speichern
        save_to_database(timestamp, city, temperature, wind_speed, temp_max, temp_min)
    else:
        print("Fehler: Keine Daten gefunden.")


# Funktion zum Speichern der Wetterdaten in die Datenbank
def save_to_database(timestamp, city, temperature, wind_speed, temp_max, temp_min):
    try:
        # Verbindung zur Datenbank herstellen
        conn = pg8000.connect(
            database='weather',     # Name der Datenbank, zu der eine Verbindung hergestellt werden soll
            user='postgres',    # Benutzername für die Datenbankverbindung
            password='Monster',      # Passwort für die Datenbankverbindung
            host='localhost',   # Hostname oder IP-Adresse des Servers, auf dem die Datenbank läuft
            port=5432   # Port, über den die Verbindung hergestellt wird (standardmäßig 5432 für PostgreSQL)
        )

        # Cursor erstellen
        cur = conn.cursor()

        # Daten in die Tabelle einfügen
        cur.execute(
            "INSERT INTO weather_data (timestamp, city, temperature, wind_speed, temp_max, temp_min) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (timestamp, city, temperature, wind_speed, temp_max, temp_min)
        )

        # Änderungen bestätigen und Cursor schließen
        conn.commit()    # Änderungen in die Datenbank übernehmen
        cur.close()     # Cursor schließen, um Ressourcen freizugeben

    except pg8000.Error as e:
        print('Fehler beim Speichern der Daten in die Datenbank:', e)


# Hauptprogramm: Ausführen der fetch_weather_data-Funktion
# beim direkten Ausführen dieses Skripts
if __name__ == "__main__":
    fetch_weather_data()
    # Aufruf der fetch_weather_data-Funktion,
    # um die Wetterdaten abzurufen und zu speichern

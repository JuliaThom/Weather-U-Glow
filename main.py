import pg8000
import requests
from datetime import datetime


def fetch_weather_data():
    # Daten aus der API abrufen
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Rome&appid=7b256a5921981a44c938b40908d30411'
    response = requests.get(url)
    data = response.json()

    # Daten aus der API parsen
    if 'main' in data and 'wind' in data:
        city = data['name']
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        timestamp = datetime.now()

        # Daten in die Datenbank speichern
        save_to_database(timestamp, city, temperature, wind_speed, temp_max, temp_min)
    else:
        print("Fehler: Keine Daten gefunden.")


def save_to_database(timestamp, city, temperature, wind_speed, temp_max, temp_min):
    try:
        # Verbindung zur Datenbank herstellen
        conn = pg8000.connect(
            user='postgres',
            password='Monster',
            host='localhost',
            port=5432
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
        conn.commit()
        cur.close()

    except pg8000.Error as e:
        print('Fehler beim Speichern der Daten in die Datenbank:', e)


if __name__ == "__main__":
    fetch_weather_data()

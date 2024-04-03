import requests
from datetime import datetime
import psycopg2



def fetch_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=7b256a5921981a44c938b40908d30411'
    response = requests.get(url)
    data = response.json()

    if 'main' in data and 'wind' in data:
        city = data['name']
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        timestamp = datetime.now()
        save_to_database(timestamp, city, temperature, wind_speed, temp_max, temp_min)
    else:
        print("Fehler: Keine Daten gefunden.")


def save_to_database(timestamp, city, temperature, wind_speed, temp_max, temp_min):
    conn = psycopg2.connect(
        dbname='weather',
        user='postgres',
        password='Monster',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO weather_data (timestamp, city, temperature, wind_speed, temp_max, temp_min) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (timestamp, city, temperature, wind_speed, temp_max, temp_min)
    )
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    fetch_weather_data()
# Importieren der benötigten Module
from kivy.app import App    # Import der App-Klasse aus dem kivy-Modul
from kivy.uix.boxlayout import BoxLayout    # Import der BoxLayout-Klasse aus dem kivy.uix-Modul
# (uix → User Interface Extensions)
from kivy.uix.label import Label    # Import der Label-Klasse aus dem kivy.uix-Modul
from kivy.uix.button import Button      # Import der Button-Klasse aus dem kivy.uix-Modul
import pg8000   # Import der pg8000-Bibliothek für die PostgreSQL-Datenbankanbindung


# Definition der WeatherApp-Klasse, die von der App-Klasse von Kivy erbt
class WeatherApp(App):
    # Methode zum Erstellen des GUIs der Anwendung
    def build(self):
        # Erstellung eines vertikalen BoxLayouts für die Anordnung der Widgets
        self.layout = BoxLayout(orientation='vertical')

        # Erstellung von Labels für die Anzeige von Wetterinformationen und Hinzufügen zum Layout
        self.label_city = Label(text='Stadt: ')
        self.layout.add_widget(self.label_city)

        self.label_temp = Label(text='Temperatur: ')
        self.layout.add_widget(self.label_temp)

        self.label_wind = Label(text='Windgeschwindigkeit: ')
        self.layout.add_widget(self.label_wind)

        self.label_max_temp = Label(text='Maximale Temperatur: ')
        self.layout.add_widget(self.label_max_temp)

        self.label_min_temp = Label(text='Minimale Temperatur: ')
        self.layout.add_widget(self.label_min_temp)

        self.label_timestamp = Label(text='Letztes Update: ')
        self.layout.add_widget(self.label_timestamp)

        # Erstellung eines Buttons zum Aktualisieren der Wetterdaten und Binden an die refresh_data-Methode
        refresh_button = Button(text='Daten aktualisieren')
        # Änderung: Verwendung von `lambda` für den Funktionsaufruf ohne Argumente
        refresh_button.bind(on_press=lambda _: self.refresh_data())
        self.layout.add_widget(refresh_button)

        # Abrufen und Anzeigen der Wetterdaten
        self.fetch_weather_data()

        # Rückgabe des Layouts als GUI der Anwendung
        return self.layout

    # Methode zum Abrufen und Anzeigen der Wetterdaten
    def fetch_weather_data(self):
        # Verbindung zur PostgreSQL-Datenbank herstellen
        conn = pg8000.connect(
            database='weather',     # Name der Datenbank, zu der eine Verbindung hergestellt werden soll
            user='postgres',     # Benutzername für die Datenbankverbindung
            password='Monster',    # Passwort für die Datenbankverbindung
            host='localhost',   # Hostname oder IP-Adresse des PostgreSQL-Servers
            port='5432'     # Port, über den die Verbindung hergestellt wird (standardmäßig 5432 für PostgreSQL)
        )

        # Cursor erstellen und die neuesten Wetterdaten abrufen
        cur = conn.cursor()
        cur.execute('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 1')
        data = cur.fetchone()
        cur.close()
        conn.close()

        # Wenn Daten vorhanden sind, die Label mit den Wetterinformationen aktualisieren
        if data:
            timestamp, city, temperature, wind_speed, temp_max, temp_min = data[1:]
            temperature_celsius = temperature - 273.15 # Inkl. Umwandlung Kelvin → Celsius
            self.label_city.text = f'Stadt: {city}'
            self.label_temp.text = f'Temperatur: {temperature_celsius:.2f} °C'
            self.label_wind.text = f'Windgeschwindigkeit: {wind_speed} m/s'
            self.label_max_temp.text = f'Maximale Temperatur: {temp_max - 273.15:.2f} °C'
            self.label_min_temp.text = f'Minimale Temperatur: {temp_min - 273.15:.2f} °C'
            self.label_timestamp.text = f'Letztes Update: {timestamp}'
        else:
            # Wenn keine Daten gefunden wurden, eine Meldung ausgeben
            print('Keine Daten gefunden.')

    # Methode zum Aktualisieren der Wetterdaten bei Betätigung des Aktualisierungsbuttons
    def refresh_data(self):
        self.fetch_weather_data()


# Überprüfen, ob das Skript direkt ausgeführt wird, und Ausführen der WeatherApp
if __name__ == "__main__":
    WeatherApp().run()

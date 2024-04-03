from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import pg8000

class WeatherApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

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

        refresh_button = Button(text='Daten aktualisieren')
        refresh_button.bind(on_press=self.refresh_data)
        self.layout.add_widget(refresh_button)

        self.fetch_weather_data()

        return self.layout

    def fetch_weather_data(self):
        conn = pg8000.connect(
            user='postgres',
            password='Monster',
            host='localhost',
            port=5432
        )
        cur = conn.cursor()
        cur.execute('SELECT city, temperature, wind_speed, temp_max, temp_min FROM weather_data ORDER BY timestamp DESC LIMIT 1')
        data = cur.fetchone()
        cur.close()
        conn.close()

        if data:
            city, temperature, wind_speed, temp_max, temp_min = data
            self.label_city.text = f'Stadt: {city}'
            self.label_temp.text = f'Temperatur: {temperature} °C'
            self.label_wind.text = f'Windgeschwindigkeit: {wind_speed} m/s'
            self.label_max_temp.text = f'Maximale Temperatur: {temp_max} °C'
            self.label_min_temp.text = f'Minimale Temperatur: {temp_min} °C'
        else:
            print('Keine Daten gefunden.')

    def refresh_data(self, instance):
        self.fetch_weather_data()

if __name__ == "__main__":
    WeatherApp().run()
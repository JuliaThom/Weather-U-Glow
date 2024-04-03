from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests


class WeatherUI(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.api_key = 'YOUR_API_KEY'

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.city_input = TextInput(hint_text='Enter city name')
        layout.add_widget(self.city_input)

        self.weather_label = Label(text='', size_hint_y=0.8)
        layout.add_widget(self.weather_label)

        refresh_button = Button(text='Refresh', size_hint_y=0.2)
        refresh_button.bind(on_press=self.fetch_weather_data)
        layout.add_widget(refresh_button)

        return layout

    def fetch_weather_data(self, instance):
        city = self.city_input.text.strip()
        if city:
            url = f'{self.base_url}?q={city}&appid={self.api_key}'
            response = requests.get(url)
            data = response.json()
            if 'main' in data and 'weather' in data:
                weather_desc = data['weather'][0]['description']
                temperature = data['main']['temp']
                self.weather_label.text = f'Weather: {weather_desc}, Temperature: {temperature}K'
            else:
                self.weather_label.text = 'Error: No data found.'
        else:
            self.weather_label.text = 'Please enter a city name.'


if __name__ == '__main__':
    WeatherUI().run()
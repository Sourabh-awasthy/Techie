import requests
from uagents import Agent

# Define the Weather API URL (replace with a real weather API endpoint)
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=960ded1d33bf1a0b60cc8d5d7432bcb1"

class TemperatureAlertAgent(Agent):
    def __init__(self, name, location, min_temp, max_temp):
        super().__init__(name=name)
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp

    def check_temperature(self):
        try:
            # Fetch real-time temperature data from the Weather API
            response = requests.get(WEATHER_API_URL)
            response.raise_for_status()
            weather_data = response.json()

            # Extract the current temperature from the API response
            current_temperature = weather_data.get("main", {}).get("temp")

            # Check if the temperature is outside the specified range
            if current_temperature is not None:
                if current_temperature < self.min_temp:
                    self.send_alert(f"Temperature in {self.location} is below {self.min_temp}°C.")
                elif current_temperature > self.max_temp:
                    self.send_alert(f"Temperature in {self.location} is above {self.max_temp}°C.")
                else:
                    print(f"Temperature in {self.location} is within the desired range.")
            else:
                print("Temperature data not available in the API response.")

        except Exception as e:
            print(f"Error fetching temperature data: {str(e)}")

    def send_alert(self, message):
        # Replace this with your preferred method of sending alerts (e.g., email, SMS)
        print(f"ALERT: {message}")

if __name__ == "__main__":
    # Create a TemperatureAlertAgent instance
    agent = TemperatureAlertAgent(
        name="MyTemperatureAgent",
        location="YourLocation",
        min_temp=20,  # Set your preferred minimum temperature
        max_temp=30,  # Set your preferred maximum temperature
    )

    while True:
        agent.check_temperature()

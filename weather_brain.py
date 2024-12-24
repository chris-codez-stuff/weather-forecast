def clothing_suggestion(data):
    city = data["location"]["name"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"].lower()
    uv_index = data["current"]["uv"]
    wind_speed = data["current"]["wind_kph"]

    suggestions = f"In {city}, the weather is currently {temp}°C with {condition}. Here's what you should wear:\n"

    if temp < 10:
        suggestions += "- It's very cold. Wear a heavy jacket, scarf, and gloves to stay warm.\n"
    elif 10 <= temp < 20:
        suggestions += "- The temperature is a bit chilly. A sweater or hoodie would be comfortable.\n"
    elif 20 <= temp < 30:
        if uv_index > 5:
            suggestions += "- It's warm and sunny. Wear a t-shirt, sunglasses, and apply sunscreen to protect yourself from UV rays.\n"
        else:
            suggestions += "- The temperature is moderate. Light, casual clothing would be perfect.\n"
    else:
        suggestions += "- It's hot. Wear summer clothing like shorts and a cotton shirt to stay cool.\n"

    if "rain" in condition:
        suggestions += "- Rain is expected. Carry an umbrella or wear a raincoat to stay dry.\n"

    if wind_speed > 20:
        suggestions += f"- It's windy with speeds around {wind_speed} km/h. A windproof jacket will help protect you.\n"

    return suggestions


def generate_weather_forecast(data):
    location = data.get("location", {})
    current = data.get("current", {})
    
    city = location.get("name", "Unknown Location")
    country = location.get("country", "")
    localtime = location.get("localtime", "N/A")
    
    temp_c = current.get("temp_c", "N/A")
    condition = current.get("condition", {}).get("text", "N/A")
    wind_kph = current.get("wind_kph", "N/A")
    humidity = current.get("humidity", "N/A")
    uv_index = current.get("uv", "N/A")
    feels_like = current.get("feelslike_c", "N/A")
    
    forecast = (
        f"Weather Forecast for {city}, {country}:\n"
        f"- Local Time: {localtime}\n"
        f"- Temperature: {temp_c}°C (Feels like {feels_like}°C)\n"
        f"- Condition: {condition}\n"
        f"- Wind Speed: {wind_kph} km/h\n"
        f"- Humidity: {humidity}%\n"
        f"- UV Index: {uv_index}\n"
    )
    
    return forecast

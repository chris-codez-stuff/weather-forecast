import speech_recognizer as sr
import text_to_speech as tts
import weather_forecaster as wf
import weather_brain as wb

print("Weather forecast")

tts.speak("Welcome to weather forecast app!")
tts.speak("Here are the list of functions that can be performed, enter the corresponding number for the action to be executed!")

while True:
    print("1. Get weather forecast")
    print("2. Get clothing suggestion")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":

        tts.speak("Tell the city you are from, to start recording enter Y")
        start = input("Start recording (Y/n): ")

        if start.lower() == "y":
            sr.record_audio("output.wav", 4, 16000)
            city = sr.recognize_speech_from_audio("output.wav")

            data = wf.get_weather(city)
            weather_forecast = wb.generate_weather_forecast(data)

            print(weather_forecast)
            tts.speak(weather_forecast)
        else:
            continue
    elif choice == "2":
        tts.speak("Tell the city you are from, to start recording enter Y")
        start = input("Start recording (Y/n): ")

        if start.lower() == "y":
            sr.record_audio("output.wav", 4, 16000)
            city = sr.recognize_speech_from_audio("output.wav")

            data = wf.get_weather(city)
            clothing_suggestion = wb.clothing_suggestion(data)

            print(clothing_suggestion)
            tts.speak(clothing_suggestion)
    elif choice == "3":
        tts.speak("Ok see you later!")
        break
    else:
        continue
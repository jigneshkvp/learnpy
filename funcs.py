def weather_condition(temp: float) -> str:
    if temp > 7:
        return "Warm"
    else:
        return "Cold"


user_temp = input("Enter a temperature: ")

print(weather_condition(float(user_temp)))

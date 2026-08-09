temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 25:
    if temperature <= 40:
        print("The temperature is suitable for wearing light clothes.")
    else:
        print("It is too hot outside!")
else:
    print("It is too cold, you should wear a jacket or pullover.")

print("This is a Simple Unit Converter")

print("What do you want to do ? (1,2,3,4) \n"
      "1. C to K\n"
      "2. K to C\n"
      "3. F to C\n"
      "4. C to F\n")

select = input()

temperature = input("Enter the temperature: ")

# def celsius_to_kelvin(temp):
#     return float(temp) + 273.15

# def kelvin_to_celsius(temp):
#     return float(temp) - 273.15

# def fahrenheit_to_celsius(temp):
#     return (float(temp) - 32) * 5 / 9

# def celsius_to_fahrenheit(temp):
#     return (float(temp) * 9 / 5) + 32

# if select == "1":
#     result = celsius_to_kelvin(temperature)
#     print(f"{temperature} °C is {result} K")

# elif select == "2":
#     result = kelvin_to_celsius(temperature)
#     print(f"{temperature} K is {result} °C")

# elif select == "3":
#     result = fahrenheit_to_celsius(temperature)
#     print(f"{temperature} °F is {result} °C")

# elif select == "4":
#     result = celsius_to_fahrenheit(temperature)
#     print(f"{temperature} °C is {result} °F")

# else:
#     print("Invalid selection")



if select == "1":
    print(float(temperature)+273)

elif select == "2":
    print(float(temperature)-273)

elif select == "3":
    print((float(temperature)-32)*(5/9))

elif select == "4":
    print(float(temperature)*(9/5)+32)
else:
    print("Invalid selection")
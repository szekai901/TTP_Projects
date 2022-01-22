def temp(pick,num):
    pick=int(pick)
    num=int(num)
    if pick == 1:
        celcius = (num-32) * 5/9
        kelvin = (num-32) * 5/9 + 273.15
        print("celcius= " + str(celcius))
        print("kelvin= " + str(kelvin))
    if pick == 2:
        fahrenheit = (num*9/5) + 32
        kelvin = num + 273.15
        print("farenheit= " + str(fahrenheit))
        print("kelvin= " + str(kelvin))
    if pick == 3:
        farenheit = (num-273.15) * 9/5 + 32
        celcius = num - 273.15
        print("farenheit= " + str(farenheit))
        print("celcius= " + str(celcius))
        
print("Pick a temperature: 1. Farenheit, 2. Celcius, 3. Kelvin")
pick = input("input: ")
num = input("Enter the degrees: ")
temp(pick,num)
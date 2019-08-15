import pyowm

owm = pyowm.OWM('TOKEN') #can use mine f264aeb8ca0f3f986f6ab19c7b7c0184
print ("Console GisMeteo")
def gis():
	city = input("City: ")
	observation = owm.weather_at_place(city)
	w = observation.get_weather()
	time = w.get_reference_time(timeformat='iso')
	print(time)

	humidity = w.get_humidity()
	print ("Humidity:", str(humidity) + "%")

	pressure = w.get_pressure()['press'] 
	print("Pressure:", str(pressure-290))

	rain = w.get_rain()
	if rain == { }:
		rain = "Нет"
	print("Precipitation:", str(rain))

	status = w.get_detailed_status()
	print ("Небо:", str(status))

	wind = w.get_wind()['speed']       
	print ("Wind speed:",str(wind), 'м/с')

	t = w.get_temperature('celsius')['temp']
	print("Temperature:", str(t), 'degrees')

	sunrise = w.get_sunrise_time('iso')
	print("Sunset:", sunrise)

	sunset = w.get_sunset_time('iso')
	print("Sunrise:", sunset) 

choice = "y"
while choice.lower() == "y":
	gis()
choice = input("To continue, press Y, and to exit, any other key: ")
print("The program is shut down")
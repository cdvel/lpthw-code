def weather_forecast(conditions, temperature):
	print "Today\'s forecast is:"
	print "The weather\'s %s and you enjoy %dC \n" % (conditions, temperature)
	pass

print "Call the forecast x10"

sun = 'sunny'
cloud = 'cloudy'
shower = 'showers'
rain = 'rainy'

temp = 22

weather_forecast('sunny', 19)
weather_forecast('foggy', 19-5)
weather_forecast(cloud, temp)
weather_forecast(cloud +' with '+shower, temp -10)
weather_forecast(rain, 19)
weather_forecast(sun, 2*10)
weather_forecast('intermittent' + ' ' + shower, 9)
weather_forecast('nice', temp)
weather_forecast('super '+ 'nice', 22)
weather_forecast(rain, 11-1)

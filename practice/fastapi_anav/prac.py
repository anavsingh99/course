import pyowm

#APIKEY= '03f6f7e2a6de6ff65f3a24e46cd8930c'    #your API Key here as string
#OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
#Weather=OpenWMap.weather_at_place('London')  # give where you need to see the weather
#Data=Weather.get_weather()                   # get out data in the mentioned location

#temp = Data.get_temperature(unit='celsius')      # get current temparature in celsius 
#print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
#print ("Max Temp. Currently ", temp['temp_max']) # get max tmp
#print ("Min Temp. Currently ", temp['temp_min']) # get min tmp>>

#owm = pyowm.OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
#mgr = owm.weather_manager()
#obs = mgr.weather_at_place('Delhi')
#w = obs.weather
#print(w.status)

def get_temp(loc: str):
    owm = pyowm.OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
    mgr = owm.weather_manager()
    loc2 = loc.title()
    obs = mgr.weather_at_place(loc2)
    w = obs.weather
    t = w.temperature(unit='fahrenheit')
    print(t['temp'])

#get_temp('new york')

owm = pyowm.OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
mgr = owm.weather_manager()
obs = mgr.weather_at_place('London')
w = obs.weather
t = w.temperature(unit='fahrenheit')
print(w)
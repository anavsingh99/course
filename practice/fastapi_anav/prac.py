from pyowm.owm import OWM

owm = OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
mgr = owm.weather_manager()
three_h_forecast = mgr.forecast_at_place('New York', '3h')
print(three_h_forecast.weather)

from pyowm.utils import timestamps
from pyowm.owm import OWM
owm = OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
mgr = owm.weather_manager()
three_h_forecaster = mgr.forecast_at_place('Charlottesville', '3h')
tomorrow_at_five = timestamps.tomorrow(17, 0)                      # datetime object for tomorrow at 5 PM
weather = three_h_forecaster.get_weather_at(tomorrow_at_five) 
print(weather.status)

from pyowm.utils import timestamps
from pyowm.owm import OWM
owm = OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
mgr = owm.weather_manager()
three_h_forecaster = mgr.forecast_at_place('Charlottesville', '3h')
tomorrow_at_five = timestamps.tomorrow(17, 0)                      # datetime object for tomorrow at 5 PM
weather = three_h_forecaster.weather()
print(weather.status)

def forecast(loc: str, hr: int):
    owm = OWM('03f6f7e2a6de6ff65f3a24e46cd8930c')
    mgr = owm.weather_manager()
    loc2 = loc.title()
    three_h_forecaster = mgr.forecast_at_place(loc2, '3h')
    tomorrow_at_five = timestamps.tomorrow(hr, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_five) 
    return {"Location": loc2, "Forecast For": 'Tomorrow', "24 Hour": hr , "Status": weather.status}

forecast('singapore', 8)
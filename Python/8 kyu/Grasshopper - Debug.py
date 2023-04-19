def weather_info(t):
    c =  convert_to_celsius(t)
    return str(c) + " is freezing temperature" if c < 0 else str(c) + " is above freezing temperature"
    
def convert_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)

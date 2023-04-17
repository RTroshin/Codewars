def weather_info(t):
    c =  convert_to_celsius(t)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)

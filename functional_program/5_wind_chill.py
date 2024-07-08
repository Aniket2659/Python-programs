def wind_chill(t,v):
    if t<50 and (3<t<120): # use condition
        return round((35.74 + 0.6215*t +(0.4275*t-35.75)*(v**0.16)) ,2) # return equation
    else:
        print('plz choose apropriate value of t and v')
temp=int(input('enter a temperature in Farenhite :'))
wind_speed=int(input('enter a valid speed :'))
print(wind_chill(temp,wind_speed))
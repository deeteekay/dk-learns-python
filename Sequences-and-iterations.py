#!/usr/bin/env python
# coding: utf-8
# In[26]:
# Define immutable day-of-week & weather forecast for the week
dayOfWeek = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
weekWeatherForecast = ["rain", "rain", "sunny", "cloudy", "cloudy", "cloudy", "rain"]

# In[27]:
# Define what equipment needed for the day's weather
def equipmentToday(weather):
    if weather == "rain":
        return "umbrella!"
    elif weather == "sunny":
        return "sunscreen!"
    elif weather == "cloudy":
        return "sunscreen, if desired."
    else:
        return "...never mind!" #undefined weather; execution should never reach here

# In[36]:
# Set up initial conditions for WHILE loop
exitLoop = "n"
while (exitLoop != "y"):

    # Obtain day from user
    today = input("What day is it today? ")

    # Prepare the string by taking first three letters and capitalize, if needed.
    today=today[0:3]
    today=today.capitalize()

    # Find today's weather
    if today in dayOfWeek:
        indx = dayOfWeek.index(today) #grab index
        weatherToday = weekWeatherForecast[indx] #find today's weather
        stuff = equipmentToday(weatherToday) #find today's stuff
        print("Don't forget your", stuff,"!")
    else:
        print ("Incorrect day entered")
		
	#print weather forecast (at user's request)    
    showforecast=input("Would you like to see the week's forecast [y/n]?")
    if showforecast == 'y':
        for i in range(7):
            print (dayOfWeek[i] + ": " + weekWeatherForecast[i] + ". ")
    
    # Ask if user would like to exit 
    exitLoop=input("Would you like to exit [y/n]?")
    isExit = exitLoop.lower()
    if exitLoop == 'y':
        break

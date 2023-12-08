#Defining the function to convert time from 12 hour to 24 hour format

def time_convertor(hr, min, time_period):

    #Since we add 12 once the clock passes 12pm in the 24 hour clock format, we check if the time period is pm and if the time is not equal to 12 (after 12 pm, 12 is added to all subsequent hours)
    if time_period == "pm" and hr != 12:
        hr +=12

    #Setting the hour to equal 0 for all hours between 12 am and 12 pm
    elif time_period== "am" and hr==12:
        hr=0

    #Formatting the result to become a four digit string
    #02-> width of the input field: in this case the width of the hour and minute inputs
        #Even if the hour has only one digit, a zero will be added to it by default because of the specified format
    time="{:02d}{:02d}".format(hr,min) #outputting the result in decimal format
    print(time)

time_convertor(1,30,"am")
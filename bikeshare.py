## TODO: import all necessary packages and functions
import csv
import time
import datetime
import calendar

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

month = 'january'
day = 0

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function

    while city.lower() != 'chicago' and city.lower()!= 'new york' and city.lower()!= 'washington':
        city = input('\nPlease enter the valid city name!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')

    return city

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) time period as either month, day or none
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    global month
    global day

    while time_period.lower() != 'month' and time_period.lower()!= 'day' and time_period.lower()!= 'none':
        time_period = input('\nPlease enter the valid filter!\n'
                     'Would you like to filter the data by month, day, or not at'
                                         ' all? Type "none" for no time filter.\n')

    if time_period.lower() == 'month':
        month = get_month()
    elif time_period.lower() == 'day':
        day = get_day()
    elif time_period.lower() == 'none':
        time_period = 'none'

    return time_period

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) Name of the month
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function

    months = ['january','february','march','april','may','june','july','august','september','october','november','december']

    while month.lower() not in months:
        month = input('\nPlease enter the month between January and December\n')

    return month

def get_day( ):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (int) Day of the week
    '''
    day = int(input('\nWhich day? Please type your response as an integer.\n'))

    # TODO: handle raw input and complete function

    while day > 7:
        day = int(input('\nPlease enter your day Which represents day of the week?'
                         ' Please type your response as an integer.\n'))

    return day

def popular_month(city_file, time_period):
    '''Finds the most popular month in the start time and returns the name of the month

    Args:
        file name, time period
    Returns:
        (str) Name of the month
    '''
    # TODO: complete function
    months = { 'january' : 0, 'february' : 0, 'march' : 0, 'april' : 0, 'may' : 0,
               'june' : 0, 'july' : 0, 'august' : 0, 'september' : 0, 'october' : 0,
               'november' : 0, 'december' : 0 }

    for dictionary in city_file:
        for key, value in dictionary.items():
            if key.lower() == 'start time':
                month = int(value.split(' ')[0].split('-')[1])
                if month == 1:
                    months['january'] += 1
                elif month == 2:
                    months['february'] += 1
                elif month == 3:
                    months['march'] += 1
                elif month == 4:
                    months['april'] += 1
                elif month == 5:
                    months['may'] += 1
                elif month == 6:
                    months['june'] += 1
                elif month == 7:
                    months['july'] += 1
                elif month == 8:
                    months['august'] += 1
                elif month == 9:
                    months['september'] += 1
                elif month == 10:
                    months['october'] += 1
                elif month == 11:
                    months['november'] += 1
                elif month == 12:
                    months['december'] += 1

    return max( months, key = months.get )

def day_c(days, day):
    '''Updates the value for each key in the days dictionary

    Args:
        days, day
    Returns:
        None
    '''
    if day == 1:
        days['Monday'] += 1
    elif day == 2:
        days['Tuesday'] += 1
    elif day == 2:
        days['Wednesday'] += 1
    elif day == 2:
        days['Thursday'] += 1
    elif day == 2:
        days['Friday'] += 1
    elif day == 2:
        days['Saturday'] += 1
    elif day == 2:
        days['Sunday'] += 1

def popular_day(city_file, time_period):
    '''Finds the most popular day in the start time based on the time period and returns the name of the day in the week

    Args:
        file name, time period
    Returns:
        (str) Name of the day in the week
    '''
    # TODO: complete function
    days = { 'Monday' : 0, 'Tuesday' : 0, 'Wednesday' : 0, 'Thursday' : 0,
             'Friday' : 0, 'Saturday' : 0, 'Sunday' : 0}


    if time_period == 'none':
        for dictionary in city_file:
            for key, value in dictionary.items():
                if key.lower() == 'start time':
                    date = value.split(' ')[0].split('-')
                    date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
                    day = date1.isoweekday()
                    day_c(days,day)

        return max( days, key = days.get )

    elif time_period == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]
        #print(month_num)

        for dictionary in city_file:
            for key, value in dictionary.items():
                if key.lower() == 'start time':
                    date = value.split(' ')[0].split('-')
                    if int(date[1]) == month_num:
                        date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
                        day = date1.isoweekday()
                        day_c(days, day)

        return max( days, key = days.get )

def hour_c(hours, hour):
    '''Updates the value for each key in the hours dictionary

    Args:
        hours, hour
    Returns:
        None
    '''
    if hour == 1:
        hours[1] += 1
    elif hour == 2:
        hours[2] += 1
    elif hour == 3:
        hours[3] += 1
    elif hour == 4:
        hours[4] += 1
    elif hour == 5:
        hours[5] += 1
    elif hour == 6:
        hours[6] += 1
    elif hour == 7:
        hours[7] += 1
    elif hour == 8:
        hours[8] += 1
    elif hour == 9:
        hours[9] += 1
    elif hour == 10:
        hours[10] += 1
    elif hour == 11:
        hours[11] += 1
    elif hour == 12:
        hours[12] += 1
    elif hour == 13:
        hours[13] += 1
    elif hour ==14:
        hours[14] += 1
    elif hour == 15:
        hours[15] += 1
    elif hour == 16:
        hours[16] += 1
    elif hour == 17:
        hours[17] += 1
    elif hour == 18:
        hours[18] += 1
    elif hour == 19:
        hours[19] += 1
    elif hour == 20:
        hours[20] += 1
    elif hour == 21:
        hours[21] += 1
    elif hour == 22:
        hours[22] += 1
    elif hour == 23:
        hours[23] += 1
    elif hour == 24:
        hours[24] += 1

def popular_hour(city_file, time_period):
    '''Finds the most popular hour in the start time based on the time period and returns the hour

    Args:
        file name, time period
    Returns:
        (int) Hour
    '''
    # TODO: complete function

    hours = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0,
              10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0,
              18 : 0, 19 : 0, 20 : 0, 21 : 0, 22 : 0, 23 : 0, 24 : 0 }


    if time_period == 'none':

        for dictionary in city_file:
            for key, value in dictionary.items():
                if key.lower() == 'start time':
                    hour = int(value.split(' ')[1].split(':')[0])
                    hour_c(hours, hour)

        return max( hours, key = hours.get )

    elif time_period == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:
            for key, value in dictionary.items():
                if key.lower() == 'start time':
                    date = value.split(' ')[0].split('-')
                    if int(date[1]) == month_num:
                        hour = int(value.split(' ')[1].split(':')[0])
                        hour_c(hours, hour)

        return max( hours, key = hours.get )

    elif time_period == 'day':

        day1 = day

        for dictionary in city_file:
            for key, value in dictionary.items():
                if key.lower() == 'start time':
                    date = value.split(' ')[0].split('-')
                    date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
                    day_week = date1.isoweekday()
                    if day1 == day_week:
                        hour = int(value.split(' ')[1].split(':')[0])
                        hour_c(hours, hour)

        return max( hours, key = hours.get )

def trip_duration(city_file, time_period):
    '''Finds the total trip time and average trip time from trip duration
       based on the time period and returns total and average trip time

    Args:
        file name, time period
    Returns:
        (int,float) Total trip time and Average trip time
    '''
    # TODO: complete function
    total_trip = 0
    count = 0

    if time_period.lower() == 'none':
        for dictionary in city_file:
            for key, value in dictionary.items():
                if key.lower() == 'trip duration':
                    total_trip += int(float(value))
                    count += 1

        avg_trip = total_trip / count

        return ( total_trip, avg_trip )

    elif time_period.lower() == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:
            date = int(dictionary['Start Time'].split(' ')[0].split('-')[1])
            if date == month_num:
                total_trip += int(float(dictionary['Trip Duration']))
                count += 1

        avg_trip = total_trip / count

        return ( total_trip, avg_trip )

    elif time_period.lower() == 'day':

        day1 = day

        for dictionary in city_file:
            date = list(dictionary['Start Time'].split(' ')[0].split('-'))
            date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            day_week = date1.isoweekday()
            if day1 == day_week:
                total_trip += int(float(dictionary['Trip Duration']))
                count += 1

        avg_trip = total_trip / (count+0.01)

        return ( total_trip, avg_trip )

def popular_stations(city_file, time_period):
    '''Finds the most popular start station and end station based on the
       time period and returns the names of the stations

    Args:
        file name, time period
    Returns:
        (str,str) Name of the start station and name of the end station
    '''
    # TODO: complete function
    start_station = { }
    end_station = { }

    if time_period.lower() == 'none':

        for dictionary in city_file:
            if dictionary['Start Station'] in list(start_station.keys()):
                start_station[dictionary['Start Station']] += 1
            else:
                start_station[dictionary['Start Station']] = 1

            if dictionary['End Station'] in list(end_station.keys()):
                end_station[dictionary['End Station']] += 1
            else:
                end_station[dictionary['End Station']] = 1

        start_key = list(start_station.keys())
        end_key = list(end_station.keys())

        start_value = list(start_station.values())
        end_value = list(end_station.values())

        return ( start_key[start_value.index(max(start_value))], end_key[end_value.index(max(end_value))] )

    elif time_period.lower() == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:
            date = int(dictionary['Start Time'].split(' ')[0].split('-')[1])
            if date == month_num:
                if dictionary['Start Station'] in list(start_station.keys()):
                    start_station[dictionary['Start Station']] += 1
                else:
                    start_station[dictionary['Start Station']] = 1

                if dictionary['End Station'] in list(end_station.keys()):
                    end_station[dictionary['End Station']] += 1
                else:
                    end_station[dictionary['End Station']] = 1

        start_key = list(start_station.keys())
        end_key = list(end_station.keys())

        start_value = list(start_station.values())
        end_value = list(end_station.values())

        return ( start_key[start_value.index(max(start_value))], end_key[end_value.index(max(end_value))] )

    elif time_period.lower() == 'day':

        day1 = day

        for dictionary in city_file:
            date = dictionary['Start Time'].split(' ')[0].split('-')
            date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            day_week = date1.isoweekday()
            if day1 == day_week:
                if dictionary['Start Station'] in list(start_station.keys()):
                    start_station[dictionary['Start Station']] += 1
                else:
                    start_station[dictionary['Start Station']] = 1

                if dictionary['End Station'] in list(end_station.keys()):
                    end_station[dictionary['End Station']] += 1
                else:
                    end_station[dictionary['End Station']] = 1

        return ( max( start_station, key = start_station.get ), max( end_station, key = end_station.get ))

def popular_trip(city_file, time_period):
    '''Finds the most popular trip based on the time period and
       returns the names of the start and end stations with most number of trips

    Args:
        file name, time period
    Returns:
        (str,str) Name of start station and end station
    '''
    # TODO: complete function

    trip = { }

    if time_period == 'none':

        for i, dictionary in enumerate(city_file):
            if i % 10000 == 0:
                print("Running, processed {} rows".format(i))

            if (dictionary['Start Station'],dictionary['End Station']) in list(trip.keys()):
                trip[(dictionary['Start Station'],dictionary['End Station'])] += 1
            else:
                trip[(dictionary['Start Station'],dictionary['End Station'])] = 1

        key = list(trip.keys())
        value = list(trip.values())


        return key[value.index(max(value))]

    elif time_period == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:

            date = int(dictionary['Start Time'].split(' ')[0].split('-')[1])
            if date == month_num:
                if (dictionary['Start Station'],dictionary['End Station']) in list(trip.keys()):
                    trip[(dictionary['Start Station'],dictionary['End Station'])] += 1
                else:
                    trip[(dictionary['Start Station'],dictionary['End Station'])] = 1

        key = list(trip.keys())
        value = list(trip.values())


        return key[value.index(max(value))]

    elif time_period == 'day':

        day1 = day

        for dictionary in city_file:

            date = dictionary['Start Time'].split(' ')[0].split('-')
            date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            day_week = date1.isoweekday()
            if day1 == day_week:
                if (dictionary['Start Station'],dictionary['End Station']) in list(trip.keys()):
                    trip[(dictionary['Start Station'],dictionary['End Station'])] += 1
                else:
                    trip[(dictionary['Start Station'],dictionary['End Station'])] = 1

        key = list(trip.keys())
        value = list(trip.values())

        return key[value.index(max(value))]

def users(city_file, time_period):
    '''Finds the number of users for each user type based on the time period and
       returns the count of users for each user type

    Args:
        file name, time period
    Returns:
        (int,int) Count of users for user type subscriber and customer
    '''
    # TODO: complete function
    users = { }

    if time_period == 'none' :

        for dictionary in city_file:
            if dictionary['User Type'] in (None,""):
                continue
            elif dictionary['User Type'] in list(users.keys()):
                users[dictionary['User Type']] += 1
            else:
                users[dictionary['User Type']] = 1

        user_type = list(users.keys())

        if len(user_type) == 1:
            if 'Subscriber' in user_type:
                return ( users['Subscriber'], 0, 0 )
            elif 'Customer' in user_type:
                return ( 0, users['Customer'], 0 )
            elif 'Dependent' in user_type:
                return ( 0, 0, users['Dependent'] )

        elif len(user_type) == 2:
            if 'Subscriber' in user_type and 'Customer' in user_type:
                return ( users['Subscriber'], users['Customer'], 0 )
            elif 'Subscriber' in user_type and 'Dependent' in user_type:
                return ( users['Subscriber'], 0, users['Dependent'] )
            elif 'Customer' in user_type and 'Dependent' in user_type:
                return ( 0, users['Customer'], users['Dependent'] )

        elif len(user_type) == 3:
            if 'Subscriber' in user_type and 'Customer' in user_type and 'Dependent' in user_type:
                return ( users['Subscriber'], users['Customer'], users['Dependent'] )

        else:
            return (0, 0, 0)

        #return  ( users['Subscriber'], users['Customer'],users['Dependent'] )

    elif time_period == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:
            date = int(dictionary['Start Time'].split(' ')[0].split('-')[1])
            if date == month_num:
                if dictionary['User Type'] in (None,""):
                    continue
                elif dictionary['User Type'] in list(users.keys()):
                    users[dictionary['User Type']] += 1
                else:
                    users[dictionary['User Type']] = 1

        user_type = list(users.keys())

        if len(user_type) == 1:
            if 'Subscriber' in user_type:
                return ( users['Subscriber'], 0, 0 )
            elif 'Customer' in user_type:
                return ( 0, users['Customer'], 0 )
            elif 'Dependent' in user_type:
                return ( 0, 0, users['Dependent'] )

        elif len(user_type) == 2:
            if 'Subscriber' in user_type and 'Customer' in user_type:
                return ( users['Subscriber'], users['Customer'], 0 )
            elif 'Subscriber' in user_type and 'Dependent' in user_type:
                return ( users['Subscriber'], 0, users['Dependent'] )
            elif 'Customer' in user_type and 'Dependent' in user_type:
                return ( 0, users['Customer'], users['Dependent'] )

        elif len(user_type) == 3:
            if 'Subscriber' in user_type and 'Customer' in user_type and 'Dependent' in user_type:
                return ( users['Subscriber'], users['Customer'], users['Dependent'] )

        else:
            return (0, 0, 0)

        #return  ( users['Subscriber'], users['Customer'], users['Dependent'] )

    elif time_period == 'day':

        day1 = day

        for dictionary in city_file:
            date = dictionary['Start Time'].split(' ')[0].split('-')
            date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            day_week = date1.isoweekday()
            if day1 == day_week:
                if dictionary['User Type'] in (None,""):
                    continue
                elif dictionary['User Type'] in list(users.keys()):
                    users[dictionary['User Type']] += 1
                else:
                    users[dictionary['User Type']] = 1

        user_type = list(users.keys())

        if len(user_type) == 1:
            if 'Subscriber' in user_type:
                return ( users['Subscriber'], 0, 0 )
            elif 'Customer' in user_type:
                return ( 0, users['Customer'], 0 )
            elif 'Dependent' in user_type:
                return ( 0, 0, users['Dependent'] )

        elif len(user_type) == 2:
            if 'Subscriber' in user_type and 'Customer' in user_type:
                return ( users['Subscriber'], users['Customer'], 0 )
            elif 'Subscriber' in user_type and 'Dependent' in user_type:
                return ( users['Subscriber'], 0, users['Dependent'] )
            elif 'Customer' in user_type and 'Dependent' in user_type:
                return ( 0, users['Customer'], users['Dependent'] )

        elif len(user_type) == 3:
            if 'Subscriber' in user_type and 'Customer' in user_type and 'Dependent' in user_type:
                return ( users['Subscriber'], users['Customer'], users['Dependent'] )

        else:
            return (0, 0, 0)

        #return  ( users['Subscriber'], users['Customer'], users['Dependent'] )

def gender(city_file, time_period):
    '''Finds the number of users for each gender type based on the time period and
       returns the count of users for each gender type

    Args:
        file name, time period
    Returns:
        (int,int) Count of users for gender types Male and Female
    '''
    # TODO: complete function
    genders = { }

    if time_period == 'none' :

        for dictionary in city_file:
            if dictionary['Gender'] in (None,""):
                continue
            elif dictionary['Gender'] in list(genders.keys()):
                genders[dictionary['Gender']] += 1
            else:
                genders[dictionary['Gender']] = 1

        gender_type = list(genders.keys())

        if len(gender_type) == 1:
            if 'Male' in gender_type:
                return ( genders['Male'], 0)
            elif 'Female' in gender_type:
                return ( 0, users['Female'])


        elif len(gender_type) == 2:
            if 'Male' in gender_type and 'Female' in gender_type:
                return ( genders['Male'], genders['Female'] )

        else:
            return (0, 0)

        #return  ( genders['Male'], genders['Female'] )

    elif time_period == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:
            date = int(dictionary['Start Time'].split(' ')[0].split('-')[1])
            if date == month_num:
                if dictionary['Gender'] in (None,""):
                    continue
                elif dictionary['Gender'] in list(genders.keys()):
                    genders[dictionary['Gender']] += 1
                else:
                    genders[dictionary['Gender']] = 1

        gender_type = list(genders.keys())

        if len(gender_type) == 1:
            if 'Male' in gender_type:
                return ( genders['Male'], 0)
            elif 'Female' in gender_type:
                return ( 0, users['Female'])


        elif len(gender_type) == 2:
            if 'Male' in gender_type and 'Female' in gender_type:
                return ( genders['Male'], genders['Female'] )

        else:
            return (0, 0)

        #return  ( genders['Male'], genders['Female'] )

    elif time_period == 'day':

        day1 = day

        for dictionary in city_file:
            date = dictionary['Start Time'].split(' ')[0].split('-')
            date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            day_week = date1.isoweekday()
            if day1 == day_week:
                if dictionary['Gender'] in (None,""):
                    continue
                elif dictionary['Gender'] in list(genders.keys()):
                    genders[dictionary['Gender']] += 1
                else:
                    genders[dictionary['Gender']] = 1

        gender_type = list(genders.keys())

        if len(gender_type) == 1:
            if 'Male' in gender_type:
                return ( genders['Male'], 0)
            elif 'Female' in gender_type:
                return ( 0, users['Female'])


        elif len(gender_type) == 2:
            if 'Male' in gender_type and 'Female' in gender_type:
                return ( genders['Male'], genders['Female'] )

        else:
            return (0, 0)

        #return  ( genders['Male'], genders['Female'] )

def birth_years(city_file, time_period):
    '''Finds the yongest user, oldest user and most popular birth year based on
       the time period and returns the birth years

    Args:
        file name, time period
    Returns:
        (int,int,int) Birth years of oldest, youngest users and Most popular birth year
    '''
    # TODO: complete function

    years = { }

    if time_period == 'none' :

        for dictionary in city_file:
            if dictionary['Birth Year'] in (None,""):
                continue
            elif dictionary['Birth Year'] in list(years.keys()):
                years[dictionary['Birth Year']] += 1
            else:
                years[dictionary['Birth Year']] = 1

        key = list(years.keys())
        value = list(years.values())

        earliest = min(key)
        recent = max(key)
        popular = key[value.index(max(value))]

        return ( earliest, recent, popular )

    elif time_period == 'month':

        month1 = month
        month1 = month1.title()[:3]
        months = {v: k for k,v in enumerate(calendar.month_abbr)}
        month_num = months[month1]

        for dictionary in city_file:
            date = int(dictionary['Start Time'].split(' ')[0].split('-')[1])
            if date == month_num:
                if dictionary['Birth Year'] in (None,""):
                    continue
                elif dictionary['Birth Year'] in list(years.keys()):
                    years[dictionary['Birth Year']] += 1
                else:
                    years[dictionary['Birth Year']] = 1

        key = list(years.keys())
        value = list(years.values())

        earliest = min(key)
        recent = max(key)
        popular = key[value.index(max(value))]

        return ( earliest, recent, popular )

    elif time_period == 'day':

        day1 = day

        for dictionary in city_file:
            date = dictionary['Start Time'].split(' ')[0].split('-')
            date1 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            day_week = date1.isoweekday()
            if day1 == day_week:
                if dictionary['Birth Year'] in (None,""):
                    continue
                elif dictionary['Birth Year'] in list(years.keys()):
                    years[dictionary['Birth Year']] += 1
                else:
                    years[dictionary['Birth Year']] = 1

        key = list(years.keys())
        value = list(years.values())

        earliest = min(key)
        recent = max(key)
        popular = key[value.index(max(value))]

        return ( earliest, recent, popular )

def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        file name
    Returns:
        none.
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function

    start = 0
    end = 5

    while display.lower() == 'yes':
        for dictionary in city_file[ start : end ]:
            print(dictionary)
        start += 5
        end += 5

        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    if city.lower() == 'chicago':
        with open(chicago) as csv_file:
            list_of_dicts = [ { key : value for key, value in r.items() } for r in csv.DictReader(csv_file,skipinitialspace = True)]

    elif city.lower() == 'new york':
        with open(new_york_city) as csv_file:
            list_of_dicts = [ { key : value for key, value in r.items() } for r in csv.DictReader(csv_file,skipinitialspace = True)]

    elif city.lower() == 'washington':
        with open(washington) as csv_file:
            list_of_dicts = [ { key : value for key, value in r.items() } for r in csv.DictReader(csv_file,skipinitialspace = True)]

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        popular_m = popular_month( list_of_dicts, time_period )

        print("Most Popular Month is {}".format(popular_m))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        popular_d = popular_day( list_of_dicts, time_period )

        print("Most Popular Day is {}".format(popular_d))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_h = popular_hour( list_of_dicts, time_period )

    print("Most Popular Hour is {}".format(popular_h))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    total_trip, average_trip = trip_duration( list_of_dicts, time_period )

    print("Total Trip Duration is {}".format(total_trip))
    print("Average Trip Duration is {}".format(average_trip))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_start , popular_end = popular_stations( list_of_dicts, time_period )

    print("Most Popular Start Station is {}".format(popular_start))
    print("Most Popular End Station is {}".format(popular_end))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    start_s , end_s = popular_trip( list_of_dicts, time_period )

    print("Popular Trip is from {} station to {} station".format(start_s, end_s))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    subscriber_count, customer_count, Dependent_count = users( list_of_dicts, time_period )

    print("Count of Subscribers: {}, Count of Customers: {} and Count of Dependents: {}".format(subscriber_count, customer_count, Dependent_count))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    try:
        male, female = gender( list_of_dicts, time_period )
        print("Count of Male: {} and Count of Female: {}".format(male, female))

    except:
        print("Sorry -- Gender data is not available for Washington city ")


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    try:
        earliest, recent, popular_b = birth_years( list_of_dicts, time_period )
        print("Earliest Birth Year: {}, Youngest Birth Year: {} and Most Popular Birth Year: {}".format(earliest, recent, popular_b))

    except:
        print("Sorry -- Birth Year data is not available for Washington city")

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data( list_of_dicts )

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()

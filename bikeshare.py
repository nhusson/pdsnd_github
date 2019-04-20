
import time
import pandas as pd
import numpy as np

#declaring global variables

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']

#change 1
def show_rawdata(df):
    """
    Ask the user if he wishes to see the raw data file. The data will be paged by increment of 5 records at a time, the user can
    stop the paging after each iteration

    Returns:
        None
    """
    #removing extra columns
    df = cleanup_data(df)
    
    for index,row in df.iterrows():
        print(row)
        if index % 5 == 0 and index>0:
            continue_rawdata = input("Do you want to see the next 5 records of the raw data? (yes/no)").lower()
            if continue_rawdata!="yes":
                break
    
    
        
        
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease enter a city (chicago, new york city or washington).\n').lower()
        if (city in CITY_DATA):
            break
        print('Invalid city!')    

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input('\nPlease enter a month (all, january, february, ... , june).\n').lower()
        if (month in MONTHS or month=='all'):
            break
        print('Invalid Month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease enter a day of week (all, monday, tuesday, ... sunday).\n').lower()
        if (day in DAYS or day=='all'):
            break
        print('Invalid Day of Week!')

    print('-'*40)
    return city, month, day

def cleanup_data(df):
    """
    Cleans up the data frame and removes the extra columns.

    Args:
        (df) dataframe - the dataframe to be cleaned up
        
    Returns:
        df - Pandas DataFrame removed from the extra columns initially created for the stats calculation
    """
    
    df = df.drop(columns=['Start End Combo', 'month', 'day_of_week'])
    
    return df
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Start Time'].dt.month.mode()[0]

    print ('Most Commont Month: ' + MONTHS[popular_month-1])
    # TO DO: display the most common day of week
    popular_week = df['Start Time'].dt.week.mode()[0]

    print ('Most Commont Week: ', popular_week)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print ('Most Commont Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]

    print ('Most Popular Start Station: ' + popular_startstation)
    

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]

    print ('Most Popular End Station: ' + popular_endstation)
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Combo'] = df['Start Station'] + '/' + df['End Station']
    popular_startendstation = df['Start End Combo'].mode()[0]

    print ('Most Frequent combo of Start & End Station: ' + popular_startendstation)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    
    print('Total Travel Time:', total_travel)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print ('Mean Travel Time', mean_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('User Types Count:\n', user_types)    

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nGender Count:\n', gender)    
    else:
        print('\nGender Count: Not Available\n')    
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest Year of Birth:', int(df['Birth Year'].min()))
        print('Most Recent Year of Birth:', int(df['Birth Year'].max()))
        print('Most Common of Birth:', int(df['Birth Year'].mode()[0]))
    else:
        print('Birth Year data not available')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        #ask user for desired filters
        city, month, day = get_filters()
        
        #load data based on provided filters
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        continue_rawdata = input("Do you want to take a look at the raw data? (yes/no)").lower()
        if continue_rawdata=="yes":
            show_rawdata(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

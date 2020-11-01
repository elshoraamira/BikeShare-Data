import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    month = "all"
    day = "all"
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ]

    city = input("Would you like to see stats about Chicago, New york city or Washington? Type city name: \n")
    while city.lower() not in CITY_DATA:
        city = input("Invalid input please choose an existing city or recheck for spelling mistakes: \n")

    filter = ['month', 'day', 'both', 'nothing']
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    filterBy = input("Would you like to filter data by 'month', 'day', 'both' or 'nothing': \n")
    while filterBy.lower() not in filter:
        filterBy = input("Invalid input! Please choose from: 'month', 'day', 'both' or 'nothing': \n")

    if filterBy.lower() == 'month' or filterBy.lower() == 'both':
        month = input("Please enter the desired month: 'january', 'february', 'march', 'april', 'may', 'june' \n")
        while month.lower() not in months:
            month = input("Invalid input! Kindly rechoose from: 'january', 'february', 'march', 'april', 'may', 'june' \n")
    if filterBy.lower() == 'day' or filterBy.lower() == 'both':
        day = input("Please enter the desired day: 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'  \n")
        while day.lower() not in days:
            day = input("Invalid input! Kindly rechoose from: 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' \n")

    print('-'*80)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

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

    #change start time to datetime
    #get the hours
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour

    # display the most common month
    if len(df['month'].unique()) > 1:
        popular_month = df['month'].mode()[0]
        count_month = df['month'].value_counts().tolist()
        print("The most commom month is: {} with count of: {} \n".format(popular_month, count_month[0]))

    # display the most common day of week
    if len(df['day_of_week'].unique()) > 1:
        popular_day = df['day_of_week'].mode()[0]
        count_day = df['day_of_week'].value_counts().tolist()
        print("The most commom day is: {} with count of: {} \n".format(popular_day, count_day[0]))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    count_hour = df['hour'].value_counts().tolist()
    print("The most commom hour is: {} - with count of: {} \n".format(popular_hour, count_hour[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_startStation = df['Start Station'].mode()[0]
    count_startSTation = df['Start Station'].value_counts().tolist()
    print("Most common Start station is: {}            Count: {}".format(popular_startStation, count_startSTation[0]))
    # display most commonly used end station
    popular_endStation = df['End Station'].mode()[0]
    count_endSTation = df['End Station'].value_counts().tolist()
    print("Most common End station is: {}            Count: {}".format(popular_endStation, count_endSTation[0]))
    # display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    count_trip = (df['Start Station'] + " - " + df['End Station']).value_counts().tolist()
    print("Most common Trip is: {}            Count: {}".format(popular_trip, count_trip[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total tavel time: {}".format(total_travel_time))
    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Average tavel time: {}".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("Count of each user type:\n{}\n".format(count_user_types.to_string()))

    #check for gender and birthyear if existing
    if len(list(df.columns)) >= 11:
        # Display counts of gender
        count_gender = df['Gender'].value_counts()
        print("Count of each gender:\n{}\n".format(count_gender.to_string()))
        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year is: {}".format(int(earliest_year)))
        mostrecent_year = df['Birth Year'].max()
        print("The most recent birth year is: {}".format(int(mostrecent_year)))
        mostcommon_year = df['Birth Year'].mode()[0]
        print("The most common birth year is: {}".format(int(mostcommon_year)))
    else:
        print("No Gender data available \n")
        print("No Birth year data availble \n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def display_raw_data(city):
    user_input = input("Do you want to print a sample of the data? type 'yes' or 'no': ")
    while(user_input.lower() =="yes"):
        df = pd.read_csv(CITY_DATA[city.lower()])
        sample_data = df.sample(n = 5)
        for i in range(len(sample_data)):
            sr = sample_data.iloc[i]
            dt = sr.to_dict()
            print(" ")
            for key, val in dt.items():
                print('{}: {}'.format(key, val))
            print(" ")

        user_input = input("Do you want to print another sample of the data? type 'yes' or 'no': ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

# df.head()
# df.columns
# df.describe()
# df.info()
# df['column_name'].value_counts()
# df['column_name'].unique()



import time
import pandas as pd
import numpy as np

CITY_DATA = { 'C': 'chicago.csv',
              'N': 'new_york_city.csv',
              'W': 'washington.csv' }

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
    city = 'none'
    test = 0
    while test == 0:
        city_input = input("What city would you like to explore?  Enter \"C\" for Chicago, \"N\" for New York City or \"W\" for Washington: ")
        city = city_input[0].upper()
        
        if city != "C" and  city != "N" and  city != "W":
            print("The value you entered is not valid, please try again.\nWhat city would you like to explore?  Enter \"C\" for Chicago, \"N\" for New York City or \"W\" for Washington:")
        else:
            print("Thank you!  You chose {}!".format(city))
            test = 1
            break
    
    
    
    # get user input for month (all, january, february, ... , june)
   
    month = 'none'
    test = 0
    while test == 0:
        month_input = input("What month would you like to analyze?  Enter JAN, FEB, MAR, APR, MAY, JUN or ALL:")
        month = month_input[0:3].upper()
        
        if month != "JAN" and month != "FEB" and month != "MAR" and month != "APR" and month != "MAY" and month != "JUN" and month != "ALL":
            print("The value you entered is not valid, please try again.\n What month would you like to analyze?  Enter JAN, FEB, MAR, APR, MAY, JUN or ALL:")
        else:    
            print("Thank you!  You chose {}!".format(month))
            test = 1
            break
      
      
    
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_short = 'none'
    test = 0
    while test == 0:
        day_input = input("What day or the week would you like to analyze?  Enter Mon, Tue, Wed, Thu, Fri, Sat, Sun or All:")
        day_short = day_input[0:3].upper()
        print(day_short)
        if day_short != "MON" and day_short != "TUE" and day_short != "WED" and day_short != "THU" and day_short != "FRI" and day_short != "SAT" and day_short != "SUN" and day_short != "ALL":
            print("The value you entered is not valid, please try again.\nWhat day or the week would you like to analyze?  Enter Mon, Tue, Wed, Thu, Fri, Sat, Sun or All:")
        else:    
            if day_short == "MON":
                day="Monday"
            elif day_short == "TUE":
                day="Tuesday"
            elif day_short == "WED":
                day="Wednesday"
            elif day_short == "THU":
                day="Thursday"    
            elif day_short == "FRI":
                day="Friday"    
            elif day_short == "SAT":
                day="Saturday"    
            elif day_short == "SUN":
                day="Sunday"   
            elif day_short == "ALL":
                day = "ALL"
            test = 1
            print("Thank you!  You chose {}!".format(day))
            break      
 
    print('-'*40)
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


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    # filter by month if applicable
    if month != 'ALL':
        # use the index of the months list to get the corresponding int
        months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    

    # filter by day of week if applicable
    if day != 'ALL':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
   
    return df




def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    #---------------------------------------------------
    # display the most common month
    #---------------------------------------------------

    if month == "ALL":
        # extract month from the Start Time column to create a month column
        df['month'] = df['Start Time'].dt.month

        # find the most popular month
        popular_month = df['month'].mode()[0]
        
        if popular_month == 1:
            print_month = "January"
        elif popular_month == 2:
            print_month = "February"
        elif popular_month == 3:
            print_month = "March"
        elif popular_month == 4:
            print_month = "April"
        elif popular_month == 5:
            print_month = "May"
        elif popular_month == 6:
            print_month = "June"
    

        print('Most Popular month:', print_month)
    
    else:
        print("This data is only for the month of " + month)

    #---------------------------------------------------
    # display the most common day of week
    #---------------------------------------------------

    if day == "ALL":
        # extract day from the Start Time column to create a day column
        df['weekday'] = df['Start Time'].dt.weekday

        # find the most popular day
        popular_day = df['weekday'].mode()[0]
        
        if popular_day == 0:
            print_day = "Monday"
        elif popular_day == 1:
            print_day = "Tuesday"
        elif popular_day == 2:
            print_day = "Wednesday"
        elif popular_day == 3:
            print_day = "Thursday"
        elif popular_day == 4:
            print_day = "Friday"
        elif popular_day == 5:
            print_day = "Saturday"
        elif popular_day == 6:
            print_day = "Sunday" 

        print('Most Popular day:', print_day)
    
    else:
        print("This data is only for " + day)
        
    #---------------------------------------------------
    # display the most common start hour
    #---------------------------------------------------

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    #---------------------------------------------------
    # display most commonly used start station
    #---------------------------------------------------
    
    # find the most popular start station
    popular_start = df['Start Station'].mode()[0]
        
    print('Most Popular start station:', popular_start)
    
    
    #---------------------------------------------------
    # display most commonly used end station
    #---------------------------------------------------
    
    # find the most popular end station
    popular_end = df['End Station'].mode()[0]
        
    print('Most Popular end station:', popular_end)

    #---------------------------------------------------
    # display most frequent combination of start station and end station trip
    #---------------------------------------------------

    # extract hour from the Start Time column to create an hour column
    df['Start End'] = "From: " + df['Start Station']+ " To: " + df['End Station']
    
    # find the most popular combination of start and end station
    popular_start_end = df['Start End'].mode()[0]
        
    print('Most Popular trip: ', popular_start_end)


    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')


    # display total travel time
    sum_travel_time = df['Trip Duration'].sum()
    total_travel_time = sum_travel_time / 3600
    print("Total travel time is ", total_travel_time, " hours")

    # display mean travel time
    mean_travel_sec = df['Trip Duration'].mean()
    mean_travel_min = mean_travel_sec / 60
    print("Average travel time is ", mean_travel_min, " min")


    print('-'*40)




def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    
    # Display counts of user types
    print('\nCount by user type:\n')
    user_types = df['User Type'].value_counts()
    print(user_types)


    if city == "C" or city == "N":
    
        # Display counts of gender
        print('\nCount by gender:\n')
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

        # Display earliest year of birth
        early_year = int(df['Birth Year'].min())
        print("\nEarliest birth year is:", early_year)


        # Display most recent year of birth
        last_year = int(df['Birth Year'].max())
        print("\nLatest birth year is:", last_year)
 
        # Display most common year of birth
        common_year = int(df['Birth Year'].mode())
        print("\nMost common birth year is:", common_year)

    else:
        print("\nWashington does not have gender nor birth data available\n")

 
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #give user option to view data 10 rows at a time
        
        view_ten = input('\nWould you like to view 10 lines of sample data? Enter yes or no.\n')
        more = view_ten[0].lower()
        rows_viewed = 0
        while more == 'y':
            
            if more == 'y':
                rows_viewed += 10
                data_sample = df.head(rows_viewed)
                print(data_sample)
                view_more = input('\nWould you like to add 10 lines to the sample data? Enter yes or no.\n')
                more = view_more[0].lower()
            else:
                more = 'n'
                break

    
    
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        #Give user option to restart
        restart_input = input('\nWould you like to restart? Enter yes or no.\n')
        restart = restart_input[0].lower()
        
        if restart != 'y':
        
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
               'new york city': 'new_york_city.csv',
               'washington': 'washington.csv' }


#####  the (optimize_input) function takes two arguments the first is an input and the second is a number which is considered a specefic mark for this input.
#####  the (optimize_input) runs a while true loop which will run indefinitely until two conditions happen then breaks.
#####  the first condition is the output for the input (question) being within a specefic list and the second condition is the number (question_rank) being matching a specefic number. 
#####  if any of the two conditions has not happened a specefic message will appear and the loop continue. 
#####  the (optimize_input) function will be nested inside the (get_filters) function which contain 3 inputs(question) with 3 numbers(question_rank).

def optimize_input(question , question_rank):
  while True:
    answer = input(question)
    
    if answer.lower().strip() in['chicago','new york city','washington'] and question_rank==1:
      break
    elif answer.lower().strip() in['january', 'february', 'march', 'april', 'may', 'june','all'] and question_rank ==2:
      break
    elif answer.lower().strip() in['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','all'] and question_rank ==3:
      break
    else:
      if question_rank ==1:
        print('Undefined city!\nOnly data for Chicago, New york city, Washington are available.')
      if question_rank ==2:
        print('Undefined month!\nOnly data for the first six months are available.')
      if question_rank ==3:
        print('Undefined day.')
  return answer.lower().strip() 
      
     
  
     
      

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
    city = optimize_input('Which city data do you like to explore ?\nChicago, New york city or Washington.\n',1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = optimize_input('Which month ?\nJanuary, February, March, April, May, June or all.\n',2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = optimize_input('which day ?\nMonday, Tuesday, ... or all.\n',3)
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
    df = pd.read_csv(CITY_DATA[city])                                   # Use Pandas read_csv function to read csv file and do operations on it.
    df['Start Time'] = pd.to_datetime(df['Start Time'])                 # Use Pandas to_datetime method to convert string Date time into Python Date time.
    df['month'] = df['Start Time'].dt.month                             # Extract month from the Start time column in a new column.
    df['day'] = df['Start Time'].dt.day_name()                          # Extract day from the Start time column in a new column.
    
    if month != 'all':
      months = ['january', 'february', 'march', 'april', 'may', 'june']   # Convert month name into month number by using index of months list 
      month = months.index(month)+1
      df = df[df['month'] == month]                                       # Create new data frame contain the choosen month
    if day != 'all':
      df = df[df['day'] == day.title()]                                   # Create new data frame contain the choosen day which must be capitalized to match the day name extracted by the (dt.day_name) method.
    return df



  


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']          # Convert month number into month name by using index of months list.
    month = df['month'].mode()[0]                                              # use mode function to calculate the most frequent month.
    print('Most frequent month is : %s' % (months[month-1]) )

    # TO DO: display the most common day of week
    print('Most frequent day is : %s' % df['day'].mode()[0])           # use mode function to calculate the most frequent month.

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour                                      # Extract hour from the Start time column in a new column.
    print('Most frequent hour is : %s' % df['hour'].mode()[0])                 # use mode function to calculate the most frequent hour.


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]                                           # use mode function to calculate the most frequent start station.
    print(f'Most popular start station is : {popular_start}')
    
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]                                                 # use mode function to calculate the most frequent end station.
    print(f'Most popular end station is : {popular_end}')

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = 'from ' + df['Start Station'] + ' to ' + df['End Station']               # concatinate the start and end stations in a new column 
    print('Most popular trip is %s' % popular_combination.mode()[0])             # use mode function to calculate the most frequent combination of stations.

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    

    # TO DO: display total travel time
    print('Total travel time is : %s minutes' % ((df['Trip Duration'].sum())/60))                  # use sum function to calculate the total travel time

    # TO DO: display mean travel time
    print('Average travel time is : %s minutes' % ((df['Trip Duration'].mean())/60))               # use mean function to calculate the average travel time.

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

                                                                 #####################################################################################
def user_stats(df,city):                                         ####   the argument (city) has been added to the function to allow displaying    ####  
    """Displays statistics on bikeshare users."""                ####        gender and year of birth data according to the choosen city          ####
                                                                 #####################################################################################
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())                                         # Use value_counts method to get the count of unique entries in user type column.

    # TO DO: Display counts of gender
    if city!= 'washington':                                                       # displaying data about gender and birth year in case of chicago and new york as these data are not available for washington.         
      print(df['Gender'].value_counts())                                          # Use value_counts method to get the count of unique entries in gender column

    # TO DO: Display earliest, most recent, and most common year of birth         # Use max, min and mean functions to Display earliest, most recent, and most common year of birth.
      print("Most common year of birth is : %s" % df['Birth Year'].mode()[0])
      print("Most recent year of birth is : %s" % df['Birth Year'].max())
      print("Most earliest year of birth is : %s" % df['Birth Year'].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):                                                      # Ask the user if he wants to display raw data
  raw = input('would you like to display raw data ?\n').strip()
  if raw.lower() == 'yes':
    x = 0 
    while True:
      print(df.iloc[x:x+5])
      x += 5
      ask = input('would you like to display next five rows ?\n').strip()
      if ask.lower() != 'yes':
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            break


if __name__ == "__main__":
  main()
    
          

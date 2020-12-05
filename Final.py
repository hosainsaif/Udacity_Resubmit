#This comment was added throgh the branch 'refactoring'. This code
#helps you understand some business statistics about the bikehsare company

#The best lesson I learned here is that when debugging, print variables
#in each sequence/operation. That way, you will find out where you're messing
#it up.
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    print("Hello! Let\'s explore some US bikeshare data! In this program, you will give us some inputs and we will spit out some Bikeshare wisdome that you will love.")


    while True:
        city = input("Hey sunshine! What city are we looking at today? Chicago, New York City, Washington?").lower()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Hmmm... this does not seem one of the cities I mentioned above...Try again")

        else:
            break


    while True:
        month = input('Ok, what month are you looking for? For all months please type all\n').lower()
        if month.lower() not in ('all','january', 'february', 'march', 'april', 'may','june', 'july','august','september','october','november','december'):
            print('Choose a valid option')

        else:
            break



    while True:
        day = input('Which day of the week? \n all, sunday, monday, tuesday, wednesday, thursday, friday or saturday\n')
        if day not in ('all','sunday', 'monday', 'tuesday',
                                 'wednesday', 'thursday', 'friday','saturday'):
            print('Choose a valid option')

        else:
            break


    print("-"*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.weekday

    if month != 'all':
        print(month)
        print(df['month'])
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
        day = days.index(day) + 1
        df = df[df['day'] == day]



    return df


#The following function displays the most common month for rides, day and hour
def time_stats(df):
    # TO DO: display the most common month
    mostc_month = df["month"].mode()
    print("Common month in numbers is:\n",mostc_month)
    # TO DO: display the most common day of week
    mostc_day = df["day"].mode()
    print("Common day in numbers :\n",mostc_day)
    # TO DO: display the most common start hour
    mostc_hour= df["Start Time"].dt.hour.mode()
    print("Common hour is:\n",mostc_hour)

    print("-"*40)

def station_stats(df):

    # TO DO: display most commonly used start station
    mostc_startstation=df["Start Station"].mode()
    print("Common start station is:\n",mostc_startstation)
    # TO DO: display most commonly used end station
    mostc_endstation=df["End Station"].mode()
    print("Common end station is:\n",mostc_endstation)
    # TO DO: display most frequent combination of start station and end station trip
    df["combined"]= (df["Start Station"]+ ' '+ df["End Station"]).mode()
    combined1=df["combined"]
    print("Combined stations are:\n ",combined1)

    print("-"*40)



def trip_duration_stats(df):

    # TO DO: display total travel time
    trip_duration = (df["Trip Duration"].sum())/3600
    print("Total travel time in hours:\n",trip_duration)
    # TO DO: display mean travel time
    Ave_trip_duration = (df["Trip Duration"].mean())/60
    print("Average Trip duration in minutes:\n",Ave_trip_duration)

    print("-"*40)

def user_stats(df):

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Type is:\n",user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:

        genders = df['Gender'].value_counts().keys()
        count_genders = df['Gender'].value_counts().tolist()
        genders_count = dict(zip(genders,count_genders))
        print(genders_count)
    else:
        print('\nColumn Gender does not exist in dataset')


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    print("Earliest birth year:\n",earliest_birth)
    recent_birth = df['Birth Year'].max()
    print("Most recent birth year:\n",recent_birth)
    common_birth = df['Birth Year'].mode()
    print("Most common birth year:\n",common_birth)

    print("-"*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if (city != 'chicago'and city != 'new york city'):
            print('There are no gender and birth year data')
        else:
            user_stats(df)

        data = input("Would you like to see raw data?").lower().strip()

        count =0
        lines=0
        while(data != 'no'):

                print(df.iloc[count:lines+5])
                lines += 5
                count += 5
                data=input('You would like to view the 5 lines of the dataset? Enter yes or no.\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

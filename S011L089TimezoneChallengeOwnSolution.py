#
# TIM BUCHALKA'S COMPLETE PYTHON MASTERCLASS Created by Tim Buchalka, Jean-Paul Roberts,
# Tim Buchalka's Learn Programming Academy.
# This is a collection of my codes, generated by myself for learning Python
# This challenge is about understanding timezones and pytz package methods in Python.
# Here is a link to the course: https://www.udemy.com/python-the-complete-python-developer-course/
# Authors of the challenge (definition of what to code)
#
# Tim Buchalka
# https://www.udemy.com/user/timbuchalka/
# https://github.com/tim-buchalka
#
# Jean-Paul Roberts
# https://www.udemy.com/user/jeanpaulroberts/
#
# START OF CHALLENGE (TIM BUCHALKA, JEAN-PAUL ROBERTS)
#
# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
#
# END OF THE CHALLENGE (TIM BUCHALKA, JEAN-PAUL ROBERTS)
#
# Python 3.7.0
# IntelliJ IDEA 2019.1.3 (Community Edition)
# Windows 10, 64 bit
#
# START OF MY OWN CODE
#

import datetime
import pytz

timezones = {0: "quit",
             1: "GB",
             2: "FR",
             3: "US - New York",
             4: "US - Pacific/Honolulu",
             5: "China - Asia/Shanghai",
             6: "China - Asia/Urumqi",
             7: "Australia - Australia/Sydney",
             8: "Australia - Pacific",
             9: "India - Asia/Kolkata"
             }

timezoneDict = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
timezoneDict[1] = {"country_names": "Britain (UK)", "country_timezones": "Europe/London"}
timezoneDict[2] = {"country_names": "France", "country_timezones": "Europe/Paris"}
timezoneDict[3] = {"country_names": "United States", "country_timezones": "America/New_York"}
timezoneDict[4] = {"country_names": "United States", "country_timezones": "Pacific/Honolulu"}
timezoneDict[5] = {"country_names": "China", "country_timezones": "Asia/Shanghai"}
timezoneDict[6] = {"country_names": "China", "country_timezones": "Asia/Urumqi"}
timezoneDict[7] = {"country_names": "Australia", "country_timezones": "Australia/Sydney"}
timezoneDict[8] = {"country_names": "Australia", "country_timezones": "Australia/Melbourne"}
timezoneDict[9] = {"country_names": "India", "country_timezones": "Asia/Kolkata"}


# # testing how to retrieve data from dictionary by key - start
# timezoneDict[1] = {"country_names": "Britain (UK)", "country_timezones": "Europe/London"}
# print(timezoneDict[1])
# print(timezone+Dict[1].get("country_names"))
# print(timezoneDict[1].get("country_timezones"))
# # testing how to retrieve data from dictionary by end - start

# # just a short check for printing out a time in a certain timezone - V1
# tz_to_display = pytz.timezone("Europe/London")
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The local time in {} is {}".format(tz_to_display, local_time))

# # just a short check for printing out a time in a certain timezone - V2
# tz_to_display = pytz.timezone(timezoneDict[1].get("country_timezones"))
# local_time_now = datetime.datetime.now(tz=tz_to_display)
# print("The local time in {} is {}".format(tz_to_display, local_time_now))

# # just a short check for printing out a time in a certain timezone - V3
# for tzID in range(1, 4):
#     print(tzID)
#     tz_to_display = pytz.timezone(timezoneDict[tzID].get("country_timezones"))
#     local_time_now = datetime.datetime.now(tz=tz_to_display)
#     print("The local time in {} is {}".format(tz_to_display, local_time_now))

tzID = 0

while True:
    for tzID in timezones:
        print("{}: {}".format(tzID, timezones[tzID]))
    inputString = (input("Please select a timezone to display: "))
    if len(inputString) == 0:
        print("WARNING: Please enter a valid input!")
    else:
        tzID = int(inputString)
        if tzID == 0:
            break
        elif tzID not in timezones:
            print("The selected timezone is not valid")
        else:
            naive_utc_time_now = datetime.datetime.utcnow()  # naive UTC - CHECKED
            print("\tnaive UTC time in {}:\t\t\t\t\t\t\t\t\t\t{}".format(naive_utc_time_now.tzinfo, naive_utc_time_now))

            aware_utc_time_now = pytz.utc.localize(naive_utc_time_now)  # aware UTC - CHECKED
            print("\taware UTC time in {}:\t\t\t\t\t\t\t\t\t\t{}".format(aware_utc_time_now.tzinfo, aware_utc_time_now))
            print("")

            # print("\tformat(timezones[tzID]: {}".format(timezones[tzID]))
            # print("country_names: {}".format(timezoneDict[tzID].get("country_names")))
            # print("country_timezones: {}".format(timezoneDict[tzID].get("country_timezones")))
            country = timezoneDict[tzID].get("country_timezones")
            timezone_to_display = pytz.timezone(country)

            # NAIVE local time in selected country
            naive_local_time_in_selected_country = datetime.datetime.now(tz=timezone_to_display)
            print("\tnaive local time in {}:\t\t\t\t\t\t\t{}".format(timezone_to_display, naive_local_time_in_selected_country))

            # AWARE local time in selected country
            aware_local_time_in_selected_country = pytz.utc.localize(naive_utc_time_now).astimezone(timezone_to_display)
            print("\taware local time in {}:\t\t\t\t\t\t\t{}".format(timezone_to_display, aware_local_time_in_selected_country))
            print("")

            # NAIVE local time on the user's system - CHECKED
            naive_local_time_now = datetime.datetime.now()
            print("\tnaive local time in {}:\t\t\t\t\t\t\t\t\t{}".format(naive_local_time_now.tzinfo, naive_local_time_now))

            # AWARE local time on the user's system
            aware_local_time_now = pytz.utc.localize(naive_utc_time_now).astimezone()
            print("\taware local time in {}:\t\t\t\t{}".format(aware_local_time_now.tzinfo, aware_local_time_now))





# TODO
# printing out user's timezone as well
# example
# aware_local_time = pytz.utc.localize(utc_time).astimezone()
# aware_utc_time = pytz.utc.localize(utc_time)
# local_time = datetime.datetime.now()
# utc_time = datetime.datetime.utcnow()
#
# print("Naive local time {}".format(local_time))
# print("Naive UTC {}".format(utc_time))
# print("")
#
# aware_local_time = pytz.utc.localize(utc_time).astimezone()
# aware_utc_time = pytz.utc.localize(utc_time)
#
#
# print("Aware local time {}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
# print("Aware UTC {}. time zone {} ".format(aware_utc_time, aware_utc_time.tzinfo))
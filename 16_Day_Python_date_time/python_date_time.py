# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, date

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(day, month, year, hour, minute, timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

time_formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_formatted)

# Today is 5 December, 2019. Change this time string to time.

date_string = "5 December, 2019"

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# Calculate the time difference between now and new year.

today = date(year=2024, month=12, day=2)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print("Time left for new year: ", time_left_for_newyear)

# Calculate the time difference between 1 January 1970 and now.

new_date = date(year=1970, month=1, day=1)
diference = today - new_date
print(diference)

# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# Make an counter app
# To schedule appointments